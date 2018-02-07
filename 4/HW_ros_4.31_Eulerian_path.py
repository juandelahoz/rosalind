#!/Users/juan/anaconda/bin/python

import sys

inp = open(sys.argv[1],"r")

# variables for graph
edges = []
in_out = []
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

while len(edges) >1:
	print(edges,stack)
	print(path)
	stuck = False
	while not stuck:
		print("a",current)
		print(edges,stack)

		edges, next_node = find_next(edges,current)
		
		print(edges, current, next_node)
		if next_node == -1:
			stuck = True
			exit = False
		else:
			stack.append(int(current))
			current = int(next_node)
		print("b",current,stuck, stack)
		print("-----------------------")
	# go back to some edge with other exit
	print(path)

	if len(edges) > 0:
		while not exit:
			print("c",current)
			print(edges,stack)
			path.append(current)
			current = stack[-1]
			stack.pop(-1)
			exit = other_path(edges,current)
			print(path)
			print("d",current, exit)
			print(".-.-.-.-.-.-.-.-.-.-.-.-")
	else:
		while len(stack) > 0:
			print("e",current)
			print(edges,stack)
			path.append(current)
			current = stack[-1]
			stack.pop(-1)
			print(path)
			print("f",current)
			print("...-...-...-...-...-...-...")

path.append(current)
path.reverse()
# print result:
print(" ".join(map(str,path)))
print(edges)
