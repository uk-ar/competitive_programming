#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections
N,E,r = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
sdd = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(E)) # multi line with multi param
#G = [[src1 dist1 d1][src1 dist1 d1]...]# vect source1 -> distance1 distances
G = [[] for i in range(N)]
for src,dist,d in sdd:
  G[src].append((dist,d))
#print(sdd,r,G)
INF = float("inf")
ALL = set(range(N))
mst = set()
#distances = [INF]*N # 始点rからの距離
distances = collections.defaultdict(lambda:INF)
distances[r] = 0

import heapq

dv = []
def add(u):
  mst.add(u)
  if len(mst) == N: return
  for v,w in G[u]:
    if not v in mst and w + distances[u] < distances[v]: # uを経由した方が安い
      distances[v] = distances[u]+w
      heapq.heappush(dv, (distances[v],v))
  #print(distances)
  #print(u,distances,dv)
  if not dv:
    return None
  d,v = heapq.heappop(dv)
  while dv and v in mst:
    d,v = heapq.heappop(dv)
  if v in mst:
    return None
  return v

n = add(r)
while n != None:
  n = add(n)
  #print("n:",n)

for i in range(N):
  if distances[i] == INF:
    print("INF")
  else:
    print(distances[i])
