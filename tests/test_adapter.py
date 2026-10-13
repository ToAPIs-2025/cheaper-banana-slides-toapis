import unittest,tempfile,types,sys,importlib.util,json,io,os
from pathlib import Path
from PIL import Image
import argparse
parser=argparse.ArgumentParser();parser.add_argument('--upstream',type=Path,required=True);args,remaining=parser.parse_known_args();sys.argv=[sys.argv[0]]+remaining
image_root=args.upstream.resolve()/'backend/services/ai_providers/image'
pkg=types.ModuleType('banana_image');pkg.__path__=[str(image_root)];sys.modules['banana_image']=pkg
spec=importlib.util.spec_from_file_location('banana_image.toapis_image_provider',image_root/'toapis_image_provider.py');m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
b=io.BytesIO();Image.new('RGB',(8,8),'blue').save(b,format='PNG');raw=b.getvalue()
class Response:
    headers={'content-type':'image/png'}
    def __enter__(self):return self
    def __exit__(self,*a):pass
    def read(self,*a):return raw
class AssetHTTP:
    def open(self,req,timeout):
        assert not req.has_header('Authorization')
        return Response()
class AdapterTests(unittest.TestCase):
    def provider(self,d):return m.ToAPIsImageProvider('fixture-key','https://toapis.cn/v1','gpt-image-2-vip','low',d)
    def test_submit_once_and_resume_completed_receipt(self):
        with tempfile.TemporaryDirectory() as d:
            p=self.provider(d);p.http=AssetHTTP();calls=[]
            def get(path,body=None,content_type=None):
                calls.append((path,body))
                return {'id':'fixture_task'} if body is not None else {'status':'completed','result':{'data':[{'url':'https://assets.example/out.png'}]}}
            p._json=get
            self.assertEqual(p.generate_image('test').size,(8,8));self.assertEqual(p.generate_image('test').size,(8,8))
            posts=[c for c in calls if c[1] is not None];self.assertEqual(len(posts),1)
            self.assertEqual(posts[0][1]['quality'],'low');self.assertEqual(posts[0][1]['size'],'16:9');self.assertEqual(posts[0][1]['n'],1)
    def test_lost_submission_blocks_new_post(self):
        with tempfile.TemporaryDirectory() as d:
            p=self.provider(d);calls=[]
            def fail(*args):calls.append(args);raise TimeoutError()
            p._json=fail
            with self.assertRaisesRegex(RuntimeError,'Submission response'):p.generate_image('unknown')
            with self.assertRaisesRegex(RuntimeError,'prior POST'):p.generate_image('unknown')
            self.assertEqual(len(calls),1)
    def test_failed_task_retains_id_and_does_not_resubmit(self):
        with tempfile.TemporaryDirectory() as d:
            p=self.provider(d);calls=[]
            def get(path,body=None,content_type=None):
                calls.append((path,body));return {'id':'failed_task'} if body is not None else {'status':'failed'}
            p._json=get
            for _ in range(2):
                with self.assertRaisesRegex(RuntimeError,'failed_task'):p.generate_image('failure')
            self.assertEqual(sum(body is not None for _,body in calls),1)
    def test_reference_url_upload_and_standard_omits_quality(self):
        with tempfile.TemporaryDirectory() as d:
            p=m.ToAPIsImageProvider('fixture','https://toapis.cn','gpt-image-2','low',d);p.http=AssetHTTP();calls=[]
            def get(path,body=None,content_type=None):
                calls.append((path,body,content_type))
                if path=='uploads/images':return {'data':{'url':'https://assets.example/reference.png'}}
                return {'id':'with_ref'} if body is not None else {'status':'completed','result':{'data':[{'url':'https://assets.example/out.png'}]}}
            p._json=get;p.generate_image('reference',[Image.new('RGBA',(8,8),(0,0,255,255))])
            self.assertIn(b'filename="reference.png"',calls[0][1]);body=calls[1][1]
            self.assertEqual(body['reference_images'],['https://assets.example/reference.png']);self.assertNotIn('quality',body)
    def test_wrong_host_model_and_resolution_fail_early(self):
        for url in ['https://evil.example','http://toapis.cn','https://toapis.cn/v1/v1','https://toapis.cn:8443','https://u:p@toapis.cn']:
            self.assertFalse(m.is_toapis(url))
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):m.ToAPIsImageProvider('fixture','https://toapis.cn','other-model','low',d)
            with self.assertRaises(ValueError):self.provider(d).generate_image('x',resolution='16K')
if __name__=='__main__':unittest.main()
