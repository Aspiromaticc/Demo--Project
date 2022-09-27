states = {
'New York': 'NY',
'Los Angeles': 'LA',
'California': 'CA',
'Chicago': 'CH'
}
cities = {'NY': 'Apomu', 'LA': 'Ikire', 'CA': 'Ife', 'CH': 'Osogbo'}
print(states['New York'])
for state, abbev in list(states.items()):
    print(f"{state} is abbreviated as {abbev}")
for city, abbrev in list(states.items()):
    print(f"{city} has {abbrev}")
center = states.get("New York")
print(center)
