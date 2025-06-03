import heapq
import time  # Import the time module

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

graph = {
    '0': [('1', 4), ('2', 8)],
    '1': [('4', 6), ('0', 4)],
    '2': [('3', 2), ('0', 8)],
    '3': [('4', 10), ('2', 2)],
    '4': [('1', 6), ('3', 10)]
}

# Start timing
start_time = time.time()

# Run Dijkstra's algorithm
result = dijkstra(graph, '0')
print(result)

# End timing
end_time = time.time()

# Print execution time
print(f"Execution time: {end_time - start_time:.6f} seconds")

