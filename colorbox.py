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

app = gui("Colorbox Test")
app.addLabel("title", "G810 Led Keyboard")

color = app.colourBox(colour="#00FF00")

# omit the hash before the color (substring)
print "You selected the color: " + color[1:]

app.go() # loop
