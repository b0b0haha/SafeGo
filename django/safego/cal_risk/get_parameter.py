import requests
import json

def get_area(district):

    if (district in area_key):
        area = int(area_key[district])
        return area
    else:
        return 0

def get_case(district):
    res = requests.get('https://covid-dashboard-api.aminer.cn/dist/epidemic.json',verify=False)
    res_json = json.loads(res.text)
    # data = res_json['China|Beijing']
    district_key = {'110105': 'China|Beijing|Chaoyang District', '110108':'China|Beijing|Haidian District', '110102':'China|Beijing|Xicheng District',
                     '110106':'China|Beijing|Fengtai District', '110115':'China|Beijing|Daxing District','110114':'China|Beijing|Changping District',
                     '110112':'China|Beijing|Tongzhou District', '110111':'China|Beijing|Fangshan District', '110101':'China|Beijing|Dongcheng District',
                     '110116':'China|Beijing|Huairou District', '110118':'China|Beijing|Miyun District', '110107':'China|Beijing|Shijingshan District',
                     '110109':'China|Beijing|Mentougou District', '110119':'China|Beijing|Yanqing District', '110113':'China|Beijing|Shunyi District'}
    if (district in district_key):

    # district_key = {'朝阳区':'China|Beijing|Chaoyang District', '':'China|Beijing|Haidian District', '': }
        data = res_json[district_key[district]]
        total = data['data'][-1][0]
        cured = data['data'][-1][2]
    # dead = data['data'][-1][3]
        existing = data['data'][-1][0] - data['data'][-1][2] - data['data'][-1][3]
        return total, cured, existing
    else:
        return 0, 0, 0