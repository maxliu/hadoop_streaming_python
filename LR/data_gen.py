"""

"""

import sys
from random import random
import numpy as np
from math import exp
total = 10

filename = 'data.txt'

w = [0.1,-0.2,0.3,-0.4,0.5,-0.6,0.7,-0.8,0.9,-1.0,1.1]
n = len(w)

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

def g(x,w):
	return 1.0/(1.0+exp(-Sigma(x,w)))	

xarray = np.random.rand(total,n-1)


y = []
for x in xarray:
	y.append(g(x,w))
	print x


xy = np.zeros((total, n))

xy[:,-1] = y

xy[:,:-1] = xarray

with open(filename,'w') as f:
	np.savetxt(f,xy,fmt='%5.3f',delimiter=',')
		
	

