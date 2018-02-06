#!/Users/juan/anaconda/bin/python

import sys

inp = open(sys.argv[1],"r")
k = int(inp.readline().strip())

# iterate over graphs
for ik in range(k):
	# variables for each graph
	hp = -1
	edges = []
	m = -1
	# read one graph
	for line in inp:
		if line.startswith("\n"):
			continue
		a,b = map(int,line.strip().split())
		if m == -1:
			inc = []
			out = []
			for j in range(a):
				inc.append([])
				out.append([])
			end = b
		else:
			inc[b-1].append(a)
			out[a-1].append(b)
			edges.append((a,b))
		m += 1
		if m == end:
			break

	# test if hamiltonian path exists
	zeros = [0,0]
	for i in range(len(inc)):
		if len(inc[i]) == 0:
			zeros[0] += 1
			first = i+1
		if len(out[i]) == 0:
			zeros[1] += 1			
			final = i+1
	if zeros[0] == 1 and zeros[1] == 1:
		hp = 1
	else:
		print(hp)
		continue

	# build hamiltonian path
	path = [str(first)]
	prev = first
	for i in range(len(inc)):
		# get all outgoing nodes from previous
		outgoing = out[prev-1]
		# if there is only one outgoing node, go to that one
		if len(outgoing) == 1:
			prev = int(outgoing[0])
			path.append(str(outgoing[0]))
			continue
		# if there are more outgoing nodes...
		else:
			# look at each of them
			for destination in outgoing:
				origin = inc[destination-1]
				# if one of them has only one origin node, go there
				if len(origin) == 1:
					prev = destination
					path.append(str(destination))
					break
				# if one of them has multiple origins
				else:
					# check that all those origins are already on path
					all_on_path = True
					for orig in origin:
						# if one of its origins is not yet on path, stop
						if str(orig) not in path:
							all_on_path = False
							break
					# if all origins are already on path, add it to path
					if all_on_path:
						prev = destination
						path.append(str(destination))

	# print result:
	print(hp, " ".join(path))
