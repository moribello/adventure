import time

def print_pause(message):
    """Print a line and pause before continuing."""
    print(message)
    time.sleep(.5)

def play_again():
    time.sleep(1)
    while True:
        restart = input("Would you like to play again? (y or n) ")
        if restart == "y":
            inventory = []
            actions = []
            monster = generate_RME
            return inventory, actions, monster
        if restart == "n":
            print_pause("Thanks for playing!")
            break
        else:
            print_pause("I'm sorry - I don't understand that.")

play_again()
