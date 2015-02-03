#! /usr/bin/env python
"""
12/2014
Xinyu Max liu 
xinyulrsm@gmail.com
"""

import sys
from itertools import groupby

def get_mapper_key_values(source = sys.stdin):
    for line in source:
	yield line.split('\t',1)

def reducer(source = sys.stdin):
    key_values = get_mapper_key_values(source)

    for thisWord, g in groupby(key_values, lambda x: x[0]):
		try:
	    	thisCount = sum(int(count) for _, count in g)
	    	print "%s\t%d" % (thisWord,thisCount)
		except valueError:
	    	pass

def reducer_2(source = sys.stdin):
    key_values = get_mapper_key_values(source)
    [thisWord,thisCount] = next(key_values)
    [nextWord,nextCount] = next(key_values)
    while True:
	
		while thisWord == nextWord:
		    thisCount = int(thisCount) + int(nextCount)
	    	try:
            	[nextWord,nextCount] = next(key_values)
	    	except:
	        	print "%s\t%d" % (thisWord,int(thisCount))
	        return
		print "%s\t%d" % (thisWord,int(thisCount))
     
		[thisWord,thisCount] = [nextWord,nextCount]
        try:
	    	[nextWord,nextCount] = next(key_values)
		except:
	    	print "%s\t%d" % (thisWord,int(thisCount))
	    return

if __name__ == '__main__':
    reducer_2()

