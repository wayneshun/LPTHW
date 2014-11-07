#This is my first game.
#It may full of mistakes and errors,but it can work.
#It is a adventure game.

def death():
	print "You are dead!"
def good():
	print "You live a happy life forever!"


def tigerroom():
	print "Now you are in front of a huge tiger,what do you do?"
	you_do = raw_input(">")
	if "beat" in you_do:
		print "poor person",
		death()
	elif "run" in you_do:
		print "smart boy"
		good()



def east():
	print "choose your next step:left or right?"
	choose =raw_input(">")
	if choose == "left":
		print "Congralations! You enter into the goldenroom.You will be rich enough!"
		return good()
	elif choose == "right":
		print "Danger! You enter into the bearroom.Watch out the bear!"
		print "enter a number and see if you are lucky!"
		num = raw_input(">")
		if num == "5":
			return good()
		else:
			return death()
	else:
		return death()



def west():
	choose = raw_input("welcome to the west,enter your choice : left or right ?")
	if choose == "left":
		print "now you are in the tigerroom"
		tigerroom()


def direction():
	print "choose your direction"
	choose = raw_input(">")
	if choose == "east":
		east()
	elif choose == "west":
		west()
	elif choose == "south":
		south()
	elif choose == "north":
		north()
	else:
		death()

direction()
