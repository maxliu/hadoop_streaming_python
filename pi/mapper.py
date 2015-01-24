#! /usr/bin/env python
"""

"""

import sys
from random import random

def get_ran(totalPoints = 100):
	for i in xrange(totalPoints):
		yield [random(),random()]

def mapper(totalPoints = 100):

	coor = get_ran(totalPoints)
	countInCircle = sum([1 for x in coor if (x[0]*x[0]+x[1]*x[1]<=1) ])
	print 4*float(countInCircle )/float(totalPoints)

if __name__ == "__main__":
	totalPoints = int(sys.argv[1])
	mapper(totalPoints = totalPoints)
