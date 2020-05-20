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
ret = []

for i in range(1,V):
    p = parent[i]
    if prenum[p] < lowest[i]:
        if p < i:
            ret.append([p,i])
        else:
            ret.append([i,p])
ret = sorted(list(ret))

for s,t in ret:
    print(s,t)
