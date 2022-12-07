import json

gugus_dict = {}
current_min = 99

with open('./input.txt', 'r') as gugus_lists:
    for gugus_raw_data in gugus_lists:
        [name, path] = gugus_raw_data.replace('\n', '').split(' - ')

        if len(path) < current_min:
            current_min = len(path)
            gugus_dict = {}
            gugus_dict[name] = path
        elif len(path) == current_min:
            gugus_dict[name] = path


print(json.dumps(gugus_dict, indent = 2))

iteration = 0
previous_length = len(gugus_dict)
current_length = 0

print("Initial : {}".format(len(gugus_dict)))

while(len(gugus_dict) > 1 and previous_length != current_length):

    previous_length = len(gugus_dict)
    new_dict = {}
    for gugus in gugus_dict:
        if gugus_dict[gugus][iteration] == 'L':
            new_dict[gugus] = gugus_dict[gugus]
    iteration += 1

    gugus_dict = new_dict
    current_length = len(new_dict)
    print("Iteration = {} / Restants : {}".format(iteration, len(new_dict)))

print(gugus_dict)
