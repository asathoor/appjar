#!/usr/bin/env python
# -*- coding: utf-8 -*-

# file: tastatur.py
# purpose: a GUI for g810-led
# by: per thykjaer jensen
# license: GPLv3

# DEPENDENCIES
# appjar
# g810-led: https://github.com/MatMoul/g810-led

from appJar import gui # appjar
import subprocess as sub # os commands
import signal

app = gui("G810-led")
app.addLabel("title", "G810 Led Keyboard")
app.setLabelBg("title", "orange")

'''
Button Actions
'''
def btnClick( btn ):
    if btn == "All":
        color = app.colourBox(colour="#00FF00")
        # the pop up will return the hex with a hash
        # I need a substring, so:
        # print color[1:]
        setKbd = sub.call( [ "g810-led", "-a", color[1:] ] )
    elif btn == "Key":
        color = app.colourBox(colour="#00FF00")
        key = app.getEntry("key")
        setKbd = sub.call( [ "g810-led", "-k", key, color[1:] ] )
    elif btn == "Set Keygroup Color":
        print "Keygroup pressed."
        print(app.getOptionBox("Select Keygroup"))
        # get the value from the keygroup option labels
        keygroup = app.getOptionBox("Select Keygroup")
        color = app.colourBox(colour="#00FF00")
        setKbd = sub.call( [ "g810-led", "-g", keygroup, color[1:] ] )
    elif btn == "Cancel":
        app.stop()
    elif btn == "Hwave":
        theWave = sub.call( [ "g810-led", "-fx", "hwave", "all", "ff"] )
    elif btn == "Cwave":
        theWave = sub.call( [ "g810-led", "-fx", "cwave", "all", "ff"] )

        
'''
Button Panel
'''
app.addLabel("keyName")
app.addLabelEntry("key")

'''
Optionbox: keygroups
'''
keygroup = app.addLabelOptionBox("Select Keygroup", ["- Group List -",
                                                     "logo",
                                                     "indicators",
                                                     "fkeys",
                                                     "modifiers",
                                                     "multimedia",
                                                     "arrows",
                                                     "numeric",
                                                     "functions",
                                                     "keys",
                                                     "- Group logo -",
                                                     "logo"                                                     
                                                     ])

app.addButtons(["All","Key","Set Keygroup Color","Hwave","Cwave","Cancel"],btnClick)

app.go() # loop
