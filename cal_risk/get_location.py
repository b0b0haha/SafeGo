
from requests import get
from json import loads
from get_key import *
def get_location(name, city):
    key = get_key()
    res = get('https://restapi.amap.com/v3/geocode/geo?address=' + name + '&city=' + city + '&key=' + key)
    res_json = loads(res.text)

    # print(type(res_json['geocodes']))
    # for place in res_json['geocodes']:
    if(len(res_json['geocodes']) == 0):
        return '0', '0'   #说明查不到
    location = res_json['geocodes'][0]['location']
    lon = location[0:10]
    lat = location[-9:]
    return lon, lat