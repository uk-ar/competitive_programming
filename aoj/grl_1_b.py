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
sdw = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(E)) # multi line with multi param
#sdw = [[src1 dist1 d1][src1 dist1 d1]...]# vect source1 -> distance1 distances
INF = float("inf")
ALL = set(range(N))#including sentinel
distances = collections.defaultdict(lambda:INF)
distances[r] = 0

for _ in range(N):
  modified = False
  for src,dst,weight in sdw:
    if distances[dst] > distances[src] + weight:
      distances[dst] = distances[src] + weight
      modified = True
  if modified == False:
    for i in range(N):
      if distances[i] == INF:
        print("INF")
      else:
        print(distances[i])
    exit()
print("NEGATIVE CYCLE")
