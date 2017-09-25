#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 2017年6月22日

@author: yangxiumei

'''

import json
import urllib3

data = {
        "auth": {
            "identity": {
                "methods": [ "password" ],
                "password": {
                    "user": {
                        "name": "admin",
                        "domain": {
                            "id": "default"
                            },
                        "password": "a123456."
                        }
                    }
                }
            }
        }

data1 = {
                "audit_status": False,
                "ip_src": "remote_addr",
                "log_level": "default",
                "anti_tamper_alarm": False,
                "forbidden_type": "default",
                "check_response_body": True,
                "domains": [],
                "ssl_chain_file": None,
                "ssl_private_key": None,
                "anti_virus": False,
                "name": "1",
                "admin_state_up": True,
                "tamper_recv_mail": "",
                "front_keepalive": True,
                "front_timeout": 60,
                "backend_keepalive": True,
                "backend_timeout": 60,
                "redirect_url": None,
                "check_request_body": True,
                "ssl_public_key": None,
                "domain_match": False,
                "policy_id": "497542bc-06f6-4ee5-bcb0-444efa5a41df",
                "server_info_hide":False
}

pdata1 = {
        "engine": "asg",
        "protocol": "http",
        "name": "1",
        "backend_protocol_port": 80,
        "address": "192.168.9.70",
        "bypass_if": "",
        "service_subnet_id": "",
        "backend_address": "192.168.9.54",
        "asg_id": "08b01e5f-72fb-4dab-a113-4d8de1306bdb",
        "link": "",
        "protocol_port": 80,
        "vlan_id": ""
}


http = urllib3.PoolManager()

r1 = http.request(
    'POST',
    'http://192.168.7.153:5001/v3/auth/tokens',
    body=json.dumps(data),
    headers={'Content-Type': 'application/json'}
    )

token = r1.headers['X-Subject-Token']

i = 0
while(i < 16):
    site_dict = data1
    site_dict['name'] = str(i)

    r2 = http.request(
        'POST',
        'http://192.168.7.153:1029/v1/protect_sites',
        body=json.dumps(site_dict),
        headers={'X-Auth-Token': token}
        )

    site_data = json.loads(r2.data)
    site_id = site_data['id']
    name = r2_data + 1

    p1 = http.request(
        'POST',
        'http://192.168.7.153:1029/v1/protect_sites/'+ site_id + '/members',
        body=json.dumps(pdata1),
        headers={'X-Auth-Token': token}
        )
    protect_data = json.loads(p1.data)
    name = protect_data['name'] + 1
    backend_protocol_port = protect_data['backend_protocol_port'] + 1
    protocol_port = protect_data['protocol_port'] + 1

    i = i + 1

print ('good')







