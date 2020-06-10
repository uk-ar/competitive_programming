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

N,Q = map(int,sys.stdin.readline().split())
COM = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(Q)) # multi line with multi param

parents = list(range(N))
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

for com,x,y in COM:
    if com == 0:
        union(x,y)
    else:
        if find(x) == find(y):
            print(1)
        else:
            print(0)
