#!/Users/juan/anaconda/bin/python

import sys

inp = open(sys.argv[1],"r")

# variables for graph
edges = []

# read file
for line in inp:
	a,b = map(str,line.strip().split(" -> "))
	edges.append((a,b))

# build Eulerian path
#path = [str(first)]

# print result:
#print(" ".join(path))
print(edges)
