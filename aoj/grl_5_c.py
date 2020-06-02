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

N = int(sys.stdin.readline())
c = tuple(tuple(map(int,sys.stdin.readline().rstrip().split()))[1:] for _ in range(N)) # multi line with multi param
Q = int(sys.stdin.readline())
uv = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(Q)) # multi line with multi param
tree = {}
for i,children in enumerate(c):
    tree[i] = children

levels = {}
parents = {}
def dfs(v,l,p):
    levels[v] = l
    parents[v] = p
    for i in tree[v]:
        dfs(i,l+1,v)

dfs(0,0,0)
#print(c,levels,parents)
#print(c,levels,parents)
for u,v in uv:
    #print(u,v,levels[u],levels[v])
    if levels[u] > levels[v]:
        u,v = v,u
    d = levels[v]-levels[u]
    for _ in range(d):
        v = parents[v]
    #print(u,v)
    while v != u:
        v = parents[v]
        u = parents[u]
    print(u)
 #            ((1, 2, 3),
 #      (4, 5, 6), (), (7, 8),
 # (), (9, 10), (14, 15), (), (),
 # (), (11, 12, 13), (), (), (), (), ())
