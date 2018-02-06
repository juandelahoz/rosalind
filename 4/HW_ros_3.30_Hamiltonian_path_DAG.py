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
	print(edges)
	print(inc)
	print(out)

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
		print("---> ",hp)
		continue

	# build hamiltonian path
	print(first,final)
	path = [str(first)]
	sorted_edges = []
	prev = first
	print("path= "," ".join(path))
	for i in range(len(inc)):
		print("i = ", i)
		# get all outgoing nodes from previous
		outgoing = out[prev-1]
		# if there is only one outgoing node, go to that one
		if len(outgoing) == 1:
			print("outgo 1", outgoing)
			next_n = outgoing
			prev   = int(next_n[0])
			path.append(str(next_n[0]))
			print("path= "," ".join(path))
			continue
		# if there are more outgoing nodes...
		else:
			print("outgo 2", outgoing)
			# look at all of them
			for destination in outgoing:
				# if one of them has only one origin node, go there
				origin = inc[destination-1]
				if len(origin) == 1:
					print("origin 1",origin," - ", destination)
					next_n = destination
					prev   = next_n
					path.append(str(next_n))
					print("path= "," ".join(path))
					break
				else:
					print("origin 2",origin," - ", destination)
					all_on_path = True
					for orig in origin:
						print("c",orig,destination)
						if str(orig) not in path:
							all_on_path = False
							print("not in path",orig)
							break
					if all_on_path:
						next_n = destination
						prev   = next_n
						path.append(str(next_n))
						print("path= "," ".join(path))

		print("i = ", i)
	print(path)




	# print result:
	print("--> ",hp, " ".join(path))






