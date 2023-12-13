# Initialization
Officers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Units = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Preferences
Off_Pref = {  # indicates the preferences of the officers 
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
    'E': ['h', 'i', 'e', 'f', 'a', 'd', 'g', 'j', 'b', 'c'],
    'F': ['h', 'd', 'i', 'b', 'g', 'a', 'f', 'e', 'j', 'c'],
    'G': ['g', 'f', 'e', 'h', 'b', 'c', 'j', 'i', 'a', 'd'],
    'H': ['i', 'c', 'd', 'h', 'j', 'b', 'e', 'f', 'g', 'a'],
    'I': ['d', 'f', 'e', 'j', 'b', 'a', 'g', 'i', 'c', 'h'],
    'J': ['a', 'h', 'c', 'b', 'i', 'j', 'g', 'f', 'd', 'e']
}
def main():
    Off_Free = list(Officers)
    Unit_Free = list(Units)
    # Part 3: Proposal
    Matches = {
        'a':  '',
        'b': '',
        'c': '',
        'd': '',
        'e':  '',
        'f': '',
        'g': '',
        'h': '',
        'i':  '',
        'j': ''
    }

    key_list = list(Matches.keys())

    # the algorithm

    while len(Off_Free) > 0:
       for officer in Off_Free.copy():  # Iterate over a copy of Off_Free
        for unit in Off_Pref[officer]:
            if unit not in Matches.values():
                Matches[officer] = unit
                if officer in Off_Free:  # Check if the officer is still free before removing
                    Off_Free.remove(officer)
                print('{} is tentatively matched to {}'.format(officer, unit))
                break
            elif unit in Matches.values():
                current_suitor = list(Matches.keys())[list(Matches.values()).index(unit)]
                w_list = Unit_Pref.get(unit)
                if w_list.index(officer) < w_list.index(current_suitor):
                    Matches[officer] = unit
                    if officer in Off_Free:  # Check if the officer is still free before removing
                        Off_Free.remove(officer)
                    Matches[current_suitor] = ''
                    if current_suitor not in Off_Free:  # Add the current suitor back if they are not in the list
                        Off_Free.append(current_suitor)
                    print('{} was matched to {} but now is matched to {}'.format(unit, current_suitor, officer))


    print('\n ')
    print('Stable Matching Finished! Enjoy your new assignment!')
    for officer in Matches.keys():
        print('{} is matched to {} !'.format(officer, Matches[officer]))


if __name__ == "__main__":
    main()
