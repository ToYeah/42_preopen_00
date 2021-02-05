import sys

states = {
    "Oregon": "OR",
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado": "CO"
}
capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

swap_states = {v: k for k, v in states.items()}
swap_capitals = {v: k for k, v in capital_cities.items()}

if (len(sys.argv) != 2):
    exit()
argv_list = sys.argv[1].split(',')
for i in argv_list:
    key = i.strip().title()
    if (key == ""):
        continue
    if (key in states):
        print(f'{capital_cities[states[key]]} is the capital of New Jersey')
    elif (key in swap_capitals):
        print(f'{swap_states[swap_capitals[key]]} is the capital of Oregon')
    else:
        print(f'{key} is neither a capital city nor a state')
