# import the library
from appJar import gui

# create gui
win = gui("Hello")
win.setBg("green")
win.setFont(24)

win.setGeometry("500x400")
win.setResizable(False)

win.addLabel("L1","Hello, hello!")
win.addLabel("L2","Hello, goodbye!")
win.addLabel("L3","Goodbye, hello!")
win.addLabel("L4","Hello, hello!")

def press ( name ):
	print(name, "Button Pressed")

	if name == "Cancel":
		win.stop()
	elif name == "Reset":
		win.clearEntry("Username")
		win.clearEntry("Password")
		win.setFocus("Username")
	elif name == "Submit":
		username = win.getEntry("Username")
		password = win.getEntry("Password")

	if username == "per" and password == "ostemad":
		win.infoBox("Success","Valid Password")
	else:
		win.errorBox("Begone Oh Evil Thing","Never come back!")

win.addButton("Press me", press)

win.addLabelEntry("Username")
win.setLabelFg("Username","white")

win.addSecretLabelEntry("Password")
win.setLabelFg("Password","white")

win.addButtons(["Submit","Reset","Cancel"],press)

win.setLabelBg("L3","orange")
win.go()
