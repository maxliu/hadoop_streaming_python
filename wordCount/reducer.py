#! /usr/bin/env python
"""
This is the reducer function for word count.

Xinyu Max liu <xinyulrsm@gmail.com>
12/2014
"""

import sys
from itertools import groupby


def get_mapper_key_values(source=sys.stdin):
    for line in source:
        yield line.split('\t', 1)


def reducer(source=sys.stdin):
    """
    method-1 for word count.
    Because the key-value pairs are sorted by key in sys.stdin, we
    could use groupby.
    """
    key_values = get_mapper_key_values(source)

    for thisWord, g in groupby(key_values, lambda x: x[0]):
        try:
            thisCount = sum(int(count) for _, count in g)
            print "%s\t%d" % (thisWord, thisCount)
        except ValueError:
            pass


def reducer_2(source=sys.stdin):
    """
    method-2 without groupby.
    """
    key_values = get_mapper_key_values(source)
    [thisWord, thisCount] = next(key_values)
    [nextWord, nextCount] = next(key_values)
    while True:
        while thisWord == nextWord:
            thisCount = int(thisCount) + int(nextCount)
            try:
                [nextWord, nextCount] = next(key_values)
            except:
                print "%s\t%d" % (thisWord, int(thisCount))
                return
            print "%s\t%d" % (thisWord, int(thisCount))

        [thisWord, thisCount] = [nextWord, nextCount]
        try:
            [nextWord, nextCount] = next(key_values)
        except:
            print "%s\t%d" % (thisWord, int(thisCount))
        return

if __name__ == '__main__':
    reducer_2()
    # reducer()  # this also works
