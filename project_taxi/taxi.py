import datetime
import json


class Taxi:
    def __init__(self, registration_plate, taxi_number, license_number, license_date):
        self.registration_plate = registration_plate
        self.taxi_number = taxi_number
        self.license_number = license_number
        self.license_date = license_date


def license_after_2070(taxi_list):
    list_license = []
    for i in taxi_list:
        if i.license_date.year >= 2071:
            list_license.append(i.license_number)
    return list_license


def registration_gwe(taxi_list):
    number = 0
    for i in taxi_list:
        if i.registration_plate[0:3] == 'GWE':
            number += 1
    return number


def license_2020(taxi_list):
    number = 0
    for i in taxi_list:
        if i.license_number.split('/', 1)[1] == '2020':
            number += 1
    return number


taxi_list = []

file = open('list_taxi.json')
data = json.load(file)

for i in data['results']:
    taxi_list.append(Taxi(str(i['numerRejestracyjny']), int(i['numerBoczny']), str(i['numerLicencji']),
                          datetime.datetime.strptime(i['dataLicencji'], '%d.%m.%Y')))

print('List of license numbers which will be valid after 2070: ')
list_license = license_after_2070(taxi_list)
for i in list_license:
    print(i)

print('Taxis from Wejcherowo: ', registration_gwe(taxi_list))

print('Total number of licenses issued in 2020: ', license_2020(taxi_list))
