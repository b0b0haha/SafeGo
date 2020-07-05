<<<<<<< HEAD
import requests
import json
import time

# from get_key import *
def get_location(address, city, key):
    # key = get_key()
    res=''
    while (res==''):
        try:
            res = requests.get(
                'https://restapi.amap.com/v3/geocode/geo?address=' + address + '&city=' + city + '&key=' + key)
            break

        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue
    res_json = json.loads(res.text)
    print(res_json)
=======

from requests import get
from json import loads
# from get_key import *
def get_location(address, city, key):
    # key = get_key()
    res = get('https://restapi.amap.com/v3/geocode/geo?address=' + address + '&city=' + city + '&key=' + key)
    res_json = loads(res.text)
>>>>>>> dee77f3703c8c7188232cde577c00c6a12c4b0ca
    # for place in res_json['geocodes']:
    location = res_json['geocodes'][0]['location']
    lon = location[0:10]
    lat = location[-9:]
    return lon, lat


