#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n = int(sys.stdin.readline())

ret = []
inp = sys.stdin.readlines()
G = [None]*(n)
d = [0]*(n)
f = [0]*(n)
def dfs(i,t):
  if d[i] != 0:
    return t
  t = t+1
  d[i] = t
  for j in G[i]:
    t = dfs(j,t)
  f[i] = t+1
  return f[i]
for i in range(n):
  v = list(map(int,inp[i].split()))
  G[v[0]-1] = list(map(lambda x: int(x-1),v[2:]))
#print(G)
t = 0
for j in range(n):
  t = dfs(j,t)

for i in range(n):
  print(i+1,d[i],f[i])
