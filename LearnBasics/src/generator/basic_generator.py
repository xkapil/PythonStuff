import random, types

def lottery():
    # returns 6 numbers between 1 and 40
    for i in xrange(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

if type(lottery()) == types.GeneratorType:
    print 'Good, random is generator'

for random_number in lottery():
    print "And the next number is... %d!" % random_number

