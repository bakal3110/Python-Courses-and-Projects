# simple version of point tracking

# lets try oop - is that simple though - maybe later then
# my classes would be (so far):
# - Player
# - Set

import os, sys
from pynput import keyboard
import pyfiglet
from time import sleep
from termcolor import colored

team1 = ['1a', '2a', '3a', '4a', '5a', '6a']
team2 = ['1b', '2b', '3b', '4b', '5b', '6b']
field = []


def main():
    with keyboard.Listener(on_release=on_release) as listener:
        while True:
            clear_screen()
            display_menu()
            listener.join()

def clear_screen():
    os.system('cls')

def on_release(key):
    if key == keyboard.Key.esc:
        print("Zamykanie programu...")
        sys.exit()
        return False  # To zatrzyma listener i pozwoli wyjść z programu
    elif hasattr(key, 'char') and key.char == '1':
        start_match()
    return True

    

# Start listening in a separate thread
#listener = keyboard.Listener(on_release=on_key_release)
#listener.start() #to start listening
# listener.join() to stop program execution until listener executes

def display_menu():
    #fonts = ['banner3-D', 'kban', 'larry3d', 'nancyj-fancy', 'r2-d2___', 'roman', 'slant', 'smslant', 'speed', 'standard', 'trek', '3-d', 'basic', 'chunky', 'epic', 'fender']
    #fonts = ['fender']
    #for font in fonts:
    #print(f"\nTesting font: {font}")
    ascii_art = pyfiglet.figlet_format("Volleyball Tracker", font='fender', width = 133, justify = 'center')
    c_ascii_art = colored(ascii_art, 'red')
    print(colored('=' * 133, 'red'))
    print("\n\n\n")
    print(c_ascii_art)
    print()
    print(colored('=' * 133, 'red'))
    #sleep(0.3)

    print("\nChoose option:")
    print("1. Start New Match")
    print("2. View Statistics") 
    print("3. Player Management")
    print()

def start_match():
    #while True:
        clear_screen()
        print("=== START NEW MATCH ===")
        print("Match setup would go here...")
        print("\nPress ENTER to return to menu...")

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

main()