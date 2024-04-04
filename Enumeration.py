

# Create a dictionary with state-capital key-value pairs
state_capital_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne',
}

# Enumerate the contents of state-capital key-values
print("Enumerating the contents of state-capital key-values:")
for state, capital in state_capital_dict.items():
    print(f"{state}: {capital}")

# List all states
print("\nList of all states:")
states_list = list(state_capital_dict.keys())
print(states_list)

# List all capitals
print("\nList of all capitals:")
capitals_list = list(state_capital_dict.values())
print(capitals_list)

# Replace the capital of a specific state
new_capital = 'New Capital'
state_to_replace = 'California'
if state_to_replace in state_capital_dict:
    state_capital_dict[state_to_replace] = new_capital
    print("\nUpdated dictionary:")
    for state, capital in state_capital_dict.items():
        print(f"{state}: {capital}")
else:
    print(f"\nState '{state_to_replace}' not found in the dictionary.")