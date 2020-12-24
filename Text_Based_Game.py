#-*- mode: python -*-
# -*- coding: utf-8 -*-

from sys import exit

you_the_reader = True
life = True
death = False

#Introduction into the screenplay
def bus():
    print """You walk onto the little island in the middle of the infinity pool lining the oceans and mountains in the background. The mountains are surrounded by clouds. They’re
    literally above the clouds. It’s probably raining down there. There’s an orchard with lemon and plums to the west of the wall outside, and a green statue of a golfer further in.
    Bunnies jump on the lawn in the background."""
    print "Do you want to sit on the sun umbrella ?"

    choice = raw_input("> ");

    if "yes" is choice:
        umbrella()
    elif "no" is choice:
        start_again("This only works if you use the sun umbrella, sorry I didn't write the script.")

#The sun umbrella
def umbrella():
    print "You sit under a sun umbrella, opens the pop tart and starts to eat it. He looks off with his face flat. He gets a text message:"
    print "FAM: when u wanna paddle out? [PURPLE DEVIL FACE EMOJI]"
    print "You text back: pick me up"

    choice = raw_input("Press enter to continued: > ");
    if "" is choice:
        start_again()
