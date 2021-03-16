"""Script to calculate amount of errors in the JSON string,
as specified by "Easy Rider Bus Company" documentation.
Third stage - counting the number of stops
"""
import json
from sys import exit
import itertools

data_dict = {}

user_input = json.loads(input())

"""First we read each element of given json string, and
create dictionary items in data_dict with bus numbers as keys. 
Then we check each bus stop information, and write it down in 
corresponding part of our data_dict"""
for i in user_input:
    try:
        data_dict[i['bus_id']]
    except KeyError:
        data_dict[i['bus_id']] = {'start': '', 'stop': '', 'stops': []}
    if i['stop_type'] == 'S':
        data_dict[i['bus_id']]['start'] = i['stop_name']
    elif i['stop_type'] == 'F':
        data_dict[i['bus_id']]['stop'] = i['stop_name']
    else:
        data_dict[i['bus_id']]['stops'].append(i['stop_name'])

"""If there is not start or end stations, we exit the script"""
for k, v in data_dict.items():
    if not v['start'] or not v['stop']:
        print('There is no start or end stop for the line:', k)
        exit()

"""If start and end stations are present, we get all data ready for output"""
start_stops, finish_stops, transfer_stops = [], [], []
for i in data_dict.values():
    start_stops.append(i['start'])
    finish_stops.append(i['stop'])
    transfer_stops.append([j for j in i['stops']])
transfer_stops = [i for i in itertools.chain(*transfer_stops, start_stops, finish_stops)]
transfer_stops = set([i for i in transfer_stops if transfer_stops.count(i) > 1])

"""And then we output results"""
print('Start stops:', len(set(start_stops)), sorted(list(set(start_stops))))
print('Transfer stops:', len(transfer_stops), sorted(list(transfer_stops)))
print('Finish stops:', len(set(finish_stops)), sorted(list(set(finish_stops))))

