import os, pyfiglet
from termcolor import colored

team1 = ['1a', '2a', '3a', '4a', '5a', '6a']
team2 = ['1b', '2b', '3b', '4b', '5b', '6b']
field = []

def main():
    while True:
        display_menu()
        uinput = input("Choose option ('e' to exit): ")
        if uinput == 'e':
            break
        else:
            menu_choice(uinput)

def clear_screen():
    os.system('cls')

def start_match():
    team1_points = 0
    team2_points = 0

    team1_sets = 0
    team2_sets = 0

    clear_screen()
    print("=== START NEW MATCH ===")

    team1_name = input("Name of first team: ")
    team2_name = input("Name of second team: ")

    #display points , sets with team names
    clear_screen()
    print(f'Current set: {team1_sets + team2_sets}')
    print(f'{team1_name} {team1_points}\t{team1_sets}:{team2_sets]\t{team2_points} {team2_name}')
    

    input("\nPress ENTER to return to menu...")

def view_stats():
    clear_screen()
    print("=== VIEW STATISTICS ===")
    print("Statistics would be displayed here...")
    input("\nPress ENTER to return to menu...")

def manage_players():
    clear_screen()
    print("=== PLAYER MANAGEMENT ===")
    print("Player management interface...")
    input("\nPress ENTER to return to menu...")

def update_field(team1, team2):

    return [
        [team1[4], team1[3], team2[1], team2[0]],
        [team1[5], team1[2], team2[2], team2[5]],
        [team1[0], team1[1], team2[3], team2[4]],
    ]

def rotation(team):
    popped_player = team.pop(0)
    team.append(popped_player)

def display_menu():
    ascii_art = pyfiglet.figlet_format("Volleyball Tracker", font='fender', width = 133, justify = 'center')
    c_ascii_art = colored(ascii_art, 'red')
    print(colored('=' * 133, 'red'))
    print("\n\n\n")
    print(c_ascii_art)
    print()
    print(colored('=' * 133, 'red'))

    print("1. Start New Match")
    print("2. View Statistics") 
    print("3. Player Management")
    print()

def menu_choice(uinput):
    match uinput:
        case '1':
            start_match()
        case '2':
            view_stats()
        case '3':
            manage_players()
        case 'e':
            quit()
        case _:
            clear_screen()
            input('Invalid input! Press ENTER to try again...')

main()
