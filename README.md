# Johnson's Algorithm

Johnson's Algorithm is a method for finding all-pairs shortest paths in a weighted graph with positive and negative edge weights. It works by transforming the original graph using the Bellman-Ford algorithm to remove negative edge weights, then applying a modified version of the Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices.

# Algorithm
1. Add a new vertex to the graph and connect it to all existing vertices with zero-weight edges.
2. Run the Bellman-Ford algorithm on the modified graph to find the shortest path from the new vertex to all other vertices. If a negative cycle is detected, stop (as no solution exists).
3. Recalculate the edge weights using the Bellman-Ford results to remove negative weights.
4. Apply a modified version of the Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices.

# Complexity
Time Complexity:
- The main steps in the algorithm are the Bellman-Ford Algorithm called once and Dijkstra called V times. The time complexity of Bellman-Ford is O(VE) and the time 
complexity of Dijkstra is O(VLogV). So, the overall time complexity is O(V2log V + VE). 
- Best Case: O(V^3) if the graph has no negative edges and the modified Floyd-Warshall algorithm can be optimized.
- Worst Case: O(V^3) if the graph contains negative edges and the Bellman-Ford algorithm is required.
Space Complexity: O(V^2) for the distance matrix and O(V) for other data structures.

# Applications
- Network Routing: Johnson's algorithm is used in network routing protocols to find the shortest paths between routers.
- Traffic Engineering: It helps optimize traffic flow by finding the most efficient routes.
- Game Theory: Johnson's algorithm can be applied in game theory for analyzing strategic interactions between players.

# Note
Johnson's algorithm is primarily used for sparse graphs due to its time complexity. Other algorithms such as the Floyd-Warshall algorithm may be more suitable for dense graphs.
