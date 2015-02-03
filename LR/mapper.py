#! /usr/bin/env python
"""

"""

import sys
from math import exp

# TODO add try-expect for if argv can be coverted to float

def Sigma(x,w):
	"""
		return = w[0]+w[1]*x[0]+w[2]*x[1]+...
	"""
	# TODO define errors if len(x) != len(w)
	sum = 0;
	for i, wn in enumerate(w[1:]):
		sum = sum + wn * x[i]
	sum = sum + w[0]
	return sum
def g(x):
	return 1.0/(1.0+exp(-x))	

def get_input(source):
    for Ln in source:
		line = Ln 
		val = map(float, line.split(',')) 
		yield val
def mapper(source):
	w = []
	for arg in sys.argv[1:]:
		w.append(float(arg))

	for val in get_input(source):
		x = val[:-1]
		y = val[-1]
		s = Sigma(x, w)
		gs = y * g(-y * Sigma(x,w))
		print '%d\t%f'%(0,gs)
		for i, wk in enumerate(w[1:]):
			wx = 'w'+str(i+1)
			print '%d\t%f'%(i+1, x[i]*gs)

if __name__ == '__main__':
    mapper(sys.stdin)
		
