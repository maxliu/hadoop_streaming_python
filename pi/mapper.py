#! /usr/bin/env python
"""
This is the mapper function for pi estiation.

Xinyu Max liu <xinyulrsm@gmail.com>
12/2014
"""

import sys
from random import random


def get_ran(totalPoints=100):
    """
    generate a pairs of random number
    """
    for i in xrange(totalPoints):
        yield [random(), random()]


def mapper(totalPoints=100):
    coor = get_ran(totalPoints)
    countInCircle = sum([1 for x in coor if (x[0] * x[0] + x[1] * x[1] <= 1)])
    print "%d\t%f" % (1, 4 * float(countInCircle) / float(totalPoints))

if __name__ == "__main__":
    """
    read total points from command line
    for example:
    ./mapper.sh  100
    """
    totalPoints = int(sys.argv[1])
    mapper(totalPoints=totalPoints)
