import json
import requests
from get_visitors import *
# count = 0
# res = get_visitors('116.308264', '39.995304', 0)
#
# print(res)
res = requests.get('https://raw.githubusercontent.com/canghailan/Wuhan-2019-nCoV/master/Wuhan-2019-nCoV.json')
print(res.text)
# res = requests.get('https://restapi.amap.com/v3/geocode/geo?key=e5927609d1b678ae42bd7d6bfb9c4687&address=国科大雁栖湖校区&city=北京')
# print(res.text)
# res_json = json.loads(res.text)
# print(res_json['geocodes'][0]['location'])
# for place in res_json['geocodes']:
#     location = place['location']
#     lon = location[0:10]
#     lat = location[-9:]
#     print(lon)
# res = requests.get(
#     'https://restapi.amap.com/v3/geocode/regeo?output=xml&location=' + '116.481488' + ',' + '39.990464' + '&key=7e7d68450e6a125367922a89004f1077&extensions=all',verify=False)
# res = requests.get(
#     'https://restapi.amap.com/v3/geocode/regeo?&location=' + '116.481488' + ',' + '39.990464' + '&key=e5927609d1b678ae42bd7d6bfb9c4687&extensions=all')
# res_json = json.loads(res.text)
# print(res_json)
# district = res_json['regeocode']['addressComponent']['adcode']
#
# print(type(district))
# district = str(110105)
# res = requests.get('https://covid-dashboard-api.aminer.cn/dist/epidemic.json', verify=False)
# res_json = json.loads(res.text)
# # data = res_json['China|Beijing']
# district_key = {'110105': 'China|Beijing|Chaoyang District', '110108': 'China|Beijing|Haidian District',
#                 '110102': 'China|Beijing|Xicheng District',
#                 '110106': 'China|Beijing|Fengtai District', '110115': 'China|Beijing|Daxing District',
#                 '110114': 'China|Beijing|Changping District',
#                 '110112': 'China|Beijing|Tongzhou District', '110111': 'China|Beijing|Fangshan District',
#                 '110101': 'China|Beijing|Dongcheng District',
#                 '110116': 'China|Beijing|Huairou District', '110118': 'China|Beijing|Miyun District',
#                 '110107': 'China|Beijing|Shijingshan District',
#                 '110109': 'China|Beijing|Mentougou District', '110119': 'China|Beijing|Yanqing District',
#                 '110113': 'China|Beijing|Shunyi District'}
# # district_key = {'朝阳区':'China|Beijing|Chaoyang District', '':'China|Beijing|Haidian District', '': }
# data = res_json[district_key[district]]
# existing = data['data'][-1][0] - data['data'][-1][2] - data['data'][-1][3]
# print(existing)

