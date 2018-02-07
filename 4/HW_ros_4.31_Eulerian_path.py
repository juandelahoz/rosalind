#!/Users/juan/anaconda/bin/python

import sys

inp = open(sys.argv[1],"r")

# variables for graph
edges = []
n_nodes = 0
# read file
for line in inp:
	a,b = map(str,line.strip().split(" -> "))
	if "," in b:
		b = b.split(",")
		for bi in b:
			edges.append((int(a),int(bi)))
			n_nodes = max(n_nodes, int(a))
			n_nodes = max(n_nodes, int(bi))
	else:
		edges.append((int(a),int(b)))
		n_nodes = max(n_nodes, int(a))
		n_nodes = max(n_nodes, int(b))

# find start and end:
balance = [0] * n_nodes
for edge in edges:
	balance[edge[0]-1] -= 1
	balance[edge[1]-1] += 1
for i in range(len(balance)):
	if balance[i] == -1:
		start = i+1
	if balance[i] ==  1:
		end   = i+1

# functions to work 
def other_path(eds,curr):
	for i in eds:
		if curr == i[0]:
			return True
	return False
	
def find_next(eds,curr):
	next_node = -1
	for i in eds:
		if curr == i[0]:
			next_node = i[1]
			eds.remove(i)
			return eds, next_node
	return eds, -1

# build Eulerian path
path = []
stack = []
current = start
exit = True # starting edge has an exit!

while len(edges) >0:
	# find an edge with an exit
	while not exit:
		path.append(current)
		current = stack[-1]
		stack.pop(-1)
		exit = other_path(edges,current)
	# go through graph until getting stuck
	stuck = False
	while not stuck:
		# what is the next node?
		edges, next_node = find_next(edges,current)
		if next_node == -1:
			stuck = True
			exit = False
		else:
			stack.append(int(current))
			current = int(next_node)

# finally, get the remaining stack
stack.append(current)
for i in range(len(stack)-1,-1,-1):
	path.append(stack[i])
# and reverse path
path.reverse()

# print result:
print("->".join(map(str,path)))
