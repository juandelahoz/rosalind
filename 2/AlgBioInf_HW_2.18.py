#!/usr/bin/python

import sys

file = open(sys.argv[1], 'r')
seqs = file.readlines().strip()

print(seqs)
