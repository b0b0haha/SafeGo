
from requests import get
from json import loads
from numpy import array, mean
from get_key import *
def get_speed(lon, lat):
    key = get_key()
    res = get('https://restapi.amap.com/v3/traffic/status/circle?location=' + lon + ',' + lat  +'&radius=1000&key=' + key + '&extensions=all',verify=False)
    res_json = loads(res.text)
    # print(res_json)
    if(len(res_json['trafficinfo']['roads']) == 0):
        return 60#没有数据默认和交通畅通一样处理
    if res_json['trafficinfo']['evaluation']['status'] == 0 or res_json['trafficinfo']['evaluation']['status'] == 1:
        return 60 #道路畅通，车速此处没有意义，可能没有车辆通过，返回一个常量
    speed_list = []
    # if ('speed' in res_json)

    for road in res_json['trafficinfo']['roads']:
        if ('speed' in road):
            speed_list.append(road['speed'])
        else:
            return 0
    speed_list = array(speed_list, dtype='float64')
    avg_speed = mean(speed_list)
    return avg_speed



    
