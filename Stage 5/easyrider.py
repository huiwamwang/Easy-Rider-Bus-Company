"""Script to calculate amount of errors in the JSON string,
as specified by "Easy Rider Bus Company" documentation.
Fourth stage - checking arrival times
"""
import json

time_test = {}

user_input = json.loads(input())

"""Create empty values, so later we can compare time stamps"""
bus_id = 0
stop_name = ''
a_time = ''

"""Iterating through the json. If bus_id variable is empty, we put
current 'bus_id' value from the json. If it's not, we check the arrival time.
If time is okay, we save new time, and continue to next element of json.
If time is wrong, we save data to the 'time_test' dictionary, with bus_id
as a key, and stop_name as value"""
for i in user_input:
    if i['bus_id'] == bus_id:
        if i['a_time'] > a_time:
            stop_name = i['stop_name']
            a_time = i['a_time']
            continue
        else:
            if bus_id in time_test:
                continue
            else:
                time_test[i['bus_id']] = i['stop_name']
    else:
        bus_id = i['bus_id']
        stop_name = i['stop_name']
        a_time = i['a_time']

"""Printing output. If 'time_test' dictionary is empty, we print OK,
and if not, we print where we have problems with arrival times."""
print("Arrival time test:")
if not time_test:
    print('OK')
else:
    for k, v in time_test.items():
        print(f"bus_id line {k}: wrong time on station {v}")
