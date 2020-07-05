
# from cal_risk.get_speed import *
# from cal_risk.load_cases import *
# from cal_risk.get_district import *
# from cal_risk.get_visitors import *
# from cal_risk.get_key import *
# from cal_risk.get_location import *
# from cal_risk.get_population import *
# from cal_risk.get_area import *
# from cal_risk.get_gdp import *


from get_speed import *
from load_cases import *
from get_district import *
from get_visitors import *
from get_key import *
from get_location import *
from get_population import *
from get_area import *
from get_gdp import *

import pandas as pd
#risk = 0, 1, 2分别表示低，中，高风险
def cal_risk_from_name(name, city):
    # key = get_key()
    lon, lat = get_location(name, city)
    if(lon == '0' and lat == '0'):
        print('查不到')
        return 3
    # print(lon)
    # print(lat)
    district = get_district(lon, lat)
    # print(district)
    population = get_population(district)
    if (population == '0'):
        print('不在范围内')
        return 3
    # print(population)
    gdp = get_gdp(district)
    # print(gdp)
    area = get_area(district)
    # print(area)
    total, cured, existing = load_cases()
    # print(existing)
    avg_speed = get_speed(lon, lat)
    if (avg_speed == 0):
        print('查不到')
        return 3
    # print('speed')
    # print(avg_speed)
    visitors = get_visitors(lon, lat, 0)
    # temp = [visitors]
    # visitors = pd.DataFrame(temp)
    # visitors.dropna()
    # visitors.columns = ['count']
    # visitors.to_csv('TecentData.csv', mode='a', index=False)
    # print(visitors)
    if (area != 0):
        fragility = population * (gdp / 10000) / area #易感人群脆弱性
    if (total != 0):
        validity = cured / total#  治愈数很难精确到区级，只能算北京市的，但是同城对比没有意义
        # print(cured)
    risk = (fragility / validity) * visitors / (avg_speed)
    if (risk<= 5):
        return 0
    elif (risk > 5 and risk <= 10):
        return 1
    elif (risk > 10):
        return 2       #0 1 2分别表示低，中，搞风险
    else:
        return 3  #表示查不到地点
    # print(risk)
    # risk = #还要改
    # return risk    #还要改

# while(1):
#     # visitors = get_visitors(lon, lat, 0)
risk = cal_risk_from_name('谷歌北京', '北京')
print(risk)

