#!/usr/bin/env python

from tetpyclient import RestClient
import json

scopeid=[]
api_ep="https://tetcluster.xxx.xxx"

tet_headers = {
    'Content-Type': "application/json",
    'Accept': "application/json"
}

restclient = RestClient(api_ep,
headers=tet_headers,
credentials_file='/home/xxx/cisco_tet/api_credentials.json',
verify=False)
resp = restclient.get('/app_scopes')

jdata_load = json.loads(resp.text)
#jdata_scope = json.dumps(jdata_load, sort_keys=True, indent=True)
for ep in jdata_load:
    scopeid.append(ep['id'])


#for x in scopeid:
#    print x

for id in scopeid:
    restclient = RestClient(api_ep,
    headers=tet_headers,
    credentials_file='/home/xxxx/cisco_tet/api_credentials.json',
    verify=False)
    resp = restclient.get('/app_scopes/'+str(id))

    print (resp.text)