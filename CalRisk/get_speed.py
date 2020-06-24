import requests
import json
from numpy import array, mean
def get_speed(lon, lat):
    res = requests.get('https://restapi.amap.com/v3/traffic/status/circle?location=' + lon + ',' + lat + '&radius=1000&key=7e7d68450e6a125367922a89004f1077&extensions=all',verify=False)
    res_json = json.loads(res.text)
    if res_json['trafficinfo']['evaluation']['status'] == 1:
        return 0 #道路畅通，车速此处没有意义，可能没有车辆通过，返回一个常量
    speed_list = []
    for road in res_json['trafficinfo']['roads']:
        speed_list.append(road['speed'])
    speed_list = array(speed_list, dtype='float64')
    avg_speed = mean(speed_list)



    
