# By PowerHotmail
# The Mental Murderer
# Rooms Module
# Holding all the information for rooms.

# ------------------------------------------------------------------------------------------------------- #

# Importing
import threading

# ------------------------------------------------------------------------------------------------------- #

# Modules
from People import *

# ------------------------------------------------------------------------------------------------------- #

# Rooms
# All the rooms in the game, with items.
Rooms = {};

Rooms["G-English-2"] = {

    "Pen":   "There are a few pens on the floor.",
    "Ruler": "There is a ruler shaped like a knife.",
    "Blood": "There is some blood on a book.",
    
                        };

Rooms["G-English-3"] = {

    "Gun":    "There is a gun on the table.",
    "Laptop": "There is a laptop, with a tad of blood.",

                        };

Rooms["G-English-4"] = {

    "Case": "There is a pencil case on the chair.",
    "Bottle": "There is a bottle which is neary full.",

                        };

Rooms["G-English-5"] = {

    "Glasses": "There are some broken glasses in the corner.",
    "Flashlight": "There seems to be a flashlight on the table.",
    "Photo": "There is a photo covered with something.",
    
                        };

# ------------------------------------------------------------------------------------------------------- #

# RoomInteraction
# All the rooms in the game, with interaction.
RoomInteraction = {};

# ------------------------------------------------------------------------------------------------------- #

# G-English-2
RoomInteraction["G-English-2"] = {};

RoomInteraction["G-English-2"]["Pen"] = {

    "Analyse":     "These pens are owned by " + ChosenMurderer + ".",
    "Take":        None,
    "Use":         "The ink is red... The ink is not ink, it is blood.",
    "Fingerprint": "The freshest fingerprints belong to " + ChosenMurderer + ".",
    
                                };

RoomInteraction["G-English-2"]["Ruler"] = {

    "Analyse":     "This ruler belongs to " + ChooseRandomInnocent() + ". It has been carved into a knife-like shape.",
    "Take":        None,
    "Use":         "You have made yourself get a small cut; with more force, this could be deadly.",
    "Fingerprint": "The freshest fingerprints belong to " + ChosenMurderer + ".",

                                    };

RoomInteraction["G-English-2"]["Blood"] = {

    "Analyse": "This blood is fresh - around 5-10 minutes old.",
    "Taste":   "It is very warm and very sweet. Interesting...",

                                    };

# ------------------------------------------------------------------------------------------------------- #

# G-English-3
RoomInteraction["G-English-3"] = {};
        
RoomInteraction["G-English-3"]["Gun"] = {
    
    "Analyse":     "This gun looks illegal and unlicensed.",
    "Take":        None,
    "Use":         None,
    "Fingerprint": "The fingerprints belong to " + ChosenMurderer + ".",

                                };
    
RoomInteraction["G-English-3"]["Laptop"] = {

    "Analyse": "This laptop belongs to " + ChooseRandomInnocent() + ". It has been running for the past hour.",
    "Use":     None,

                                    };

# ------------------------------------------------------------------------------------------------------- #

# G-English-4
RoomInteraction["G-English-4"] = {};

RoomInteraction["G-English-4"]["Case"] = {

    "Analyse": "This pencil case belongs to " + ChooseRandomInnocent() + ". Inside it is a pocket knife, with blood.",
    "Take":    None,

                                    };

RoomInteraction["G-English-4"]["Bottle"] = {

    "Analyse": "This bottle belongs to " + ChosenMurderer + ". Not too much of its contents has been drank.",
    "Drink": "That was refreshing...",

                                    };

# ------------------------------------------------------------------------------------------------------- #

# G-English-5
RoomInteraction["G-English-5"] = {};

RoomInteraction["G-English-5"]["Glasses"] = {

    "Analyse": "These glasses belong to " + ChooseRandomInnocent() + ". They have been cracked by something.",
    "Take":    None,
                                    };

RoomInteraction["G-English-5"]["Flashlight"] = {

    "Analyse": "This flashlight looks like it belongs to a surgeon.",
    "Use": "It doesn't work properly. The light keeps flickering...",
    "Fingerprint": "The fingerprints belong to " + ChooseRandomInnocent() + ".",

                                    };

RoomInteraction["G-English-5"]["Photo"] = {

    "Analyse": "This is a photo of " + ChooseRandomInnocent() + ". Their face has been covered by blood.",
    "Take": None,

                                    };
# ------------------------------------------------------------------------------------------------------- #
