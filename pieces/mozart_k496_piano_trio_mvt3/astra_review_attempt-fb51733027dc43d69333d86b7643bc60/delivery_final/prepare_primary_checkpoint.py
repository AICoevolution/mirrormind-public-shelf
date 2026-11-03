from pathlib import Path
from lxml import etree as E
from collections import defaultdict
import json,hashlib,os,shutil
R=Path(__file__).resolve().parent.parent;D=R/'delivery_final';h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
checks=json.load(open(D/'correction_application_verification.json'));assert checks['passed'];app=json.load(open(D/'topology_application_checks.json'));assert not app['overlaps_requiring_resolution'];working=D/'UNVERIFIED_topology_partial.musicxml';assert h(working)==checks['working_xml_sha256']==app['working_xml_sha256']
primary=D/'UNVERIFIED_mozart_k496_mvt3.musicxml';shutil.copyfile(working,primary);sha=h(primary)
cs=json.load(open(R/'reviewer/phase3_review.json'))['correction_targets'];batches=[json.load(open(D/f'correction_batch_{i:02}.json')) for i in range(1,4)];applied=defaultdict(list)
for i,b in enumerate(batches,1):
 for a in b['applied']:applied[a['index']].append({'batch':f'delivery_final/correction_batch_{i:02}.json','record':a})
assert set(applied)==set(range(len(cs)))
ns={n.get('id'):n for n in E.parse(str(primary)).findall('.//note')}
ledger=[]
for i,c in enumerate(cs):
 ledger.append({'index':i,**c,'application_records':applied[i],'final_target_xml':{t:E.tostring(ns[t],encoding='unicode') if t in ns else None for t in c['targets']},'status':'APPLIED_SUPPORTED_CORRECTION' if c['status']=='SUPPORTED_BY_PRINT' else 'APPLIED_PROVISIONAL_READING'})
save(D/'correction_ledger.json',{'schema':'astra_correction_ledger.v1','primary_xml_sha256':sha,'source_candidate_sha256':json.load(open(R/'reviewer/phase3_review.json'))['candidate_sha256'],'audit_sha256':h(R/'reviewer/phase3_review.json'),'correction_targets':ledger,'topology_and_application_fixes':json.load(open(D/'correction_batch_04.json')),'frozen_errata':{'delivery_final/ERRATUM_001.json':h(D/'ERRATUM_001.json')},'pending_correction_targets':[],'application_verification':'delivery_final/correction_application_verification.json','notation':'UNVERIFIED; application consistency is not Phase5 readiness or publication approval'})
lanes=defaultdict(list)
for t,v in app['timeline'].items():lanes[(v['part'],v['voice'])].append(t)
save(D/'voice_topology.json',{'schema':'astra_voice_topology.v1','primary_xml_sha256':sha,'pre_census':app['pre_census'],'post_census':app['post_census'],'continuous_lines':{'P1/1':'Single violin line','P2/1':'Single cello line','P3/1':'Piano principal upper line, crossing to lower staff at P061','P3/2':'Independent piano upper inner/held line where printed','P3/5':'Piano lower accompaniment line','P3/6':'Independent lower inner line where printed'},'final_sep_lanes':[{'part':k[0],'voice':k[1],'note_ids':v} for k,v in lanes.items()],'context_scoped_relabels':'delivery_final/correction_batch_04.json','frozen_voice_plans':'delivery_final/correction_ledger.json','retained_extra_voices':[{'part':k[0],'voice':k[1],'note_ids':v,'reason':'Independently sounding held/inner printed line overlaps the principal line; rests were not fabricated for unprinted silence.'} for k,v in lanes.items() if k==('P3','2') or k==('P3','6')],'removed_empty_lanes':'Spurious authored-as-rest lanes removed only by exact frozen delete targets; see correction ledger. Nonprinting alignment uses forward/backup.','cross_staff_line':{'voice':'P3/1','bar':61,'evidence':'reviewer/inspection_system_13.json'},'human_outcome':None,'stage5_export_confirmation':False})
freeze={'schema':'astra_final_freeze.v2','review_protocol':'print_first_candidate_audit.v1','stage4_complete':True,'stage5_complete':False,'delivery_ready':False,'status':'UNVERIFIED','primary_xml':str(primary.relative_to(R)),'primary_xml_sha256':sha,'phase3_frozen':True,'metadata_contract':'reviewed_namecard.v1','correction_ledger':'delivery_final/correction_ledger.json','voice_topology':'delivery_final/voice_topology.json','human_readiness':{},'layer_readiness':{}}
save(R/'FINAL_FREEZE.json',freeze)
p=json.load(open('/output/worker-progress.json'))
for uid,files in [('corrections:batch-04-topology',['correction_batch_04.json','topology_application_checks.json','ERRATUM_001.json']),('corrections:application-verification',['correction_application_verification.json'])]:p['units'].append({'id':uid,'status':'COMPLETE','evidence':{'delivery_final/'+f:h(D/f) for f in files}})
for u in p['units']:
 if u['id']=='corrections:primary':u.update(status='COMPLETE',evidence={str(f.relative_to(R)):h(f) for f in [primary,D/'correction_ledger.json',D/'voice_topology.json',R/'FINAL_FREEZE.json']})
p.update(state='PHASE_COMPLETE',remaining_work=['Obtain validated primary host release','Run ALL Phase5 structural, layer export/rebuild/Apply, playback/route, production viewer, metadata checks','Visually recheck every changed context and connected span in required layouts; bind attention and final delivery manifests'],next_action='Run worker_protocol primary without shortened timeout; continue only after validated host release',blocker=None)
save('/output/worker-progress.json.tmp',p);os.replace('/output/worker-progress.json.tmp','/output/worker-progress.json');print(sha)
