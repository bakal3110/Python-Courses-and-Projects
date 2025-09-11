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

charactersInPlay = []
chosenCharacters = []

alignment_index = 0

# functions
# end of functions

# program
print("How many players? (min 5, max 15)")
playerAmount = int(input())

for number_of_characters in characterAmount_dict[playerAmount]:
    if number_of_characters == 0: alignment_index += 1
    else:
        current_alignment = characterAlignment_array[alignment_index]
        chosenCharacters = random.sample(population=characterAlignment_dict[current_alignment], k=number_of_characters)
        for character in chosenCharacters:
            charactersInPlay.append(character)
        alignment_index += 1
# end of program