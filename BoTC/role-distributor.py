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

# functions
def AssignCharactersForPlayerAmount(integer):
    return true
# end of functions

print("How many players? (min 5, max 15)")
playerAmount = int(input())

AssignCharactersForPlayerAmount(playerAmount)

# random sampling without replacement random.sample(population, k, *, counts=None)