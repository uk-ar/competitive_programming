#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n,m = map(int,sys.stdin.readline().split())
g = list(range(n))
def find(x):
  while g[x] != x:
    x = g[x]
    g[x] = g[g[x]]
  return x
def union(s,t):
  sp = find(s)
  tp = find(t)
  if sp == tp:
    pass
  elif sp < tp:
    g[sp] = tp
  else:
    g[tp] = sp
for i in range(m):
  s,t = map(int,sys.stdin.readline().split())
  union(s,t)

q = int(sys.stdin.readline())
for i in range(q):
  s,t = map(int,sys.stdin.readline().split())
  if find(s) == find(t):
    print("yes")
  else:
    print("no")
