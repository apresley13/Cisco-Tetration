#!/usr/bin/env python
#### CSV input of scope Subnet, scope name, and parent scope ID. add to tetration.
from tetpyclient import RestClient
import json
import csv

api_ep="https://tetcluster.xxx.xxx"

tet_headers = {
    'Content-Type': "application/json",
    'Accept': "application/json"
}


with open('tet-scopecsvpython.csv') as csvfile:
    read = csv.DictReader(csvfile)
    for row in read:
        #print(row['field'], row['parent_app_scope_id'], row['short_name'])

        jdata_scope = { "short_name": str(row['short_name']) , "short_query": { "field": "ip", "type": "subnet", "value": str(row['field']) }, "parent_app_scope_id": str(row['parent_app_scope_id']) }
        jdata_scope_out = json.dumps(jdata_scope, indent=True)
        payloadone = jdata_scope_out
#        print(payloadone)
        restclient = RestClient(api_ep,
        headers=tet_headers,
        credentials_file='/home/xxxx/cisco_tet/api_credentials.json',
        verify=False)
        resp = restclient.post('/app_scopes',
        json_body=payloadone)
        print(resp.text)
        
