#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections

N,M = map(int,sys.stdin.readline().split())
ab = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(M)) # multi line with multi param

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

for a,b in ab:
    union(a-1,b-1)
import collections
d = collections.defaultdict(int)
m = 0
for i in range(N):
    x = find(i)
    d[x] += 1
    m = max(m,d[x])
print(m)
