#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# INF = float("inf")

import sys,collections
sys.setrecursionlimit(100000)
V,E = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
#sdw = [[src1 dist1 d1][src1 dist1 d1]...]# vect source1 -> distance1 distances
INF = float("inf")

st = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(E)) # multi line with multi param
#st = [[0,1],[0,2],[1,2],[2,3]]
G = [[] for _ in range(V)]

for s,t in st:
    G[s].append(t)
    G[t].append(s) #not directed

visited = set()
prenum = [0]*V
parent = [0]*V
lowest = [0]*V
timer = 0

def dfs(current,prev):
    global timer
    parent[current]=prev
    prenum[current]=lowest[current]=timer
    timer += 1
    visited.add(current)
    for nex in G[current]:
        if not nex in visited:
            dfs(nex,current)
            lowest[current]=min(lowest[current],lowest[nex])
        elif nex != prev:
            lowest[current]=min(lowest[current],prenum[nex])
dfs(0,-1)

ret = set()
if sum(1 for p in parent if p==0) > 1:
    ret.add(0)

for i in range(1,V):
    p = parent[i]
    if p != 0 and prenum[p] <= lowest[i]:
        ret.add(p)
ret = sorted(list(ret))
if ret:
    print(*ret,sep='\n')
