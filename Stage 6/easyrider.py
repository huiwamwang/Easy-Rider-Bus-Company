"""Script to calculate amount of errors in the JSON string,
as specified by "Easy Rider Bus Company" documentation.
Fifth stage - checking on demand stops
"""
import json

start_end = ['Pilotow Street', 'Bourbon Street', 'Sesame Street', 'Elm Street', 'Sunset Boulevard']
on_demand = []

user_input = json.loads(input())

for i in user_input:
    if i['stop_type'] == "S" or i['stop_type'] == "F":
        start_end.append(i['stop_name'])
    elif i['stop_type'] == 'O':
        on_demand.append(i['stop_name'])

print('On demand stops test:')
if not set(start_end).intersection(set(on_demand)):
    print('OK')
else:
    print("Wrong stop type:", sorted([i for i in on_demand if i in start_end]))
