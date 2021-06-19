import json


class NOPy:
    def __init__(self, id, date, voivodeship, region, gender, description):
        self.id = id
        self.date = date
        self.voivodeship = voivodeship
        self.region = region
        self.gender = gender
        self.description = description


nopy_list = []
with open('nopy160221.json', encoding="utf8")as file:
    data = json.load(file)

for i in data['results']:
    nopy_list.append(NOPy(str(i['ID']), str(i['DATE']), str(i['VOIVODESHIP']), str(i['REGION']),
                          str(i['GENDER']), str(i['DESCRIPTION'])))


def number_nop(nopy_list):
    number_woman, number_man, number_all = 0, 0, 0
    for i in nopy_list:
        if i.gender == 'K':
            number_woman += 1
        else:
            number_man += 1
        number_all = number_woman + number_man
    print(f'Woman = {number_woman}\nMan = {number_man}\nAll = {number_all}')

number_nop(nopy_list)

