#! /usr/bin/env python
"""
12/2014
Xinyu Max liu 
xinyulrsm@gmail.com
"""

import sys


def get_input(source,bad_chars = '{},<>()[].'):
    for Ln in source:
	line = Ln
	if bad_chars is not None:
	    for ch in bad_chars:
	        line = line.replace(ch,' ' )
        yield line.split()

def mapper(source):
    for words in get_input(sys.stdin):
        for word in set(words):
	    print '%s\t%d'%(word, words.count(word))

if __name__ == '__main__':
    mapper(sys.stdin)
