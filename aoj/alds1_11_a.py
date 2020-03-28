#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n = int(sys.stdin.readline())

ret = []
inp = sys.stdin.readlines()
G = [[0]*n for _ in range(n)]
for i in range(n):
  v = list(map(int,inp[i].split()))
  for j in v[2:]:
    G[v[0]-1][j-1] = 1
  print(" ".join(map(str,G[i])))
