#! /usr/bin/env python
"""
This is the mapper function for word count.

Xinyu Max liu <xinyulrsm@gmail.com>
12/2014
"""
import sys


def get_input(source=sys.stdin, bad_chars='{},<>()[].'):
    """
    read lines from source (sys.stdin) and replace chars in bad_chars
    """
    for Ln in source:
        line = Ln
        if bad_chars is not None:
            for ch in bad_chars:
                line = line.replace(ch, '')
        yield line.split()


def mapper(source):
    """
    input "may jun july aug jun" will return
    may     1
    jun     2 # not 1
    july    1
    aug     1
    """
    for words in get_input(sys.stdin):
        for word in set(words):
            print '%s\t%d' % (word, words.count(word))

if __name__ == '__main__':
    mapper(sys.stdin)
