

def get_population(district):
    population_key = {'110105': '347.3', '110108' :'323.7', '110102' :'117.9',
                '110106' :'202.5', '110115' :'188.8' ,'110114' :'216.6',
                '110112' :'157.8', '110111' :'125.5', '110101' :'82.2',
                '110116' :'42.2', '110118' :'50.3', '110107' :'57.2',
                '110109' :'34.4', '110119' :'35.7', '110113' :'122.8',
                '110117':'45.6'}
    if (district in population_key):
        population = population_key[district]
        population = float(population)
        return population
    else:
        return '0'

# district_key = {'110105': 'China|Beijing|Chaoyang District', '110108' :'China|Beijing|Haidian District', '110102' :'China|Beijing|Xicheng District',
#                 '110106' :'China|Beijing|Fengtai District', '110115' :'China|Beijing|Daxing District','110114' :'China|Beijing|Changping District',
#                 '110112' :'China|Beijing|Tongzhou District', '110111' :'China|Beijing|Fangshan District', '110101' :'China|Beijing|Dongcheng District',
#                 '110116' :'China|Beijing|Huairou District', '110118' :'China|Beijing|Miyun District', '110107' :'China|Beijing|Shijingshan District',
#                 '110109' :'China|Beijing|Mentougou District', '110119' :'China|Beijing|Yanqing District', '110113' :'China|Beijing|Shunyi District'}


