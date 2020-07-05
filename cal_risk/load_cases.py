from json import loads, load
def load_cases():
    with open('cases.json', encoding='UTF-8') as f_risk:
        data = load(f_risk)
    data = loads(data)


    total = data[0]
    cured = data[2]
    dead = data[3]

    existing = total - cured - cured
    return total, cured, existing