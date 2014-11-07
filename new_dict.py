ab = {       
             'Swaroop'   : 'swaroopch@byteofpython.info',
             'Larry'     : 'larry@wall.org',
             'Matsumoto' : 'matz@ruby-lang.org',
             'Spammer'   : 'spammer@hotmail.com'
     }

print "Swaroop's address is %s" % ab['Swaroop']

ab['Guido'] = 'guido@python.org'

print ab

del ab['Spammer']

print ab

print "There are %d contacts in the address book." % len(ab)

for name,address in ab.items():
	print 'Contact %s at %s' % (name,address)

print ab.items()


