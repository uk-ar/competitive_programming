#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
import sys,bisect
sys.setrecursionlimit(15000)
h,w = map(int,sys.stdin.readline().split())
c = [None]*h

for r in range(h):
  a = list(map(int,sys.stdin.readline().split()))
  for col in range(w):
    if a[col] == 1:
      c[r][col] = 0
    elif r == 1:
      c[0][col] = 1
    else:
      c[r][col] = c[r-1][col]+1
print(c)
