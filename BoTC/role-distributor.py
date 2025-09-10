import random

characterAlignment_dict = {
    "Townsfolk" : ["Washerwoman", "Librarian", "Investigator", "Chef", "Empath", "Fortune Teller", "Undertaker", "Monk", "Ravenkeeper", "Virgin", "Virgin", "Slayer", "Soldier", "Mayor"],
    "Outsiders" : ["Butler", "Drunk", "Recluse", "Saint"],
    "Minions" : ["Poisoner", "Spy", "Scarlet Woman", "Baron"],
    "Demons" : ["Imp"]
}

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

# functions
def ChooseCharacters(characters, amount):
    chosenCharacters = random.sample(population=characters, k=amount)
    return chosenCharacters
# end of functions

print("How many players? (min 5, max 15)")
playerAmount = int(input())

characterDistribution_array = characterAmount_dict[playerAmount]
townsfolkAmount = characterDistribution_array[0]
outsidersAmount = characterDistribution_array[1]
minionsAmount = characterDistribution_array[2]
demonsAmount = characterDistribution_array[3]

# random sampling without replacement random.sample(population, k, *, counts=None)
# 1 solution
townsfolkCharacters = ChooseCharacters(characterAlignment_dict["Townsfolk"], townsfolkAmount)
print(townsfolkCharacters)
# 2 solution with 1 function going through two lists: alignments and characters with amount