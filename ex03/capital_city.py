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
state_key = sys.argv[1]
if (not (state_key in states)):
    print('Unknown state')
    exit()
capital_key = states[state_key]
print(capital_cities[capital_key])
