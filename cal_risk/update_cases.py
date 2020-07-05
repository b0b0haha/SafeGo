
from json import loads,dumps,dump
import json
import requests
from requests import get
from time import sleep

def get_cases():
    res = get('https://covid-dashboard-api.aminer.cn/dist/epidemic.json', verify=False)
    res_json = loads(res.text)
    data = res_json['China|Beijing']
    # data = json.loads(data)
    data = data['data'][-1]
    data = dumps(data)
    with open('cases.json', 'w') as f:
        dump(data, f)

def update_cases():
    while(1):
        get_cases()
        sleep(86400)

update_cases()