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

    for wx , wv in groupby(key_values, lambda x: x[0]):
		try: 
			wxsum = sum(float(wvx) for _, wvx in wv) 
			print "%s\t%f" % (wx,wxsum)
		except valueError: 
			pass


if __name__ == '__main__':
    reducer()

