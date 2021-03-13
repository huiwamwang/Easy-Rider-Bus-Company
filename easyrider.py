"""Script to calculate amount of errors in the JSON string,
as specified by "Easy Rider Bus Company" documentation.
Third stage - counting the number of stops
"""
import json

stops_dictionary = {128: 0, 256: 0, 512: 0, 1024:0}

user_input = json.loads(input())

for i in user_input:
    for k in stops_dictionary.keys():
        if i['bus_id'] == k:
            stops_dictionary[k] += 1

print("Line names and number of stops:")
for k, v in stops_dictionary.items():
    print(f'bus_id: {k}, stops: {v}')
