def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print"Man that's enough for a party!"
    print "Get a blanker.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)



print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese  + 100, amount_of_crackers + 1000)

def function(a,b)
    print "10/(a+1), 5*b" % (c, d)

function(1+4,1-0)


def function(a,b):
    print "10/(%s+1), 5*%d" % (a, b)

c = 20
d = 5

function(c+1+4,d*1-0)