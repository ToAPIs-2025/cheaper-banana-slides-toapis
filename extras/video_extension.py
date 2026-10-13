"""Independent ToAPIs image-to-video extension; not a Banana Slides video provider."""
import argparse,json,re,time,hashlib,urllib.request,urllib.error,uuid
from pathlib import Path
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*a,**kw):return None
p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,default=Path('video-result'));p.add_argument('--key-file');p.add_argument('--live',action='store_true');a=p.parse_args()
body={'model':'grok-video-1.5','prompt':'A calm premium coffee product film. Very slow camera push-in, delicate natural steam drifting above the ivory espresso cup, subtle warm light movement. Keep the cup and studio composition recognizable. No new objects, no text, no logos.','video_generation_mode':'first_frame_image_to_video','duration':4,'resolution':'480p','aspect_ratio':'16:9'}
if not a.live:print(json.dumps({'dryRun':True,'request':body,'image':'<uploaded first-frame URL>','paidCalls':0},ensure_ascii=False,indent=2));raise SystemExit(0)
key=re.search(r'^TOAPIS_API_KEY\s*=\s*(.+)$',Path(a.key_file).read_text(encoding='utf-8-sig'),re.M).group(1).strip().strip('\"\x27')
http=urllib.request.build_opener(NoRedirect);origin='https://toapis.cn';a.output.mkdir(parents=True,exist_ok=True);receipt=a.output/'receipt.json'
def api(path,data=None,content_type='application/json'):
    payload=json.dumps(data).encode() if isinstance(data,dict) else data
    req=urllib.request.Request(origin+'/v1/'+path,data=payload,headers={'Authorization':'Bearer '+key,'Content-Type':content_type},method='POST' if payload is not None else 'GET')
    with http.open(req,timeout=60) as r:return json.load(r)
record=json.loads(receipt.read_text(encoding='utf-8')) if receipt.exists() else None
if record and not record.get('task_id'):raise SystemExit('Prior submission is uncertain. Reconcile Task Logs before starting another.')
if not record:
    price=api('pricing?model=grok-video-1.5')
    rows=[x for m in price.get('data',[]) for x in m.get('prices',[]) if x.get('conditions',{}).get('resolution')=='480p' and x.get('conditions',{}).get('input_image_count')==1 and x.get('conditions',{}).get('duration') in ('4s','4',4) and x.get('unit')=='second']
    if not rows:raise SystemExit('No exact current quote; stop before submission')
    estimated=max(float(r['unit_price']) for r in rows)*4
    if estimated>1:raise SystemExit('Video extension quote exceeds its $1 safety cap')
    (a.output/'pricing.json').write_text(json.dumps({'checkedDate':'2026-10-13','exactRows':rows,'estimatedUSD':estimated},ensure_ascii=False,indent=2),encoding='utf-8')
    raw=a.input.read_bytes();boundary='ToAPIs'+uuid.uuid4().hex
    multipart=(f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="first-frame.png"\r\nContent-Type: image/png\r\n\r\n'.encode()+raw+f'\r\n--{boundary}--\r\n'.encode())
    upload=api('uploads/images',multipart,'multipart/form-data; boundary='+boundary);body['image']=upload['data']['url']
    record={'state':'submitting','task_id':None,'request':{**body,'image':'<uploaded-reference-url-omitted>'},'input_sha256':hashlib.sha256(raw).hexdigest(),'quoteUSD':estimated,'actualCharge':None,'checkedDate':'2026-10-13','scope':'independent helper; neither upstream app video integration nor audio validation'}
    receipt.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
    try:task=api('videos/generations',body)
    except urllib.error.HTTPError as e:
        record.update({'state':'rejected','http':e.code});receipt.write_text(json.dumps(record,indent=2),encoding='utf-8');raise SystemExit('Video request rejected: '+str(e.code))
    taskid=task.get('id');record.update({'state':'submitted','task_id':taskid});receipt.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
    if not taskid:raise SystemExit('No task ID; reconcile before a new request')
    print(json.dumps({'submitted':taskid,'quotedUSD':estimated}),flush=True)
started=time.monotonic();taskid=record['task_id']
while time.monotonic()-started<900:
    task=api('videos/generations/'+taskid);status=task.get('status')
    if status in ('failed','cancelled','canceled'):
        record['state']=status;receipt.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8');raise SystemExit('Video task failed; keep '+taskid)
    if status=='completed':
        result=task.get('result') or {};data=result.get('data') or []
        url=(data[0].get('url') if data else None) or result.get('url')
        if not url or not url.startswith('https://'):raise SystemExit('Completed but no recognized result URL; inspect '+taskid)
        with http.open(urllib.request.Request(url),timeout=60) as r:video=r.read(64*1024*1024+1)
        if len(video)>64*1024*1024 or b'ftyp' not in video[:40]:raise SystemExit('Unexpected video file')
        (a.output/'result.mp4').write_bytes(video)
        record.update({'state':'completed','elapsed_seconds':round(time.monotonic()-started,2),'sha256':hashlib.sha256(video).hexdigest(),'billing':task.get('billing')})
        receipt.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'completed':taskid,'bytes':len(video)}));break
    time.sleep(8)
else:raise SystemExit('Timed out; query '+taskid+' before submitting again')
