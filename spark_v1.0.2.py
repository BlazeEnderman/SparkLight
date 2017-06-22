#!/usr/bin/python

##CREATED BY BLAZE ENDERMAN, 2017

import time
import re
import random

###ROOM VARIABLES###

health = 100
mana = 100
inventory = ["A small topaz Focus", "A skinnning knife, very sharp, not very deadly", "A dried ration of Fruit", "A dried stick of Jerkey", "A compass, a momento of your father's"]

global rooms
global curRoom

rooms = {
            "hospEntrance" : {
                               "NORTH": {
                                        "HALL" :
                                            {
                                           "locked" : True,
                                           "path" : "stangRoom",
                                           "unlock" : "touch"
                                           },
                                        },
                               "EAST": "WALL",
                               "SOUTH": "WALL",
                               "WEST": "WALL",
                               "DESCRIPTION" : "The room is huge, with tall grey walls on every side. The only wall that wasn't completely featurelss was the north wall, which had a strange looking, inset, round door in it."
                            },
            "stangRoom" : {
                           "NORTH": "WALL",
                           "EAST" : "WALL",
                           "SOUTH": "WALL",
                           "WEST" : "WALL",
                           "DESCRIPTION" : "The door slams shut behind you, sealing you in. The walls wer blank, white and featureless. the only thing that broke the monochrome was a single black orb sitting on a pedestal",
                           "INTACT" : {
                                        "ORB" : {
                                                    "path" : "recRoom",
                                                    "info" : "When you touch the orb, your body freezes, and hundreds of blue lines appear on the orb. The lines peeled off the orb and peirced your skin. While it didn't hurt, the feeling was not comfortable. It was like a bunch of works crawling under your skin. A harsh voice seemed to echo in your mind: \"Prime canidate found, beginning upgrade\" "
                                        },
                           },
            },

    }

curRoom = rooms["hospEntrance"]

######START UP#####
def start ():
    print "Welcome to my game, Spark. You are a human mage, exploring the riuns of an ancient civilization long lost to time The room you are standing in has no exits, save for a strange looking vault door, and a small hole in the ceiling." +" This game revolves around the user inputing commands to the game, and using the commands to do things inside the game. You will unlock powerful spells and have amazing encounters. Are you ready?"

    print " "

    time.sleep(2)

    yayNay = raw_input("y/n  ").upper()

    if yayNay == "Y":
        print "Let's go!"
        return
    else:
        print "Have a nice day!"
        exit()

#####END FUNCTION#####

#####ACTION FUCTIONS#####

##MOVE###
# def move(room ,dire):
#     if room[dire] == "WALL":
#         print "You walk into the wall"
#         return
#     else:
#         curRoom = rooms[room[dire]]
#         print curRoom["DESCRIPTION"]
#         return curRoom

def move(rrom, dire):
    check = rrom[dire]
    if "HALL" in check:
        print "IF HALL IS REAL"
        if check["HALL"]["locked"] == True:
            print "FIRST IF MOVE"
            return "The door is locked, you can't open it without first unlocking it."
        else:
            global curRoom
            curRoom = rooms[check["HALL"]["path"]]
            return True
    elif (check == "WALL"):
        print "ELIF what"
        return "Its a wall."
    else:
        rrom = rooms[rrom["HALL"]["path"]]
        print "MOVE ELSE"
        return True

##END##

###TOUCH###

def touch(rrom, dire):
    check = rrom[dire]
    if "HALL" in check:
        if "locked" in check["HALL"]:
            if check["HALL"]["locked"] == True:
                if check["HALL"]["unlock"] == "touch":
                    check["HALL"]["locked"] = False
                    return "You can hear a mechanism activating, and the door opens"
            else:
                return "You touch the door, for some reason"

##CAST##

def cast(tipe, shape):
    spec1 = tipe
    spec2 = shape
    while not ((spec1 == "FIRE") or (spec1 == "ICE") or (spec1 == "LIGHTNING") or (spec1 == "LIGHT") or (spec1 == "DARK")):
        redo = raw_input("That isn't a spuuported type, please use fire, ice, or lightning.  ")
        spec1 = redo.upper()
    while not ((spec2 == "BALL") or (spec2 == "ORB") or (spec2 == "SHARD") or (spec2 == "BLAST") or (spec2 == "AREA") or (spec2 == "BEAM")):
        redo = raw_input("Not supported, please use ball, orb, shard, blast, area or beam.   ")
        spec2 = redo.upper()
##    while not (spec3 == 0 or spec3 == "EXPLOSIVE" or spec3 == "LINGERING" or spec3 == "PENETRATING"):
##        redo = raw_input("please use a supported Modifier, like explosive, lingering, or penetrating, or input 0 if you don't want to use a modifier.    ")
##        spec3 = redo
    ###SPECAIL SPELLS###
    if (spec2 == "ORB" and spec1 == "LIGHT"):
        return "A small orb of light floats around your head"
    elif (spec2 == "BLAST" and spec1 == "LIGHT"):
        return "You squeeze your eyes shut and release a blinding, omnidirectional flash of white light!"
    ###GENERIC SPELLS###
    elif (spec2 == "BALL"):
        temp = "A ball of " + spec1.lower() + " shoots out of your hand!"
        return temp
    elif (spec2 == "ORB"):
        temp = "A orb of " + spec1.lower() + " floats above of you."
        return temp
    elif (spec2 == "SHARD"):
        temp = "A shard of " + spec1.lower() + " launches ahead of you at great velocity"
        return temp
    elif (spec2 == "BLAST"):
        temp = "A plume of " + spec1.lower() + " erupts in a directionless wave ahead of you! "
        return temp
    elif (spec2 == "AREA"):
        temp = "A five foot radius around you glows with the power of " + spec1.lower() + "!"
        return temp
    elif (spec2 == "BEAM"):
        temp = "A beam of " + spec2.lower() + " unfolds before you!"
        return temp
####END####

####HANDLER####
def caster():
    tes1 = raw_input("type?  ").upper()
    tes2 = raw_input("shape?  ").upper()
    print cast(tes1, tes2)
####END FUNCTION####

####inventory function####
def invent():
    for ind in inventory:
        print ind
####END####

##WALKER##
def walker():
    temp = raw_input("What direction?  ").upper()
    test = move(curRoom ,temp)
    if not (test == True):
        print "GTET HERE"
        print test
    else:
        print "Test"
        print curRoom["DESCRIPTION"]

##END##

##toucher##

def toucher():
    inp = raw_input("What direction? ").upper()
    temp = touch(curRoom, inp)
    print temp

###LOOK###

def look():
    print curRoom["DESCRIPTION"]

start()

#####MAIN LOOP#####

while (health >= 0):
    action = raw_input("What will you do?   ").lower()
    if ((action == "walk") or (action == "go")):
        walker()
    elif action == "touch":
        toucher()
    elif action == "cast":
        caster()
    elif ((action == "inventory") or (action == "inv") or (action == "i")):
        invent()
    elif action == "look":
        look()
    ##more actions to come later
    else:
        print "That is not an action you can do!"
