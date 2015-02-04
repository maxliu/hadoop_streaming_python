#! /usr/bin/env python
"""
This is the reducer function for pi estimation.

Xinyu Max liu <xinyulrsm@gmail.com>
12/2014
"""

import sys


def get_mapper_values():
    """
    read resutls from mapper only return the value
    """
    for line in sys.stdin:
        vs = line.split('\t', 1)[1]
        yield float(vs)


def reducer():
    """
    sum all the value and calculate the probality : pi
    """
    mv = get_mapper_values()
    sumVal = 0
    totalCount = 0
    for v in mv:
        sumVal += v
        totalCount += 1
    print sumVal / float(totalCount)


if __name__ == "__main__":
    reducer()
