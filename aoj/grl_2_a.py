#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")

import sys,collections
sys.setrecursionlimit(10000)

INF = float("inf")

V,E = map(int,sys.stdin.readline().split())
stw = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(E)) # multi line with multi param

wst = [[w,s,t] for s,t,w in stw]
wst.sort()

parents = list(range(V))
def find(x):
  while parents[x] != x:
    x = parents[x]
    parents[x] = parents[parents[x]]
  return x

def union(s,t):
  sp = find(s)
  tp = find(t)
  if sp == tp:
    pass
  elif sp < tp:
    parents[sp] = tp
  else:
    parents[tp] = sp

INF = float("inf")
ret = 0
for w,s,t in wst:
    if find(s) != find(t):
        union(s,t)
        ret += w
print(ret)
