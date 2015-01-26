#! /usr/bin/env python
"""

"""

import sys

def get_mapper_values():
	for line in sys.stdin:
		vs = line.split('\t',1)[1]
		yield float(vs)

def reducer():
	mv = get_mapper_values()
	sumVal = 0
	totalCount = 0
	for v in mv:
		sumVal += v
		totalCount +=1
    
	
	print sumVal /float(totalCount)
if __name__ == "__main__":
	reducer()
