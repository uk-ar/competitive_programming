#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# INF = float("inf")

import sys,collections
sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())
#sdw = [[src1 dist1 d1][src1 dist1 d1]...]# vect source1 -> distance1 distances
INF = float("inf")

stw = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N-1)) # multi line with multi param
#stw = [[0,1,2],[1,2,1],[1,3,3]]
G = [{} for _ in range(N)]

for s,t,w in stw:
    G[s][t] = w
    G[t][s] = w
distance = [0]*N
ret = 0

def dfs(c,w,visited):
    if c in visited:
        return
    distance[c] = w
    visited.add(c)
    for to,dw in G[c].items():
        dfs(to,w+dw,visited)

dfs(0,0,set())
i = distance.index(max(distance))
dfs(i,0,set())

print(max(distance))
