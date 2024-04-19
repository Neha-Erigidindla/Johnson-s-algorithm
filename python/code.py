import sys

# Number of vertices in the graph
V = 4

# A utility function to find the vertex with minimum distance value, from the set of
# vertices not yet included in shortest path tree


def minDistance(dist, sptSet):
	# Initialize min value
	min_val = sys.maxsize
	min_index = 0

	for v in range(V):
		if sptSet[v] == False and dist[v] <= min_val:
			min_val = dist[v]
			min_index = v

	return min_index

# A utility function to print the constructed distance array


def printSolution(dist):
	print("Following matrix shows the shortest distances between every pair of vertices")
	for i in range(V):
		for j in range(V):
			if dist[i][j] == sys.maxsize:
				print("{:>7s}".format("INF"), end="")
			else:
				print("{:>7d}".format(dist[i][j]), end="")
		print()

# Solves the all-pairs shortest path problem using Johnson's algorithm


def floydWarshall(graph):
	dist = [[0 for x in range(V)] for y in range(V)]

	# Initialize the solution matrix same as input graph matrix. Or we can say the initial
    # values of shortest distances are based on shortest paths considering no intermediate
    # vertex.
	for i in range(V):
		for j in range(V):
			dist[i][j] = graph[i][j]
	for k in range(V):
		# Pick all vertices as source one by one
		for i in range(V):
			# Pick all vertices as destination for the above picked source
			for j in range(V):
				# If vertex k is on the shortest path from
				# i to j, then update the value of dist[i][j]
				if dist[i][k] + dist[k][j] < dist[i][j]:
					dist[i][j] = dist[i][k] + dist[k][j]

	# Print the shortest distance matrix
	printSolution(dist)


# driver program to test above function
if __name__ == "__main__":



	graph = [[0, 5, sys.maxsize, 10],
			[sys.maxsize, 0, 3, sys.maxsize],
			[sys.maxsize, sys.maxsize, 0, 1],
			[sys.maxsize, sys.maxsize, sys.maxsize, 0]
			]

	# Print the solution
	floydWarshall(graph)

