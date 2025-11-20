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

def getBluffs(characters_in_play):
    '''
    Returns a list of three characters not in play. Only from Townsfolk and Outsiders.
    Input: list of characters in play
    '''
    characters_not_in_play = []
    for i in range(2):
        for character in characterAlignment_dict[characterAlignment_array[i]]:
            if character not in characters_in_play[i]:
                characters_not_in_play.append(character)
    bluffs = random.sample(characters_not_in_play, 3)
    return bluffs

def distributeRoles(characters_in_play):
    '''
    Distributes characters randomly
    Input: list of characters in play
    '''
    return True

# End of functions

# Program

# get amount of players
player_amount = int(input("How many players? (5 - 15): "))
characters_in_play = getCharacters(player_amount)
print(characters_in_play)

# get bluffs
    # get list of characters not in play, only townsfolk and outsiders
bluffs = getBluffs(characters_in_play)

# distribute characters at random for each player
distributeRoles(characters_in_play)

# End of program


