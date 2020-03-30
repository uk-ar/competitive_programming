#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n = int(sys.stdin.readline())
G = [list(map(int,l.split())) for l in sys.stdin.readlines()]

s = {0}
su = 0
while len(s) < n:
  mi = 0
  mj = 0
  for i in s:
    for j in range(n):
      if G[i][j] == -1 or j in s:
        continue
      if (mi == 0 and mj == 0) or G[i][j] < G[mi][mj]:
        mi = i
        mj = j
  s.add(mj)
  su += G[mi][mj]
print(su)
