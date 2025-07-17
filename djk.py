import heapq
import time

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        if curr_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = curr_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return dist

# Get input from user
graph = {}
nodes = set()

# Input number of edges
E = int(input("Enter number of edges: "))
print("Enter edges in the format: node1 node2 weight")

for _ in range(E):
    u, v, w = input().split()
    w = int(w)
    
    # Add nodes to set
    nodes.add(u)
    nodes.add(v)

    # Add edge to graph
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append((v, w))
    graph[v].append((u, w))  # For undirected graph

# Ensure all nodes have at least empty adjacency list
for node in nodes:
    if node not in graph:
        graph[node] = []

# Input the start node
start_node = input("Enter the start node: ")

# Run the algorithm and measure time
start_time = time.time()
result = dijkstra(graph, start_node)
end_time = time.time()

# Output the result
print("\nShortest distances from start node:")
for node in sorted(result):
    print(f"Node {node} : {result[node]}")

print(f"\nExecution time: {end_time - start_time:.6f} seconds")
