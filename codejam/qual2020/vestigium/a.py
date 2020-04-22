#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
# i = int(sys.stdin.readline())
import sys
sys.setrecursionlimit(15000)

T = int(sys.stdin.readline())

for test in range(T):
  N = int(sys.stdin.readline())
  a = [None]*N
  for i in range(N):
    a[i] = list(map(int,sys.stdin.readline().split()))
  #For each test case, output one line containing Case #x: k r c, where x is the test case number (starting from 1), k is the trace of the matrix, r is the number of rows of the matrix that contain repeated elements, and c is the number of columns of the matrix that contain repeated elements.
  t = row = col = 0
  cs = [set() for _ in range(N)]
  for r in range(N):
    rs = set()
    for c in range(N):
      rs.add(a[r][c])
      cs[c].add(a[r][c])
      if r == c:
        t += a[r][c]
        #print(cs)
    if len(rs) < N:
      row += 1
  for c in cs:
    if len(c) < N:
      col += 1
  print("Case #{}: {} {} {}".format(test+1,t,row,col))
