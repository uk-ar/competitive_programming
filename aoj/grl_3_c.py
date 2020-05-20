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

V,E = map(int,sys.stdin.readline().split())
st = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(E)) # multi line with multi param
Q = int(sys.stdin.readline())
uv = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(Q)) # multi line with multi param
#st = [[0,1],[0,2],[1,2],[2,3]]
#uv = [[0,1],[0,2],[1,2],[2,3]]
G = {i:[] for i in range(V)}
rG = {i:[] for i in range(V)}

for s,t in st:
    G[s].append(t)
    rG[t].append(s)

def dfs(current):
    visited.add(current)
    for nex in G[current]:
        if not nex in visited: dfs(nex)
    post_order.append(current)

def rdfs(current,k):
    visited.add(current)
    topological_order[current]=k
    for nex in rG[current]:
        if not nex in visited: rdfs(nex,k)

visited = set()
post_order = []
for i in range(V):
    if not i in visited: dfs(i)

topological_order = [0]*V
visited = set()

k = 0
for i in post_order[::-1]:
    if not i in visited:
        rdfs(i,k)
        k += 1

for u,v in uv:
    if topological_order[u] == topological_order[v]:
        print(1)
    else:
        print(0)
