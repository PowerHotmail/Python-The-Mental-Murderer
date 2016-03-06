# By PowerHotmail
# The Mental Murderer
# Core File
# Core things within the game is handled here.

# ------------------------------------------------------------------------------------------------------- #

# Importing
import time;
import threading;
from functools import partial

# ------------------------------------------------------------------------------------------------------- #

# Modules
from EaseOfUse import *
from People import *
from Rooms import *

# ------------------------------------------------------------------------------------------------------- #

# Welcome Messages.
# Presents messages for the first time being opened.
WelcomeMessages = [

    "Brought to you by PowerHotmail.",
    "Welcome to The Mental Murderer!",
    "The Mental Murderer (TMM), is a murder-mystery game. Your objective is to find out who the murderer is by collecting evidence.",
    "Use 'help' during interaction mode to get a list of commands.",
    "There will be a 1 second wait for every checkpoint to prevent instant clutter of your screen.",
    "INTERACTION MODE is whenever the game asks you to input something.",
    
                    ];

ClearLine();

print("The Mental Murderer");
print("*******************");

# Loop through the welcome messages and printing them.
for WelcomeMessage in WelcomeMessages:
    time.sleep(1);
    ClearLine();
    print(WelcomeMessage);

# ------------------------------------------------------------------------------------------------------- #

# Room Interaction functions setting.
# Settings all the functions because of Python's stupid Cyclic Dependencies (changes a lot of this code :( ).
# All the "Use" functions... Python HAS to run 

def Take(ItemName, Room):
    Rooms[Room].pop(ItemName, None);
    print("The " + ItemName + " has been taken.");
    Backpack[ItemName] = Room;
    InteractWithRoom(Room, "Placeholder2");

# G-English-2

RoomInteraction["G-English-2"]["Pen"]["Take"] = partial(Take, "Pen", "G-English-2");

RoomInteraction["G-English-2"]["Ruler"]["Take"] = partial(Take, "Ruler", "G-English-2");

# G-English-3

def GunUse():
    PlaySound("GunShot");
    print("There are no bullets. But the sound of shooting still plays.");
    InteractWithItem("G-English-3", "Gun");

RoomInteraction["G-English-3"]["Gun"]["Take"] = partial(Take, "Gun", "G-English-3")
RoomInteraction["G-English-3"]["Gun"]["Use"] = GunUse;

def LaptopUse(Placeholder1=None, Placeholder2=None):
    ClearLine();
    
    print("Using The Laptop");
    print("****************");

    ClearLine();

    print("To return, say 'return' or 'G-English-3'.");

    ClearLine();
    
    TabsOpen = {

        "Google":  "A search for: 'Dealing with threat emails.'.",
        "Outlook": "The latest email states: 'Watch out - I'm coming for you.'.",
        "Police":  "An advice page for reporting threats.",
        "eBay":    "Self defence weapons are being listed.",
        "Spotify": "Currently playing - OMI Cheerleader",
            
                };

    LoopList(TabsOpen, False);

    ClearLine();

    Interaction = input("What would you like to interact with? ");

    ClearLine();

    def FunctionToRun(Item1, Item2):
        print(Item2);
        if Item1 == "Spotify":
            PlaySound("Cheerleader");

        LaptopUse("Placeholder1", "Placeholder2");
    
    InteractionalLoop(Interaction, TabsOpen, LaptopUse, None, None, "G-English-3", InteractWithRoom, "G-English-3", None, FunctionToRun);
                      
RoomInteraction["G-English-3"]["Laptop"]["Use"] = LaptopUse;

# G-English-4

RoomInteraction["G-English-4"]["Case"]["Take"] = partial(Take, "Case", "G-English-4");

# G-English-5

RoomInteraction["G-English-5"]["Glasses"]["Take"] = partial(Take, "Glasses", "G-English-5");

RoomInteraction["G-English-5"]["Photo"] = partial(Take, "Photo", "G-English-5");

# ------------------------------------------------------------------------------------------------------- #

# Start
# Starts a new game.
def Start():
    ClearLine();
    
    print("Starting A New Game");
    print("*******************");

    ClearLine();

    print("There's a wild murderer loose! We need your help to stop him.");
    print("As the sheriff, it's up to you to find out who this murderer is!");
    print("Your job: Gather evidence/clues and find out who this murderer really is.");

    ClearLine();

    # Defining a global variable to store the sheriff's name.
    global SheriffName
    SheriffName = input("So sheriff, what is your name? ");

    # Making a backpack for all the items.
    global Backpack
    Backpack = {};

    ClearLine();

    print("Welcome, " + SheriffName + ". For now, we'll leave you to it.");

    # Starting the game off in the Hallway.
    Hallway("Placeholder1", "Placeholder2");

# ------------------------------------------------------------------------------------------------------- #

# Hallway
# The command for being in the hallway.
def Hallway(Placeholder1, Placeholder2):
    ClearLine();

    print("In The Hallway");
    print("**************");

    ClearLine();

    print("The rooms you can go to are:");

    ClearLine();

    # Loop through the string keys (RoomNames).
    LoopList(Rooms, False);

    ClearLine();

    # Getting the players input.
    Interaction = input("Where would you like to go " + SheriffName + "? ");

    def FunctionToRun(Item1, Item2):
        InteractWithRoom(Item1, "Placeholder2");

    InteractionalLoop(Interaction, Rooms, Hallway, None, None, "Hallway", Hallway, None, None, FunctionToRun);

# ------------------------------------------------------------------------------------------------------- #

# Help Commands
# Stores the help messages along with their actions.
HelpCommands = {};

def LoopTable(List):
    ClearLine();

    print("Displaying List");
    print("***************");

    ClearLine();

    LoopList(List, False);

HelpCommands["Innocent"] = partial(LoopTable, InnocentPeople);

HelpCommands["Suspicous"] = partial(LoopTable, SuspicousPeople);

HelpCommands["Rooms"] = partial(LoopTable, Rooms);

HelpCommands["Restart"] = Start;

def GuiltyF(PersonName, Placeholder2):
    ClearLine();

    print("Sheriff Declares Guilty");
    print("***********************");

    ClearLine();

    if PersonName in SuspicousPeople:

        Interaction = input("Are you sure that '" + PersonName + "' is guilty? ");

        ClearLine();

        Answers = {}
        Answers["Yes"] = "Yes";
        Answers["No"] = "No";

        def FunctionToRun(Item1, Item2):
            if Item1 == "Yes":
                print("Alright, " + SheriffName + ". We'll carry on.");

                ClearLine();

                print("We are now executing " + PersonName + ". Hopefully you are right.");
    
                ClearLine();
                time.sleep(1);

                # That person was guilty!
                if ChosenMurderer == PersonName:
                    print("Congratulations! You have successully stopped the murderer!");
                    PlaySound("Win");

                # That person is not guilty!
                else:
                    print("Game Over! Unfortunetly " + PersonName + " is not the murderer. Poor souls (you and " + PersonName + "'s).");
                    PlaySound("GameOver");

                Start();
                
            else:
                print("Alright, " + SheriffName + ". Make sure to find out soon!");

                ClearLine();
    
        InteractionalLoop(Interaction, Answers, GuiltyF, PersonName, None, "Guilty", GuiltyF, PersonName, None, FunctionToRun);
        
    else:
        print(PersonName + " is not a suspicous person.");

HelpCommands["Guilty"] = GuiltyF;

def BackpackF(Placeholder1, Placehodler2):
    ClearLine();

    print("Showing Backpack");
    print("****************");

    ClearLine();

    print("To return, say 'return' or 'hallway'.");
    
    ClearLine();

    if len(Backpack) == 0:
        print("There are no items in your backpack.");
        return;

    LoopList(Backpack, False);

    ClearLine();

    Interaction = input("What would you like to interact with? ");

    ClearLine();

    def FunctionToRun(Item1, Item2):        
        ClearLine();

        # Getting the specific item from the "RoomInteraction" dictionary.
        Item = RoomInteraction[Item2][Item1];

        print("Interacting With Item");
        print("*********************");

        ClearLine();

        print("To return, say 'return' or '" + Item2 + "'.");
        
        ClearLine();

        print("You can interact with: ");

        ClearLine();

        for ItemName in Item:
            if ItemName != "Take":
                print(ItemName);
                
        ClearLine();

        Interaction = input(SheriffName + ", what would you like to interact with? ");

        ClearLine();

        def FunctionToRun(Item1, Item2):
            if type(Item2) is str:
                print(Item2);
            else:
                Item2();
                    
        InteractionalLoop(Interaction, Item, FunctionToRun, Item2, ItemName, Item2, InteractWithRoom, Item2, None, FunctionToRun);

    InteractionalLoop(Interaction, Backpack, BackpackF, None, None, "Hallway", Hallway, None, None, FunctionToRun);

HelpCommands["Backpack"] = BackpackF;

# ------------------------------------------------------------------------------------------------------- #

def InteractionalLoop(Interaction, Dictionary, Function=None, FuncArg1=None, FuncArg2=None, ReturnSelection=None, ReturnFunction=None, ReturnArg1=None, ReturnArg2=None, FunctionToRun=None):
        ClearLine();            

        # Setting some default arguments.
        # Note: These are ultra annoying... In the future, I should learn more about "optional" arguments and save my self the cringing.

        # For "Function" function.
        if Function == None:
            def Function(Placeholder1, Placeholder2):
                return;
            
        elif FuncArg1 == None:
            FuncArg1, FuncArg2 = "Placeholder1", "Placeholder2";

        elif FuncArg2 == None:
            Func2 = "Placeholder";

        # For "Return" function.
        if ReturnFunction == None:
            def ReturnFunction(Placeholder1, Placeholder2):
                return;
            
        elif ReturnArg1 == None:
            ReturnArg1, ReturnArg2 = "Placeholder1", "Placeholder2";

        elif ReturnArg2 == None:
            ReturnArg2 = "Placeholder2";
        
        # Making the interaction all lower case.
        LoweredInteraction = Interaction.lower();
        
        # Loop through the dictionary.
        for Item1, Item2 in Dictionary.items():
            # Item1 has been found in the interaction.
            if LoweredInteraction.find(Item1.lower()) != -1:
                FunctionToRun(Item1, Item2);

                time.sleep(1);
                Function(FuncArg1, FuncArg2);
                return Item1, Item2;

            # Help has been found in the interaction.
            elif LoweredInteraction.find("help") != -1:
                DisplayHelp();

                time.sleep(1);
                Function(FuncArg1, FuncArg2);
                return "help";

            # Return and ReturnSelection has been found.
            elif LoweredInteraction.find("return") != -1 or LoweredInteraction.find(ReturnSelection.lower()) != -1:
                ReturnFunction(ReturnArg1, ReturnArg2);

                time.sleep(1);
                Function(FuncArg1, FuncArg2);
                return "return"

            # Searching through HelpCommands.
            else:
                for HelpName, HelpAction in HelpCommands.items():
                    if LoweredInteraction.find(HelpName.lower()) != -1:
                        if HelpName.lower() == "guilty":
                            HelpAction((Interaction[7:]).strip(), "Placeholder2");

                        elif HelpName.lower() == "backpack":
                            HelpAction("Placeholder1", "Placeholder");
                            
                        else:
                            HelpAction();

                        time.sleep(1);
                        Function(FuncArg1, FuncArg2);
                        return HelpName, HelpAction;
                                    
        # Couldn't understand.
        print("Could not understand, " + SheriffName + ".");
        print("Please try again.");
        
        Function(FuncArg1, FuncArg2);
        return False;

# ------------------------------------------------------------------------------------------------------- #

# InteractWithItem
# The command for interacting with an item.
def InteractWithItem(RoomName, ItemName):
    ClearLine();

    # Getting the specific item from the "RoomInteraction" dictionary.
    Item = RoomInteraction[RoomName][ItemName];

    print("Interacting With Item");
    print("*********************");

    ClearLine();

    print("To return, say 'return' or '" + RoomName + "'.");

    ClearLine();

    print("You can interact with: ");

    ClearLine();

    LoopList(Item, False);

    ClearLine();

    Interaction = input(SheriffName + ", what would you like to interact with? ");

    ClearLine();

    def FunctionToRun(Item1, Item2):
        if type(Item2) is str:
            print(Item2);
        else:
            Item2();
                
    InteractionalLoop(Interaction, Item, InteractWithItem, RoomName, ItemName, RoomName, InteractWithRoom, RoomName, None, FunctionToRun);

# ------------------------------------------------------------------------------------------------------- #

# InteractWithRoom
# The command for interacting with a room.
def InteractWithRoom(RoomName, Placeholder):
    ClearLine();

    # Getting the specific room from the "Rooms" dictionary.
    Room = Rooms[RoomName];

    print("In " + RoomName);
    print("**************");

    ClearLine();

    print("To return, say 'return' or 'hallway'.");

    ClearLine();

    print("The items within this room are:");

    ClearLine();

    # Loop through the string keys (ItemNames).
    LoopList(Room, False);

    ClearLine();

    Interaction = input("What would you like to interact with, " + SheriffName + "? ");

    def FunctionToRun(Item1, Item2):
        InteractWithItem(RoomName, Item1);

    InteractionalLoop(Interaction, Room, InteractWithRoom, RoomName, None, "Hallway", Hallway, None, None, FunctionToRun);

# ------------------------------------------------------------------------------------------------------- #

# Starting the game.
Start();

# ------------------------------------------------------------------------------------------------------- #




