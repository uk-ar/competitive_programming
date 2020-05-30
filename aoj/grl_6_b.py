#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")

import sys,collections
sys.setrecursionlimit(100000)

INF = float("inf")

V,E,F = map(int,sys.stdin.readline().split())
uvcd = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(E)) # multi line with multi param

#uvcd = [[0,1,1,1],[0,2,3,2],[1,2,1,2],[2,3,2,1]]
capacityG = {i:{} for i in range(V)} #capacity
costG = {i:{} for i in range(V)} #capacity

for u,v,c,d in uvcd:
    capacityG[u][v] = c
    costG[u][v] = d
    if not u in capacityG[v]:
        capacityG[v][u] = 0
        costG[v][u] = -d

def shortest_path(V,costG,capacityG,start=0):
    distances = [INF]*V
    distances[start] = 0
    parents = list(range(V))

    for _ in range(V):
        modified = False
        for src in range(V):
            if distances[src] == INF: continue
            for dst,cost in costG[src].items():
                if capacityG[src][dst] > 0 and distances[dst] > distances[src] + cost:
                    distances[dst] = distances[src] + cost
                    parents[dst] = src
                    modified = True
        if modified == False:
            return distances,parents
    return None,None

rest = F
total_cost = 0
while rest != 0:
    distances,p = shortest_path(V,costG,capacityG,0)
    if not distances or distances[V-1] == INF:
        print(-1)
        exit()
    cur = V-1
    flow = rest
    while cur != 0:
        flow = min(flow,capacityG[p[cur]][cur])
        cur = p[cur]
    rest -= flow
    total_cost += distances[V-1]*flow
    cur = V-1
    while cur != 0:
        capacityG[p[cur]][cur] -= flow
        capacityG[cur][p[cur]] += flow #rev
        cur = p[cur]
print(total_cost)
