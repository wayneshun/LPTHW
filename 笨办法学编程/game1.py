import random
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
choices = ['rock', 'Spock', 'paper', 'lizard', 'scissors']
#def number_to_name(number):
#    """
#	Converts the given number to name
#    """
#    return choices[number]
    
def name_to_number(name):
    """
	Converts the given name to number
    """
    return [i for i, x in enumerate(choices) if x == name][0]


def rpsls(name): 
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # get a random choice from the list. this will return a name
    comp_name = random.choice(choices)
    # convert name to comp_number using name_to_number
    comp_number = name_to_number(comp_name)
    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number) % 5
    # use if/elif/else to determine winner
    if difference in [1, 2]:
        winmsg = "Player wins!"
    elif difference == 0:
        winmsg = "Player and computer tie!"
    else:
        winmsg = "Computer wins!"
    # print results
    print " "
    print "Player chooses " + str(name)
    print "Computer chooses " + str(comp_name)
    print winmsg
    
# test code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")