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
            print_pause("You are currently carrying:")
            for item in inventory:
                print_pause(item)
        elif valid_input == "actions":
            for action in actions:
                print(action)
        else:
            for choice in choices:
                if valid_input.lower() in choice.lower():
                    return choice
            print_pause("I'm sorry - I don't understand that. Please select"
                            " one of the following choices.")

def house_livingroom():
    """Create and control interactions in living room area of the house.

    This area contains the tray, which is required to bring everything to the
    bedroom, and the vase, which is needed to bring flowers.
    """
    choices = ["Go to the kitchen", "Return to entryway", "Sit on the couch",
                    "Read magazines", "Knock on the bedroom door"]
    print_pause("\nYou are standing in the living room of the farmhouse.")
    print_pause("A comfy-looking couch sits next to a coffee table covered in"
                    " fashion magazines.")
    print_pause("To the left is what appears to be a small kitchen.")
    print_pause("Directly ahead is a closed door. From the loud snoring coming"
                    " from it, this is probably the bedroom.")
    print_pause("An interesting-looking vase and a lacquered tea tray sit"
                    " atop a bureau against the right wall.")
    if "tray" not in inventory:
        choices.append("Pick up the tray")
    if "vase" not in inventory:
        choices.append("Pick up the vase")
    action = valid_input(choices)
    if action == "Go to the kitchen":
        house_kitchen()
    elif action == "Return to entryway":
        house_entry()
    elif action == "Sit on the couch":
        print_pause("Well. Isn't this nice.")
        print_pause("After awhile you get the vague sense that you're supposed"
                        " to be doing something, so you stand up.")
        house_livingroom()
    elif action == "Pick up the tray":
        print_pause("You pick up the tea tray. It's got a rather nice"
                        " chrysanthemum inlay on it.")
        inventory.append("tray")
    elif action == "Pick up the vase":
        print_pause("You pick up the vase, which appears to be a rather cheap"
                        " Ming dynasty reproduction.")
        inventory.append("vase")
    elif action == "Read magazines":
        if "read magazines" not in actions:
            print_pause("After several minutes of careful study you now know the"
                            " secret to perfect lipstick, Beyonce's 15 top hair"
                            " tips, and how to drive your man wild.")
            print_pause("Congratulations.")
            actions.append("read magazines")
        else:
            print_pause("You've already read these magazines and learned all"
                            " of its eldritch fashion tips.")
    elif action == "Knock on the bedroom door":
        if "make coffee" not in actions:
            print_pause("You hammer on the bedroom door.")
            print_pause("The only effect this seems to have in an increase in"
                        " the volume and frequency of the snoring.")
        elif "flowers in vase" in inventory and "cup of coffee" in inventory:
                house_bedroom(monster)
        elif "flowers" in inventory:
            if "vase" not in inventory:
                print_pause("You can't just give someone a handful of flowers.")
                print_pause("Maybe arrange them in a nice vase with some water"
                        " in it.")
            else:
                print_pause("Those flowers will never survive without"
                            " some water. Maybe you can get some from the"
                            " kitchen.")
        else:
            print_pause("You should probably come bearing gifts.")
            print_pause("Flowers are always a nice present. Maybe check the"
                        " surrounding forest for some wildflowers.")
    house_livingroom()

def house_kitchen():
    choices = ["Go to living room"]
    if "vase" in inventory and "flowers" in inventory:
        if "flowers in vase" not in inventory:
            choices.append("Put flowers in vase")
    print_pause("\nYou are standing in a small but well equipped kitchen.")
    print_pause("In front of you is a porcelain sink equipped with a fancy"
                    " brass tap.")
    print_pause("To the right of that, on the counter, are several coffee"
                    " mugs and a fancy-looking coffee maker.")
    if "make coffee" not in actions:
        choices.append("Make coffee")
    if "make coffee" in actions and "cup of coffee" not in inventory:
        choices.append("Pick up cup of coffee")
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
                inventory.append("cup of coffee")
        else:
            if "tray" in inventory:
                print_pause("You carefully pour a cup of coffee and place"
                            " it on the tray.")
                inventory.append("cup of coffee")
            else:
                print_pause("You carefully pour a cup of coffee but realize"
                            " that it's too hot to carry around.")
                print_pause("You put the hot cup of coffee down on the counter.")
                print_pause("Perhaps some kind of tray would make it easier"
                            " to carry the cup of coffee.")
        actions.append("make coffee")
        house_kitchen()
    elif action == "Put flowers in vase":
        if "tray" not in inventory:
            if "cup of coffee" in inventory:
                print_pause("You quickly realize that you aren\'t going to be able to hold that hot cup of coffee"
                            " and a vase full of flowers at the same time.")
                print_pause("Perhaps if you had some kind of tray...")
        else:
            print_pause("You add water from the tap to the vase and"
                        " carefully arrange the flowers you picked.")
            inventory.append("flowers in vase")
            inventory.remove("flowers")
            inventory.remove("vase")
        house_kitchen()
    elif action == "Pick up cup of coffee":
        if "tray" not in inventory:
            print_pause("The coffee is still too hot to carry without some"
                            " kind of tray-shaped object.")
        else:
            print_pause("You pick up the cup of coffee and place it on"
                        " the tray.")
            inventory.append("cup of coffee")
        house_kitchen()

inventory = ["keys", "sword", "flowers"]
actions = []

house_livingroom()
