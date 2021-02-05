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

if (len(sys.argv) != 2):
    exit()
capital_key = sys.argv[1]
swap_states = {v: k for k, v in states.items()}
swap_capitals = {v: k for k, v in capital_cities.items()}
if (not (capital_key in swap_capitals)):
    print('Unknown capital city')
    exit()
state_key = swap_capitals[capital_key]
print(swap_states[state_key])
