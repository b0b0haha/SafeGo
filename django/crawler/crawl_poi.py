# coding=utf-8
from urllib.parse import quote
from urllib import request
import json
import os
import xlwt
import pandas as pd

# TODO 1.替换为从高德开放平台上申请申请的密钥
amap_web_key = ''

# TODO 2.分类关键字,最好对照<<高德地图POI分类关键字以及编码.xlsx>>来填写对应编码，多个用逗号隔开
keyword = ['050000','060000','070000','090000','100000','110000','150000','170000']

# TODO 3.城市，多个用逗号隔开
city = ['110100']


poi_search_url = "http://restapi.amap.com/v3/place/text"
poi_boundary_url = "https://ditu.amap.com/detail/get/detail"

poi_xingzheng_distrinct_url = "https://restapi.amap.com/v3/config/district?subdistrict=1&key=7e7d68450e6a125367922a89004f1077"


# 根据城市名称和分类关键字获取poi数据
def getpois(cityname, keywords):
    i = 1
    poilist = []
    while True:  
        result = getpoi_page(cityname, keywords, i)
        print(result)
        result = json.loads(result)  
        if result['count'] == '0':
            break

        hand(poilist, result)
        i = i + 1
    return poilist



# 数据写入csv文件中
def write_to_csv(poilist, cityname, classfield):
    data_csv = {}
    lons, lats, names, addresss, pnames, citynames, business_areas, types, tels = [], [], [], [], [], [], [], [], []

    for i in range(len(poilist)):
        print('===================')
        print(poilist[i])
        tel = poilist[i].get('tel')
        location = poilist[i].get('location')
        name = poilist[i].get('name')
        address = poilist[i].get('address')
        pname = poilist[i].get('pname')
        cityname = poilist[i].get('cityname')
        business_area = poilist[i].get('business_area')
        type = poilist[i].get('type')
        lng = str(location).split(",")[0]
        lat = str(location).split(",")[1]

        lons.append(lng)
        lats.append(lat)
        names.append(name)
        addresss.append(address)
        pnames.append(pname)
        citynames.append(cityname)
        tels.append(tel)
        if business_area == []:
            business_area = ''
        business_areas.append(business_area)
        types.append(type)
    data_csv['lon'], data_csv['lat'], data_csv['name'], data_csv['address'], data_csv['pname'], \
    data_csv['cityname'], data_csv['business_area'], data_csv['type'], data_csv['tel'] = \
        lons, lats, names, addresss, pnames, citynames, business_areas, types, tels

    df = pd.DataFrame(data_csv)

    folder_name = 'poi-' + cityname + "-" + classfield
    folder_name_full = 'data' + os.sep + folder_name + os.sep
    if os.path.exists(folder_name_full) is False:
        os.makedirs(folder_name_full)

    file_name = 'poi-' + cityname + "-" + classfield + ".csv"
    file_path = folder_name_full + file_name

    df.to_csv(file_path, index=False, encoding='utf_8_sig')
    return folder_name_full, file_name


# 将返回的poi数据装入集合返回
def hand(poilist, result):
    # result = json.loads(result)  # 将字符串转换为json
    pois = result['pois']
    for i in range(len(pois)):
        poilist.append(pois[i])


# 单页获取pois
def getpoi_page(cityname, keywords, page):
    req_url = poi_search_url + "?key=" + amap_web_key + '&extensions=all&types=' + quote(
        keywords) + '&city=' + quote(cityname) + '&citylimit=true' + '&offset=25' + '&page=' + str(
        page) + '&output=json'
    data = ''
    with request.urlopen(req_url) as f:
        data = f.read()
        data = data.decode('utf-8')
    return data


def get_areas(code):
    '''
    获取城市的所有区域
    :param code:
    :return:
    '''

    print('获取城市的所有区域：code: ' + str(code).strip())
    data = get_distrinctNoCache(code)

    print('get_distrinct result:' + data)

    data = json.loads(data)

    districts = data['districts'][0]['districts']
    # 判断是否是直辖市
    # 北京市、上海市、天津市、重庆市。
    if (code.startswith('重庆') or code.startswith('上海') or code.startswith('北京') or code.startswith('天津')):
        districts = data['districts'][0]['districts'][0]['districts']

    i = 0
    area = ""
    for district in districts:
        name = district['name']
        adcode = district['adcode']
        i = i + 1
        area = area + "," + adcode

    print(area)
    print(str(area).strip(','))
    return str(area).strip(',')


def get_data(city, keyword):
    '''
    根据城市名以及POI类型爬取数据
    :param city:
    :param keyword:
    :return:
    '''
    isNeedAreas = True
    if isNeedAreas:
        area = get_areas(city)
    all_pois = []
    if area != None and area != "":
        area_list = str(area).split(",")
        if area_list == 0:
            area_list = str(area).split("，")

        for area in area_list:
            pois_area = getpois(area, keyword)
            print('当前城区：' + str(area) + ', 分类：' + str(keyword) + ", 总的有" + str(len(pois_area)) + "条数据")
            all_pois.extend(pois_area)
        print("所有城区的数据汇总，总数为：" + str(len(all_pois)))
    
        # 写入CSV
        file_folder, file_name = write_to_csv(all_pois, city, keyword)
        
        return
        
    else:
        pois_area = getpois(city, keyword)
    
        # 写入CSV
        file_folder, file_name = write_to_csv(all_pois, city, keyword)
        
        return
    

    return None


def get_distrinctNoCache(code):
    '''
    获取中国城市行政区划
    :return:
    '''

    url = "https://restapi.amap.com/v3/config/district?subdistrict=2&extensions=all&key=7e7d68450e6a125367922a89004f1077"

    req_url = url + "&keywords=" + quote(code)

    print(req_url)

    with request.urlopen(req_url) as f:
        data = f.read()
        data = data.decode('utf-8')
    print(code, data)
    return data


if __name__ == '__main__':

    for ct in city:
        for type in keyword:
            get_data(ct, type)
    print('总的', len(city), '个城市, ', len(keyword), '个分类数据全部爬取完成!')

