
from cal_risk.get_speed import *
from cal_risk.get_cases import *
from cal_risk.get_district import *
from cal_risk.get_visitors import *
from cal_risk.get_key import *
from cal_risk.get_location import *
from cal_risk.get_population import *
from cal_risk.get_area import *
from cal_risk.get_gdp import *

'''
from get_speed import *
from get_cases import *
from get_district import *
from get_visitors import *
from get_key import *
from get_location import *
from get_population import *
from get_area import *
from get_gdp import *
'''
import pandas as pd
#risk = 0, 1, 2分别表示低，中，高风险
def cal_risk_from_name(name, city):
    key = get_key()
    lon, lat = get_location(name, city, key)
    # print(lon)
    # print(lat)
    district = get_district(lon, lat, key)
    # print(district)
    population = get_population(district)
    # print(population)
    gdp = get_gdp(district)
    # print(gdp)
    area = get_area(district)
    # print(area)
    total, cured, existing = get_cases()
    # print(existing)
    avg_speed = get_speed(lon, lat, key)
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
    else:
        return 2       #0 1 2分别表示低，中，搞风险
    # print(risk)
    # risk = #还要改
    # return risk    #还要改

# while(1):
#     # visitors = get_visitors(lon, lat, 0)
risk = cal_risk_from_name('中国科学院大学', '北京')
print(risk)

