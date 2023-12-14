# Original code provided by the user with modifications to handle truncated lists

Officers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Units = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Preferences
Off_Pref = {
    'a': ['B', 'I', 'E', 'C', 'D', 'F', 'A', 'G', 'H', 'J'],
    'b': ['B', 'D', 'H', 'F', 'G', 'C', 'J', 'A', 'I', 'E'],
    'c': ['D', 'E', 'C', 'B', 'H', 'F', 'I', 'A', 'J', 'G'],
    'd': ['E', 'I', 'D', 'B', 'G', 'A', 'F', 'C', 'J', 'H'],
    'e': ['C', 'B', 'E', 'F', 'G', 'H', 'J', 'A', 'D', 'I'],
    'f': ['A', 'J', 'C', 'E', 'B', 'H', 'I', 'D', 'G', 'F'],
    'g': ['I', 'F', 'G', 'D', 'H', 'A', 'C', 'E', 'B', 'J'],
    'h': ['H', 'A', 'F', 'B', 'J', 'I', 'G', 'D', 'E', 'C'],
    'i': ['I', 'J', 'G', 'C', 'H', 'B', 'A', 'E', 'F', 'D'],
    'j': ['B', 'C', 'E', 'I', 'D', 'F', 'J', 'A', 'G', 'H']
}

Unit_Pref = {
    'A': ['g', 'a', 'h', 'f', 'd', 'b', 'i', 'j', 'c', 'e'],
    'B': ['f', 'i', 'j', 'd', 'a', 'b', 'e', 'g', 'h', 'c'],
    'C': ['h', 'd', 'j', 'b', 'g', 'a', 'i', 'e', 'f', 'c'],
    'D': ['h', 'j', 'g', 'i', 'b', 'a', 'e', 'f', 'd', 'c'],
    'E': ['h', 'i', 'e', 'f'],
    'F': ['h', 'd', 'i', 'b', 'g', 'a', 'f', 'e', 'j', 'c'],
    'G': ['g', 'f', 'e', 'h', 'b', 'c', 'j', 'i', 'a', 'd'],
    'H': ['i', 'c', 'd', 'h', 'j', 'b', 'e', 'f', 'g', 'a'],
    'I': ['d', 'f', 'e', 'j', 'b', 'a', 'g', 'i', 'c', 'h'],
    'J': ['a', 'h', 'c', 'b', 'i', 'j', 'g', 'f', 'd', 'e']
}


# Ensuring each unit's preference list includes all officers
for unit, prefs in Unit_Pref.items():
    missing_officers = set(Officers) - set(prefs)
    Unit_Pref[unit].extend(list(missing_officers))

# Function for the stable matching algorithm
def stable_matching(Officers, Units, Off_Pref, Unit_Pref):
    Off_Free = list(Officers)
    Matches = {officer: '' for officer in Officers}

    while Off_Free:
        for officer in Off_Free.copy():  # Iterate over a copy of Off_Free
            for unit in Off_Pref[officer]:
                if unit not in Matches.values():
                    Matches[officer] = unit
                    Off_Free.remove(officer)
                    break
                else:
                    current_suitor = list(Matches.keys())[list(Matches.values()).index(unit)]
                    if Unit_Pref[unit].index(officer) < Unit_Pref[unit].index(current_suitor):
                        Matches[officer] = unit
                        Off_Free.remove(officer)
                        Matches[current_suitor] = ''
                        Off_Free.append(current_suitor)
                        break
    return Matches

# Running the modified stable matching algorithm
matches = stable_matching(Officers, Units, Off_Pref, Unit_Pref)

# Print the results
for officer, unit in matches.items():
    print(f"Officer {officer} is matched with Unit {unit}")
