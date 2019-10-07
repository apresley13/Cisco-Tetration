#!/usr/bin/env python
### use Tetration API to search flows
from tetpyclient import RestClient
import json
import csv

flows={}
api_ep="https://tetcluster.xxx.xxx"

tet_headers = {
    'Content-Type': "application/json",
    'Accept': "application/json"
}

jdata_fsearch = {"t0":"2019-10-01T00:00:00-0600","t1":"2019-10-01T17:13:00-0600","filter":{ "filters":[{"type":"subnet","field":"src_addr","value":"xxx.xxx.xxx.x/xx"},{"type":"in","field":"dst_port","values":["80","443"]}]},"scopeName":"Default:test:test:test:test","limit":1000}
jdata_fsearch_out = json.dumps(jdata_fsearch, indent=True)
payloadone = jdata_fsearch_out
#print(payloadone)
restclient = RestClient(api_ep,
headers=tet_headers,
credentials_file='/home/xxxx/cisco_tet/api_credentials.json',
verify=False)
resp = restclient.post('/flowsearch',
json_body=payloadone)
jdata_load = json.loads(resp.text)
#jdata_flows_out = json.dumps(jdata_load, sort_keys=True, indent=True)
#print(jdata_flows_out)
for flow in jdata_load['results']:
    print 'src address:',flow['src_address'], 'dst address:',flow['dst_address'],'Protocol:', flow['proto'], 'dst_port:', flow['dst_port']
