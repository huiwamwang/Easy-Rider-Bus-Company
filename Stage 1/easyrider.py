import json

all_info_together_dictionary = {'bus_id': ['int', 'required', 0],
                                'stop_id': ['int', 'required', 0],
                                'stop_name': ['str', 'required', 0],
                                'next_stop': ['int', 'required', 0],
                                'stop_type': ['str', 'N_R', 0],
                                'a_time': ['str', 'required', 0]}

user_input = json.loads(input())

for i in user_input:
    for k, v in all_info_together_dictionary.items():
        j = str(type(i[k]))
        if v[0] not in j or (len(str(i[k])) == 0 and v[1] == 'required') or (len(str(i[k])) == 2 and v[1] == 'N_R'):
            all_info_together_dictionary[k][2] += 1

print(f"Type and required field validation: {sum([i[2] for i in all_info_together_dictionary.values()])}")
for k, v in all_info_together_dictionary.items():
    print(f"{k}: {v[2]}")
