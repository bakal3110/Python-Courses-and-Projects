import random

characterAlignment_dict = {
    "Townsfolk" : ["Washerwoman", "Librarian", "Investigator", "Chef", "Empath", "Fortune Teller", "Undertaker", "Monk", "Ravenkeeper", "Virgin", "Virgin", "Slayer", "Soldier", "Mayor"],
    "Outsiders" : ["Butler", "Drunk", "Recluse", "Saint"],
    "Minions" : ["Poisoner", "Spy", "Scarlet Woman", "Baron"],
    "Demons" : ["Imp"]
}

characterAlignment_array = ["Townsfolk", "Outsiders", "Minions", "Demons"]

characterAmount_dict = {
    5 : [3,0,1,1],
    6 : [3,1,1,1],
    7 : [5,0,1,1],
    8 : [5,1,1,1],
    9 : [5,2,1,1],
    10 : [7,0,2,1],
    11 : [7,1,2,1],
    12 : [7,2,2,1],
    13 : [9,0,3,1],
    14 : [9,1,3,1],
    15 : [9,2,3,1]
}

# Functions
def getCharacters(player_amount: int):
    '''
    Returns a list of randomly chosen characters in play. List values are lists of alignment's characters - [ Townsfolk, Outsiders, Minions, Demons ]
    Input: player amount as int
    '''
    # go through all alignments
    # pick random characters for each alignment in play
    characters = []
    for i in range(4):
        characters.append(random.sample(characterAlignment_dict[characterAlignment_array[i]], characterAmount_dict[player_amount][i]))
    return characters

# End of functions

# Program

# get amount of players
player_amount = int(input("How many players? (5 - 15): "))
print(getCharacters(player_amount))
# distribute characters at random for each player

# End of program

