#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n = int(sys.stdin.readline())

ret = []
inp = sys.stdin.readlines()
G = [None]*(n+1)
depths = [-1]*(n+1)

for i in range(1,n+1):
  v = list(map(int,inp[i-1].split()))
  G[v[0]] = list(map(int,v[2:]))
#print(G)

nodes = [1]
depth = 0
while nodes:
  new = []
  for i in nodes:
    if depths[i] == -1:
      depths[i] = depth
      new += G[i]
    #print(i,nodes,depth,depths)
  depth += 1
  nodes = new

for i in range(1,n+1):
  print(i,depths[i])
