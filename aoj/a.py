#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")

import sys,collections,math
sys.setrecursionlimit(1000000)

INF = float("inf")

N = int(sys.stdin.readline())
c = tuple(tuple(map(int,sys.stdin.readline().rstrip().split()))[1:] for _ in range(N)) # multi line with multi param
Q = int(sys.stdin.readline())
uv = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(Q)) # multi line with multi param
G = [list() for _ in range(N)]

for i,children in enumerate(c):
    G[i] = children
LN = 20#math.floor(N**0.5)
depth = [0]*N
parents = [[0]*N for _ in range(LN)]

def dfs(v,p,l):
    parents[0][v] = p
    depth[v] = l
    for i in G[v]:
        if i != p:
            dfs(i,v,l+1)

dfs(0,-1,0)

for k in range(LN-1):#-1?
    for v in range(N):
        if parents[k][v] < 0:
            parents[k+1][v] = -1
        else:
            parents[k+1][v] = parents[k][parents[k][v]]

def query(u,v):
    if depth[u] > depth[v]:
        u,v = v,u
    while depth[v] != depth[u]:
        v = parents[int(math.log2(depth[v]-depth[u]))][v]
    # for k in range(LN)[::-1]:
    #     if ((depth[v]-depth[u])>>k & 1):
    #         v = parents[k][v]
    assert(depth[u]==depth[v])
    if u == v:
        return u
    for k in range(LN)[::-1]:
        if parents[k][v] != parents[k][u]:
            v = parents[k][v]
            u = parents[k][u]
    return parents[0][u]

ans = []
for u,v in uv:
    print(query(u,v))
