def main(team1, team2):
    print('Simulate start of game and rotation of team left ')
    print('Field overview:')
    field = update_field(team1, team2)
    for row in field:
        print(row)

    print("Team 2 served, team 1 won the point. Rotation.")
    rotation(team1)

    print('Field overview:')
    field = update_field(team1, team2)
    for row in field:
        print(row)

team1 = ['1a', '2a', '3a', '4a', '5a', '6a']
team2 = ['1b', '2b', '3b', '4b', '5b', '6b']
field = []

def func():
    print('Start')
    print('Current lineup:')

    # Team 1  Team 2
    #  5 4   |   2 1
    #  6 3   |   3 6
    #  1 2   |   4 5
    # list index view
    #  4 3   |   1 0
    #  5 2   |   2 5
    #  0 1   |   3 4

    # next rotation
    #  5 4   |   1 0        for rotations
    #  0 3   |   2 5        pop = list.pop(0) then list.append(popped)
    #  1 2   |   3 4

def update_field(team1, team2):

    return [
        [team1[4], team1[3], team2[1], team2[0]],
        [team1[5], team1[2], team2[2], team2[5]],
        [team1[0], team1[1], team2[3], team2[4]],
    ]

def rotation(team):
    popped_player = team.pop(0)
    team.append(popped_player)

main(team1, team2)