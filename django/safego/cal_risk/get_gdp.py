GDP_key = {'110105': '2242.7', '110108': '5915.3', '110102': '3916.9',
           '110106': '1425.8', '110115': '2009.5', '110114': '839.3',
           '110112': '758.1', '110111': '679.5', '110101': '2242.7',
           '110116': '286.4', '110118': '278.2', '110107': '534',
           '110109': '174.5', '110119': '137.6', '110113': '1717.3',
           '110117': '233.6'}
def get_gdp(district):

    # district_key = {'110105': 'China|Beijing|Chaoyang District', '110108' :'China|Beijing|Haidian District', '110102' :'China|Beijing|Xicheng District',
    #             '110106' :'China|Beijing|Fengtai District', '110115' :'China|Beijing|Daxing District','110114' :'China|Beijing|Changping District',
    #             '110112' :'China|Beijing|Tongzhou District', '110111' :'China|Beijing|Fangshan District', '110101' :'China|Beijing|Dongcheng District',
    #             '110116' :'China|Beijing|Huairou District', '110118' :'China|Beijing|Miyun District', '110107' :'China|Beijing|Shijingshan District',
    #             '110109' :'China|Beijing|Mentougou District', '110119' :'China|Beijing|Yanqing District', '110113' :'China|Beijing|Shunyi District',
    #             '110117':''}


    if (district in GDP_key):
        GDP = float(GDP_key[district])
        return GDP
    else:
        return 0