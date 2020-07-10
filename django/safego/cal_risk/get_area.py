district_key = {'110105': 'China|Beijing|Chaoyang District', '110108': 'China|Beijing|Haidian District',
                '110102': 'China|Beijing|Xicheng District',
                '110106': 'China|Beijing|Fengtai District', '110115': 'China|Beijing|Daxing District',
                '110114': 'China|Beijing|Changping District',
                '110112': 'China|Beijing|Tongzhou District', '110111': 'China|Beijing|Fangshan District',
                '110101': 'China|Beijing|Dongcheng District',
                '110116': 'China|Beijing|Huairou District', '110118': 'China|Beijing|Miyun District',
                '110107': 'China|Beijing|Shijingshan District',
                '110109': 'China|Beijing|Mentougou District', '110119': 'China|Beijing|Yanqing District',
                '110113': 'China|Beijing|Shunyi District'}

area_key = {'110105': '455', '110108': '431', '110102': '51',
            '110106': '306', '110115': '1036', '110114': '1344',
            '110112': '906', '110111': '1990', '110101': '42',
            '110116': '2123', '110118': '2229', '110107': '84',
            '110109': '1451', '110119': '1994', '110113': '1020',
            '110117': '950'}
#单位平方千米
def get_area(district):

    if (district in area_key):
        area = int(area_key[district])
        return area
    else:
        return 0