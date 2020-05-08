#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections
N = int(sys.stdin.readline())
G = tuple(tuple(map(int,sys.stdin.readline().rstrip().split()))[2:] for _ in range(N)) # multi line with multi param
# n x n adjacency matrix
#G = [[-1,2,3],[2,-1,3],[1,2,-1]]
INF = float("inf")
ALL = set(range(N))
mst = set()
distances = [INF]*N # 始点0からの距離
distances[0] = 0

import heapq

dv = []
def add(u):
  mst.add(u)
  if not ALL-mst: return
  for j in range(0,len(G[u]),2):
    v = G[u][j]
    w = G[u][j+1]
    if not v in mst and w + distances[u] < distances[v]: # uを経由した方が安い
      distances[v] = distances[u]+w
      heapq.heappush(dv, (distances[v],v))
  #print(distances)
  d,v = heapq.heappop(dv)
  while v in mst:
    d,v = heapq.heappop(dv)
  return v

n = add(0)
distances[0] = 0
while len(mst) < len(G):
  n = add(n)

for i in range(N):
  print(i,distances[i])
