"""Adventure game for Udacity Intro to Programming class."""
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

def intro():
    """Begin the game by introducing the scene."""
    print_pause("You awaken with a splitting headache in the middle of a field.")
    print_pause("Based on the large number of empty bottles lying around you"
                    " it must have been a heck of a party.")
    print_pause("You slowly get up off the ground.")
    clearing()

def clearing():
    """Create and controls interactions in the clearing area of the game."""
    choices = ["Go to the farmhouse", "Go to the"
                    " shed", "Enter the forest"]
    print_pause("\nYou are standing in a pleasant field on the outskirts"
                    " of a forest.")
    print_pause("The beauty of nature has been somewhat"
                    " spoiled by the fact that someone left a bunch of bottles"
                    " lying around the place")
    print_pause("To the right you see a large, old farmhouse.")
    print_pause("Directly ahead is a small garden shed.")
    print_pause("To your left stands a dark, forbodeing forest. ")
    if "note" not in inventory:
        print_pause("You notice what appears to be a note on the ground.")
        choices.append("Pick up the note")
    action = valid_input(choices)
    print(action)
    if action == "Go to the farmhouse":
        farmhouse()
    elif action == "Go to the shed":
        shed()
    elif action == "Enter the forest":
        forest(monster)
    elif action == "Pick up the note":
        print_pause("You pick up the hand-scribbled note and read it.")
        print_pause("The note says:\n")
        print_pause("Come on up to the farm house")
        print_pause("      - Emily")
        print_pause("p.s. - the magic word is XYZZY\n")
        inventory.append("note")
        clearing()

def forest(monster):
    """Create and controls interactions in the forest area of the game.

    Requires 1 value - monster (generated by random_choice() function)
    """
    choices = ["Pick flowers", "Go to the shed", "Return to the clearing"]
    print_pause("\nYou are in a charming glenn in the forest, covered in all"
                    " varities of widflowers.")
    print_pause("A gentle waterfall tinkles off to the left.")
    print_pause("To the right you can barely make out the ramshackle shed"
                    " you saw from the clearing.")
    if "fought monster" not in actions:
        print_pause(f"In the center of the clearing stands a fearsome {monster}!")
        choices.extend(["Run away!", "Fight!"])
    action = valid_input(choices)
    if action == "Pick flowers":
        if "fought monster" not in actions:
            print_pause(f"You should probably deal with the {monster} before you"
                            " try picking flowers.")
            forest(monster)
        elif "flowers" in inventory:
            print_pause("You already have a very nice bunch of flowers.")
            print_pause("Perhaps you should leave some for other adventurers.")
        else:
            print_pause("You carefully pick a nice bunch of wildflowers.")
            inventory.append("flowers")
        forest(monster)
    elif action == "Go to the shed":
        shed()
    elif action == "Run away!":
        print_pause("You scamper away to live and fight another day.")
        clearing()
    elif action == "Fight!":
        if "sword" in inventory:
            exclaimations = ["Pow!", "Biff!", "Bang!", "Klang!", "Swish!"]
            print_pause("You draw your sword and prepare for battle!")
            for n in range(3):
                print_pause(random.choice(exclaimations))
            print_pause(f"\nFinally the {monster} has had enough.")
            print_pause("With a pitiful whimper he runs off into the"
                        " deeper forest where you can't follow.")
            actions.append("fought monster")
            forest(monster)
        else:
            print_pause(f"Taking on a {monster} singlehandedly without any"
                            " kind of weapon really isn't advised.")
            print_pause(f"This point is proven as the {monster} unsheathes a"
                            " rather large and lethal-looking axe.")
            print_pause("You hastily perform a tactical withdrawl.")
            clearing()
    elif action == "Return to the clearing":
        clearing()

def shed():
    """Create and controls interactions in the shed area of the game.

    This area contains two required items - the keys and the sword.
    """
    choices = ["Leave the shed"]
    print_pause("\nThis is a decrepit, ramshackle garden shed.")
    print_pause("To the left you see an old wheelbarrow, piled high with rusted"
                    " and useless tools.")
    print_pause("To the right is a grimy window, through which you can see the"
                    " farmhouse.")
    if "keys" not in inventory:
        print_pause("A rather large set of keys is hanging on a hook by the"
                        " door on a rusty nail.")
        print_pause("It's a good thing your tetanus shot is up to date.")
        choices.append("Pick up the keys")
    if "sword" not in inventory:
        print_pause("An unusual glint among the rusty junk catches your eye.")
        print_pause("Someone has jammed a sword in a barrel in the corner.")
        choices.append("Pick up the sword")
    action = valid_input(choices)
    if action == "Leave the shed":
        clearing()
    elif action == "Pick up the keys":
        print_pause("You carefully pick up the set of keys.")
        inventory.append("keys")
        shed()
    elif action == "Pick up the sword":
        print_pause("You pick up the sword.")
        print_pause("Unlike everything else in here it's not covered in rust, and"
                    " it seems pretty sharp.")
        inventory.append("sword")
        shed()

def farmhouse():
    """Create and control actions for farmhouse entry portion of game.

    Users must have the keys to unlock the door and continue on.
    """
    choices = ["Knock on door", "Look under welcome mat", "Open door",
                "Return to clearing"]
    print_pause("\nYou are standing on the front porch of a weathered but"
                    " still pleasant-looking farmhouse. ")
    print_pause("At your feet is a welcome mat.")
    print_pause("The wooden front door is solidly closed, with a note that"
                " says \'Doorbell broken. Please knock.\'")
    if "keys" in inventory:
        choices.append("Unlock the front door")
    if "look under mat" in actions:
        choices.remove("Look under welcome mat")
    action = valid_input(choices)
    if action == "Knock on door":
        print_pause("You knock loudly on the door, but there's no response.")
        print_pause("Whoever is in there is a pretty sound sleeper.")
        farmhouse()
    elif action == "Open door":
        if "unlock door" in actions:
            print_pause("You step through the door and into the house.")
            house_entry()
        else:
            print_pause("The door appears to be firmly locked.")
            farmhouse()
    elif action == "Look under welcome mat":
        print_pause("You lift the corner of the mat up, disturbing"
                        " a family of spiders.")
        print_pause("Other than that, there's nothing under the mat.")
        actions.append("look under mat")
        farmhouse()
    elif action == "Return to clearing":
        clearing()
    elif action == "Unlock the front door":
        if "unlock door" in actions:
            print_pause("The door is already unlocked.")
            print_pause("It can't get any more unlocked.")
            print_pause("It has reached the pinnacle of unlocked-ness.")
            farmhouse()
        else:
            print_pause("You find a key on the rusty key ring that seems to fit"
                            " the front door and unlock the front door.")
            actions.append("unlock door")
            farmhouse()

def house_entry():
    """Create and control actions in the entry room of the farmhouse"""
    choices = ["Leave house", "Enter living room", "Look in mirror"]
    print_pause("\nYou're standing in the entryway of the farmhouse.")
    print_pause("The rug in here is somewhat threadbare but clean, and"
                    " really ties the room together.")
    print_pause("A mirror hangs on the wall to the right")
    action = valid_input(choices)
    if action == "Leave house":
        print_pause("You open the front door and exit the house.")
        farmhouse()
    elif action == "Enter living room":
        print_pause("Pausing only to admire the rug one more time you walk "
                        "into the living room.")
        house_livingroom()
    elif action == "Look in mirror":
        if "look in mirror" in actions:
            print_pause("Look - there are more important things to do today"
                            " than to stand around looking at yourself in"
                            " the mirror all day.")
            house_entry()
        else:
            print_pause("This mirror is clearly an antique, with beautiful "
                            "hand-carved inlays and real gold leaf.")
            print_pause("From what you can see, it might be time to schedule"
                        " a haircut appointment.")
            actions.append("look in mirror")
            house_entry()
    elif action == "XYZZY":
        if "use magic word" not in actions:
            print_pause("The mirror's reflection suddenly shifts and jumbles.")
            print_pause("Instead of a perfectly ordinary reflection you now"
                        " see a fearsome demon.")
            print_pause("He (she?) makes a rude gesture and disappears, leaving"
                        " a perfectly ordinary reflection of you.")
            print_pause("You still need a haircut.")
            actions.append("use magic word")
            house_entry()
        else:
            print_pause("Nothing happens.")
            print_pause("It looks like the magic has all been used up.")
            house_entry()

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
    if "tray" not in inventory:
        print_pause("A tea tray sits on the coffee table.")
        choices.append("Pick up the tray")
    if "vase" not in inventory:
        print_pause("An interesting-looking vase sits on a bureau against the"
                    " right wall.")
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
            print_pause("Some people just can't wake up without their"
                        " morning coffee.")
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
            print_pause("Flowers are always a nice present."
            print_pause("Maybe check the surrounding forest for"
            " some wildflowers.")
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
        print_pause("It might be worth knocking on the bedroom"
                    " door again.")
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

def house_bedroom(monster):
    print_pause("The door opens to reveal Emily, wearing a big"
                " smile and a Starfleet Academy t-shirt.")
    print_pause("She reaches for the cup of coffee and beckons"
                " for you to follow her into the bedroom.")
    print_pause(f"\"By the way\", she asks. \"Have you seen my pet {monster}?\"")
    play_again()

def play_again():
    time.sleep(1)
    for n in range(5)
        print("*")
        time.sleep(.25)
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


def generate_RME():
    """Select random monster from list and return to game."""
    RME = ["ogre", "goblin", "gnoll", "orc", "personal injury lawyer"]
    monster = random.choice(RME)
    return monster

inventory = []
actions = []
monster = generate_RME()
intro()

"""This is a temporary list
house_kitchen


actions:
Make coffee
flowers in vase
"""
