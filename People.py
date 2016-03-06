# By PowerHotmail
# The Mental Murderer
# People Module
# Holds people to be used within this game.

# ------------------------------------------------------------------------------------------------------- #

# Importing
import random;

# ------------------------------------------------------------------------------------------------------- #

# Modules

# ------------------------------------------------------------------------------------------------------- #

# Suspicous People
# People who are suspicous of being the murderer.
SuspicousPeople = {

    "Rebecca":  [],
    "James":    [],
    "Kate":     [],
    "Linda":    [],
    "Rob":      [],
    "Lyndsy":   [],

                    };

# ------------------------------------------------------------------------------------------------------- #

# Innocent People
# People who are used for different items.
InnocentPeople = [

    "George",
    "Jake",
    "Usain",
    "Morah",
    "Vicky",
    "Samuel",

                    ];

# ------------------------------------------------------------------------------------------------------- #

# ChooseRandomInnocent
# A function to return a random innocent.
def ChooseRandomInnocent():
    return random.choice(InnocentPeople);

# ------------------------------------------------------------------------------------------------------- #

# ChosenMurderer
# A variable for holding the chosen murderer.
ChosenMurderer = random.choice(list(SuspicousPeople.keys()));

# ------------------------------------------------------------------------------------------------------- #
