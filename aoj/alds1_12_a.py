#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n = int(sys.stdin.readline())
M = [list(map(int,l.split())) for l in sys.stdin.readlines()]

color = set()
d = [float("inf")]*n
d[0]=0
p = [-1]*n
#print(M)
while len(color) < n:
  u = -1
  for i in range(n):
    if not i in color and (u == -1 or d[u] > d[i]):
      u = i
  color.add(u)
  for v in range(n):
    if not v in color and M[u][v] != -1 and d[v] > M[u][v]:
      d[v] = M[u][v]
      p[v] = u
print(sum(M[i][p[i]] for i in range(1,n)))
