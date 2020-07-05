import json
import requests
def get_district(lon, lat, key):
    res = requests.get(
        'https://restapi.amap.com/v3/geocode/regeo?&location=' + lon + ',' + lat + '&key='+ key +  '&extensions=all')
    res_json = json.loads(res.text)
    district = res_json['regeocode']['addressComponent']['adcode']
    return district
