import json
from matplotlib import pyplot as plt


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
    x = [number_woman, number_man]
    labels = ['WOMAN', 'MAN']
    plt.pie(x, labels=labels, autopct='%1.2f%%', wedgeprops={'edgecolor': 'black'})
    plt.title('The percentage distribution people who have experienced NOPs.')
    # plt.savefig('percentage_distribution_people.png')
    plt.show()


number_nop(nopy_list)


def voivodeship_statistics(nopy_list):
    word = []
    for x in nopy_list:
        word.append(x.voivodeship)
    return word


def word_count():
    counts = dict()
    for word in voivodeship_statistics(nopy_list):
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def convert(nopy_list):
    global lst
    x = []
    for i in nopy_list:
        x.append(i.description)
        lst = ' '.join(x).split()
    return lst


def count():
    counts = dict()
    for word in convert(nopy_list):
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def description_statistics():
    temp = 0
    zaczerwienienie = 0
    drgawki = 0
    wymioty = 0
    omdlenie = 0
    for i in convert(nopy_list):
        if i == 'temp.' or i == 'temperatura' or i == 'gorączka':
            temp += 1
        elif i == 'zaczerwienienie':
            zaczerwienienie += 1
        elif i == 'drgawki':
            drgawki += 1
        elif i == 'wymioty':
            wymioty += 1
        elif i == 'omdlenie' or i == 'utrata':
            omdlenie += 1
    print(f'Fever = {temp}\nReddening = {zaczerwienienie}\nSeizures = {drgawki}'
          f'\nVomiting = {wymioty} \nSwoon = {omdlenie}')
    symptoms = ['Fever', 'Reddening', 'Seizures', 'Vomiting', 'Swoon']
    symptoms_d = [temp, zaczerwienienie, drgawki, wymioty, omdlenie]
    plt.bar(symptoms, symptoms_d)
    plt.title("Number of symptoms NOP's")
    plt.xlabel('SYMPTOMS')
    plt.ylabel('NUMBER OF CASES')
    # plt.savefig('number_of_symptoms.png')
    plt.show()


description_statistics()
