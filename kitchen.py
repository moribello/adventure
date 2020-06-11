import time
import random

def print_pause(message):
    """Print a line and pause before continuing."""
    print(message)
    time.sleep(.5)

def valid_input(choices):
    """Check for valid input based on choices list."""
    while True:
        print_pause("\nYou may:")
        for choice in choices:
            print_pause(choice)
        valid_input = input("What would you like to do?\n")
        if valid_input == "inventory":
            print_pause("You are currently carrying")
            for item in inventory:
                print_pause(item)
        else:
            for choice in choices:
                if valid_input in choice:
                    return choice
            print_pause("I'm sorry - I don't understand that. Please select"
                            " one of the above choices.")

def farmhouse_kitchen():
    choices = ["Go to living room", "Make coffee"]
    if "vase" in inventory and "flowers" in inventory:
        if "flowers in vase" not in inventory:
            choices.append("Put flowers in vase")
    print_pause("You are standing in a small but well equipped kitchen.")
    print_pause("In front of you is a porcelain sink equipped with a fancy"
                    " brass tap.")
    print_pause("To the right of that, on the counter, are several coffee"
                    " mugs and a fancy-looking coffee maker.")
    if "make coffee" in actions and "cup of coffee" not in inventory:
        choices.append("Pick up cup of coffee")
        choices.remove("Make coffee")
        print_pause("A steaming cup of coffee sits on the counter.")
    action = valid_input(choices)
    if action == "Go to living room":
        house_livingroom()
    elif action == "Make coffee":
        print_pause("You fill the coffee pot with water from the tap"
                            " and, after a certain amount of pushing buttons"
                            " and pulling levers, achieve coffee.")
        print_pause("The scent of coffee seems to have woken"
                        " the sleeper up.")
        print_pause("At least the snoring seems to have stopped.")
        if "vase" in inventory or "flowers in vase" in inventory:
            if "tray" not in inventory:
                print_pause("You quickly realize that you don't have"
                                    " enough hands to carry both the vase"
                                    " and a cup of coffee.")
                print_pause("Perhaps if you had some kind of tray...")
                if "pick up coffee" not in choices:
                    choices.append("pick up coffee")
            else:
                print_pause("You carefully pour a cup of coffee and place"
                                " it on the tray next to the vase")
                actions.append("make coffee")
                inventory.append("cup of coffee")
        else:
            print_pause("You carefully pour a cup of coffee and place"
                        " it on the tray next to the vase")
            print_pause("The scent of coffee seems to have woken"
                            " the sleeper up.")
            print_pause("At least the snoring seems to have stopped.")
            actions.append("make coffee")
            inventory.append("cup of coffee")
            farmhouse_kitchen()
    elif action == "Put flowers in vase":
        if "tray" not in inventory:
            if "cup of coffee" in inventory:
                print_pause("You quickly realize that you aren\'t going to be able to hold that hot cup of coffee"
                            " and a vase full of flowers at the same time.")
                print_pause("Perhaps if you had some kind of tray...")
                farmhouse_kitchen()
            else:
                print_pause("You add water from the tap to the vase and"
                            " carefully arrange the flowers you picked.")
                inventory.append("flowers in vase")
                inventory.remove("flowers")
                inventory.remove("vase")
                farmhouse_kitchen()
    elif action == "Pick up cup of coffee":
        if "tray" not in inventory:
            if "flowers in vase" in inventory:
                print_pause("You quickly realize that you aren\'t going to be able to hold that hot cup of coffee"
                            " and a vase full of flowers at the same time.")
            else:
                print_pause("You carefully pour a cup of coffee and place"
                                " it on the tray next to the vase")
                actions.append("make coffee")
                inventory.append("cup of coffee")
        farmhouse_kitchen()

inventory = ["flowers", "keys", "sword", "vase"]
actions = []

farmhouse_kitchen()
