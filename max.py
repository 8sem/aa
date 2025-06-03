import time

start = time.time()

n = 4
g = [[0]*n for _ in range(n)]
for u, v, c in [(0,1,3),(0,2,2),(1,3,2),(1,2,5),(2,3,3)]:
    g[u][v] = c

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
        visited = [False]*n
        increment = dfs(s, t, float('inf'), visited)
        if increment == 0:
            break
        flow += increment
    return flow

print("Max Flow:", ford_fulkerson(0, 3))
print("Time: %.6f seconds" % (time.time() - start))

