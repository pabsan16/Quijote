# -*- coding: utf-8 -*-
"""
PABLO SÁNCHEZ RICO
"""

import random
import sys

#infilename = 'quijote.txt'
#outfilename = 'quijote_s05.txt'
#0 < ratio < 1

def main(infilename, outfilename, ratio):
    with open(infilename) as infile:
        with open(outfilename, 'w') as outfile:
            for line in infile:
                if random.random()<=ratio:
                    outfile.write(line)

if __name__=="__main__":
    if len(sys.argv)<4:
        print(f"Usage: {sys.argv[0]} <infilename> <outfilename> <ratio")
        exit(1)
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    ratio = float(sys.argv[3])
    main(infilename, outfilename, ratio)