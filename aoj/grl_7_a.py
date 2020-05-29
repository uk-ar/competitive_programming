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

X,Y,E = map(int,sys.stdin.readline().split())
xy = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(E)) # multi line with multi param
#uvc = [[0,1,1],[0,2,3],[1,2,1],[2,3,2]]
#xy = [[0,0],[1,2],[2,2],[1,3]]
V = X+Y+2
uvc = [[x+1,y+X+1,1] for x,y in xy]
for i in range(X):
    uvc.append([0,i+1,1])
for i in range(Y):
    uvc.append([X+i+1,V-1,1])
G = {i:{} for i in range(V)}
mG = {i:{} for i in range(V)}

for u,v,c in uvc:
    G[u][v] = c
    G[v][u] = 0 # reverse edge
    mG[u][v] = 0
    mG[v][u] = 0
# print(G)
# print(mG)
def dfs(current,flow):
    if current == V-1:
        return flow
    visited.add(current)
    for nex,nex_c in G[current].items():
        if not nex in visited and nex_c != 0:
            f = dfs(nex,min(flow,nex_c))
            if f != 0:
                mG[current][nex] = mG[current][nex] + f
                G[current][nex] = G[current][nex] - f
                G[nex][current] = G[nex][current] + f
                return f
    return 0

visited = set()
while dfs(0,INF) != 0:
    visited = set()
    pass
print(sum(mG[0].values()))
