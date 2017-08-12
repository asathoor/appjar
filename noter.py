# import the library
from appJar import gui
# create a GUI variable called app
app = gui()

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "My first Apphar")
app.setLabelBg("title", "green")

# start the GUI
app.go()
