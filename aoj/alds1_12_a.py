#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n = int(sys.stdin.readline())
M = [list(map(int,l.split())) for l in sys.stdin.readlines()]

color = set() #MST
d = [float("inf")]*n #distance
d[0]=0
p = [-1]*n
#print(M)
while len(color) < n:
  u = -1
  for i in range(n):
    if not i in color and (u == -1 or d[u] > d[i]):# next
      u = i
  color.add(u)
  for v in range(n):
    if not v in color and M[u][v] != -1 and d[v] > M[u][v]:
      d[v] = M[u][v]
      p[v] = u
print(sum(M[i][p[i]] for i in range(1,n)))

# import sys,collections
# N = int(sys.stdin.readline())
# G = tuple(tuple(map(int,sys.stdin.readline().rstrip().split()) for _ in range(N))) # multi line with multi param
# # n x n adjacency matrix
# #G = [[-1,2,3],[2,-1,3],[1,2,-1]]

# INF = float("inf")
# ALL = set(range(N))
# distances = [INF]*N
# mst = set()

# def add(e):
#   mst.add(e)
#   if not ALL-mst: return
#   for i,w in enumerate(G[e]):
#     if not i in mst and w != -1:
#       distances[i] = min(distances[i],w)
#   m = min((distances[i],i) for i in ALL-mst)
#   return m[1]

# n = add(0)
# distances[0] = 0
# while len(mst) < len(G):
#   n = add(n)
# print(sum(distances))
