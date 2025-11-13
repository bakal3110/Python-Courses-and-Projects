# simple version of point tracking

# lets try oop - is that simple though - maybe later then
# my classes would be (so far):
# - Player
# - Set

import os
from pynput import keyboard
import pyfiglet
from time import sleep
from termcolor import colored

clear_screen = lambda: os.system('cls')
def on_key_release(key):
    match key:
        case keyboard.Key.esc:
            # Stop listener
            return False
        case keyboard.Key.('1'):
            start_match()

    

# Start listening in a separate thread
listener = keyboard.Listener(on_release=on_key_release)
# listener.start() to start listening
# listener.join() to start listening and stop until listener executes

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
    while True:
        clear_screen()
        print("=== START NEW MATCH ===")
        print("Match setup would go here...")
        user_input = input("\nPress ENTER to return to menu...")
        match user_input:
            case _:
                return False

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

def main():
    while True:
        clear_screen()
        display_menu()
        listener.start()
        listener.join()

main()