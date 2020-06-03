#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")

import sys,collections,math
sys.setrecursionlimit(100000)

INF = float("inf")

N = int(sys.stdin.readline())
c = tuple(tuple(map(int,sys.stdin.readline().rstrip().split()))[1:] for _ in range(N)) # multi line with multi param
Q = int(sys.stdin.readline())
uv = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(Q)) # multi line with multi param
G = [list() for _ in range(N)]

for i,children in enumerate(c):
    G[i] = children
LN = math.floor(N**0.5)
depth = [0]*N
parents = [[0]*N for _ in range(LN)]
#print(parents,N,LN)
def dfs(v,p,l):
    parents[0][v] = p
    depth[v] = l
    for i in G[v]:
        if i != p:
            dfs(i,v,l+1)

dfs(0,-1,0)

for k in range(LN-1):#-1?
    for v in range(N):
        #print(k,v)
        if parents[k][v] < 0:
            parents[k+1][v] = -1
        else:
            parents[k+1][v] = parents[k][parents[k][v]]

def query(u,v):
    if depth[u] > depth[v]:
        u,v = v,u
    # print("d",depth[v]-depth[u])
    # l = int(math.log2(depth[v]-depth[u]))
    for k in range(l+1)[::-1]:
        #print(k,depth[u],depth[v],parents[k][v],depth[parents[k][v]])
        #if depth[u] != depth[v] and depth[u] <= depth[parents[k][v]]:
        if ((depth[v]-depth[u])>>k & 1):
            v = parents[k][v]
    # for _ in range(d):
    #     v = parents[0][v]
    assert(depth[u]==depth[v])
    #print(u,v)
    if u == v:
        return u
    # while v != u:
    #     v = parents[v]
    #     u = parents[u]
    for k in range(LN)[::-1]:
        if parents[k][v] != parents[k][u]:
            v = parents[k][v]
            u = parents[k][u]
    return parents[0][u]
#print(c,depth,parents)
ans = []
for u,v in uv:
    #print(u,v,depth[u],depth[v])
    ans.append(query(u,v))
sys.stdout.write("\n".join(map(str, ans)))
sys.stdout.write("\n")
    #            ((1, 2, 3),
 #      (4, 5, 6), (), (7, 8),
 # (), (9, 10), (14, 15), (), (),
 # (), (11, 12, 13), (), (), (), (), ())
