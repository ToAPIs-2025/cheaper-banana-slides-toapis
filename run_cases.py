"""Run the patched upstream Banana Slides provider and its image PPTX exporter.
No generation occurs without --live. One image per case; durable task receipts.
"""
import argparse,importlib.util,sys,types,json,os,time,hashlib
from pathlib import Path
from PIL import Image

def load_source(source):
    backend=source/'backend';sys.path.insert(0,str(backend))
    # Import the real provider module without initializing unused vendor integrations.
    for name,folder in [('services',backend/'services'),('services.ai_providers',backend/'services/ai_providers'),('services.ai_providers.image',backend/'services/ai_providers/image'),('utils',backend/'utils')]:
        m=types.ModuleType(name);m.__path__=[str(folder)];sys.modules[name]=m
    name='services.ai_providers.image.openai_provider';spec=importlib.util.spec_from_file_location(name,backend/'services/ai_providers/image/openai_provider.py');m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m)
    return m.OpenAIImageProvider

def read_env(path):
    vals={}
    for line in Path(path).read_text(encoding='utf-8-sig').splitlines():
        if '=' in line and not line.lstrip().startswith('#'):
            k,v=line.split('=',1);vals[k.strip()]=v.strip().strip('\"\x27')
    return vals

def main():
    p=argparse.ArgumentParser();p.add_argument('--upstream',type=Path,required=True);p.add_argument('--output',type=Path,default=Path('results'));p.add_argument('--key-file');p.add_argument('--live',action='store_true');p.add_argument('--export-only',action='store_true');p.add_argument('--case',default='all');a=p.parse_args()
    cases=json.loads((Path(__file__).parent/'cases/briefs.json').read_text(encoding='utf-8'))
    if a.case!='all':cases=[c for c in cases if c['id']==a.case]
    if not cases:raise SystemExit('Unknown case')
    if not a.live and not a.export_only:
        print(json.dumps({'dryRun':True,'cases':cases,'generationCalls':0},ensure_ascii=False,indent=2));return
    if a.export_only:
        backend=a.upstream.resolve()/'backend';sys.path.insert(0,str(backend))
        package=types.ModuleType('utils');package.__path__=[str(backend/'utils')];sys.modules['utils']=package
    else:
        vals=read_env(a.key_file) if a.key_file else os.environ
        key=vals.get('TOAPIS_API_KEY');base=vals.get('TOAPIS_BASE_URL','https://toapis.cn')
        if not key:raise SystemExit('Configure TOAPIS_API_KEY privately')
        Provider=load_source(a.upstream.resolve())
    a.output.mkdir(parents=True,exist_ok=True)
    os.environ['TOAPIS_STATE_DIR']=str(a.output/'private-state')
    records=[]
    for case in cases:
        folder=a.output/case['id'];folder.mkdir(exist_ok=True)
        if (folder/'evidence.json').exists():
            records.append(json.loads((folder/'evidence.json').read_text(encoding='utf-8')));continue
        if a.export_only:raise SystemExit('Missing completed case '+case['id']+'; export-only never generates images')
        os.environ['TOAPIS_RUN_ID']=case['id']
        provider=Provider(api_key=key,api_base=base+'/v1' if not base.rstrip('/').endswith('/v1') else base,model=case['model'],image_quality=case.get('quality') or 'auto')
        start=time.monotonic();refs=[Image.open(a.output/r) for r in case.get('references',[])]
        image=provider.generate_image(case['prompt'],refs,aspect_ratio=case['ratio'],resolution='1K')
        if image is None:raise RuntimeError('Provider returned no image')
        image.save(folder/'result.png')
        r={'project':'Anionex/banana-slides','upstream_sha':'8bcde44c95646a863b23b1e4fc43c9a42ea4e3f7','checkedDate':'2026-10-13','case':case,'status':'completed','task_id':provider._toapis_provider.last_receipt['task_id'],'elapsed_seconds':round(time.monotonic()-start,2),'pixels':list(image.size),'output_sha256':hashlib.sha256((folder/'result.png').read_bytes()).hexdigest(),'billing':provider._toapis_provider.last_receipt.get('billing'),'method':'patched upstream OpenAIImageProvider.generate_image','scope':'backend provider; frontend not tested'}
        (folder/'evidence.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8');records.append(r);print(json.dumps({'case':case['id'],'task_id':r['task_id'],'pixels':r['pixels'],'elapsed':r['elapsed_seconds']}),flush=True)
    # Use the real upstream image-only PPTX exporter for each three-slide sequence.
    if a.case=='all':
        spec=importlib.util.spec_from_file_location('banana_export',a.upstream/'backend/services/export_service.py');exp=importlib.util.module_from_spec(spec);sys.modules['banana_export']=exp;spec.loader.exec_module(exp)
        for route in ['standard','vip-low']:
            paths=[str(a.output/c['id']/'result.png') for c in cases if c['route']==route]
            exp.ExportService.create_pptx_from_images(paths,str(a.output/(route+'-three-slides.pptx')),'16:9')
        print(json.dumps({'export':'two three-slide image-only PPTX files','nativeEditableElements':False}))
    (a.output/'runs.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__':main()
