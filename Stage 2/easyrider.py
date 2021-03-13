"""Script to calculate amount of errors in the JSON string,
as specified by "Easy Rider Bus Company" documentation.
Second stage - regexp mistakes calculations
"""
import json
import re

all_info_together_dictionary = {'bus_id': ['int', 'required', 0, ],
                                'stop_id': ['int', 'required', 0],
                                'stop_name': ['str', 'required', 0,
                                              r'[A-Z][a-z]{1,}(\s[A-Z][a-z]{1,})?\s(?:Road|Avenue|Boulevard|Street)$'],
                                'next_stop': ['int', 'required', 0],
                                'stop_type': ['str', 'N_R', 0, r'[SOF]?$'],
                                'a_time': ['str', 'required', 0, r'[012][\d]\:[0-5][\d]$']}

user_input = json.loads(input())

for i in user_input:
    for k, v in all_info_together_dictionary.items():
        if v[0] == 'str':
            if not re.match(v[3], i[k]):
                all_info_together_dictionary[k][2] += 1

print(f"Format validation: {sum([i[2] for i in all_info_together_dictionary.values()])}")
for k, v in all_info_together_dictionary.items():
    if v[0] == 'str':
        print(f"{k}: {v[2]}")
