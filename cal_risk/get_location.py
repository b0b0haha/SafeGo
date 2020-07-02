import requests
import json
# from get_key import *
def get_location(address, city, key):
    # key = get_key()
    res = requests.get('https://restapi.amap.com/v3/geocode/geo?address=' + address + '&city=' + city + '&key=' + key)
    res_json = json.loads(res.text)
    # print(res_json)
    # for place in res_json['geocodes']:
    location = res_json['geocodes'][0]['location']
    lon = location[0:10]
    lat = location[-9:]
    return lon, lat