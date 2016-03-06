# By PowerHotmail
# The Mental Murderer
# Ease Of Use (EaseOfUse) Module
# A module to help program that little bit more easier.

# ------------------------------------------------------------------------------------------------------- #

# Importing
import time;
import winsound, sys

# ------------------------------------------------------------------------------------------------------- #

# Modules


# ------------------------------------------------------------------------------------------------------- #

# ClearLine
# A function to easily make a new line.
# This is for practicallity, not efficiency. 
def ClearLine():
	print(" ");

# ------------------------------------------------------------------------------------------------------- # 

# LoopList
# A function to easily loop through a list and print the contents.
def LoopList(List, Dictionary):
    if not Dictionary:
        for Item in List:
            print(Item);
    else:
        for Item, Item2 in List.items():
            print(Item + ": " + Item2);
                           
# ------------------------------------------------------------------------------------------------------- # 

# DisplayHelp
# A function which displays the help screen.
def DisplayHelp():
    
    HelpMessages = {

        "Innocent": "Shows a list of all innocent people.",
        "Suspicous": "Shows a list of currently suspicous people.",
        "Rooms": "Shows a list of all rooms.",
        "Restart": "Restarts the current game.",
        "Guilty PERSON NAME": "You find someone to be guilty. If right, then you win the game. If wrong, game over. This only works like: 'guilty ExampleName' not like: 'I think ExampleName is guilty.'.",
        "Backpack": "See what's in your backpack (things you have taken).",
        
                    };

    ClearLine();
    
    print("Displaying help.");
    print("****************");
    
    ClearLine();
    
    print("Note: Enter the keywords below with your text to easily use them!");
    print("      Also, these keywords only work in INTERACTION MODE.");
    
    ClearLine();
    
    LoopList(HelpMessages, True);

# ------------------------------------------------------------------------------------------------------- #

# PlaySound
# A function to play sounds.
def PlaySound(SoundName):
    winsound.PlaySound('%s.wav' % SoundName, winsound.SND_ASYNC)
    
# ------------------------------------------------------------------------------------------------------- #


