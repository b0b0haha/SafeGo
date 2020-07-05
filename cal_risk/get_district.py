
from json import loads
import requests
from requests import get
from get_key import *
def get_district(lon, lat):
    key = get_key()
    res = get(
        'https://restapi.amap.com/v3/geocode/regeo?&location=' + lon + ',' + lat + '&key='+ key +  '&extensions=all')
    res_json = loads(res.text)
    district = res_json['regeocode']['addressComponent']['adcode']
    return district
