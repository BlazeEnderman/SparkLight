#!/usr/bin/python

##CREATED BY GRANT ALBERTS, 2017

import time
import re
import random

###ROOM VARIABLES###

health = 100
mana = 100

global rooms

rooms = {
            "hospEntrance" : {
                               "NORTH": {
                                        "DOOR" :
                                            {
                                           "locked" : True,
                                           "NORTH" : "ORB"
                                           },
                                        },
                               "EAST": "WALL",
                               "SOUTH": "WALL",
                               "WEST": "WALL",
                               "DESCRIPTION" : "The room is huge, with tall grey walls on every side. The only wall that wasn't completely featurelss was the north wall, which had a strange looking, inset, round door in it."
                            },
            "DOORWAY" : {
                            "NORTH": "DOOR",
                            "EAST" : "WALL",
                            "SOUTH" : "hospEntrance",
                            "WEST" : "WALL",
                            "DESCRIPTION" : "It's a short empty hall with no decor. If you were to reach your arms out, you could brush both of the walls. the round door looms ahead of you."
                        },
            "DOOR" : {
                        "locked" : True,
                        "NORTH" : "ORB"
                     }

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
def move(room ,dire):
    if room[dire] == "WALL":
        print "You walk into the wall"
        return
    else:
        curRoom = rooms[room[dire]]
        print curRoom["DESCRIPTION"]
        return curRoom

##END##

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
####HANDLER####
def caster():
    tes1 = raw_input("type?  ").upper()
    tes2 = raw_input("shape?  ").upper()
    print cast(test1, test2)
####END FUNCTION####

#####TOUCH FUNCTION#####




##start()
##
##print curRoom["DESCRIPTION"]
##
##dirs = raw_input("What direction do you want to go?   ")
##
##
##
##curRoom = move(curRoom, dirs.upper())
start()
