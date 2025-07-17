import time

n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

g = [[0] * n for _ in range(n)]

print("Enter each edge as: from_node to_node capacity")
for _ in range(m):
    u, v, c = map(int, input().split())
    g[u][v] = c  

s = int(input("Enter source node: "))
t = int(input("Enter sink node: "))

start = time.time()

def dfs(u, t, flow, visited):
    if u == t:
        return flow
    visited[u] = True
    for v in range(n):
        if not visited[v] and g[u][v] > 0:
            curr_flow = min(flow, g[u][v])
            temp_flow = dfs(v, t, curr_flow, visited)
            if temp_flow > 0:
                g[u][v] -= temp_flow
                g[v][u] += temp_flow
                return temp_flow
    return 0

def ford_fulkerson(s, t):
    flow = 0
    while True:
        visited = [False] * n
        increment = dfs(s, t, float('inf'), visited)
        if increment == 0:
            break
        print(f"Path found → Flow added: {increment}")
        flow += increment
    return flow

max_flow = ford_fulkerson(s, t)
print("Max Flow:", max_flow)
print("Execution Time: %.6f seconds" % (time.time() - start))
