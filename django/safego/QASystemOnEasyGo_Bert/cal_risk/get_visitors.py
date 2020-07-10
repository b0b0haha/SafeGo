# import requests
# import json
# import requests
from requests import post
# import json
from json import loads, dumps
# import time
# import math


def get_TecentData(lon, lat, count, rank):
    lon = float(float(lon) * 100)
    lat = float(float(lat) * 100)
    # print(lon)
    # print(lat)
    res = 0
    url = 'https://xingyun.map.qq.com/api/getXingyunPoints'
    locs = ''
    paload = {'count': count, 'rank': rank}
    response = post(url, data=dumps(paload))
    datas = response.text
    dictdatas = loads(datas)
    time = dictdatas["time"]
    locs = dictdatas["locs"]
    locss = locs.split(",")
    for i in range(int(len(locss) / 3)):
        new_lat = locss[0 + 3 * i]  # 得到纬度
        new_lon = locss[1 + 3 * i]  # 得到经度
        new_lat = int(new_lat)
        new_lon = int(new_lon)
        count = locss[2 + 3 * i]
        if (((lat - 2) < int(new_lat) < (lat + 3)) and ((lon - 2) < int(new_lon) < (lon + 3))):
            res += int(count)

    return res
def get_visitors(lon, lat, res):
    for i in range(4):
        temp = get_TecentData(lon, lat, 4, i)
        res += temp
    return res

