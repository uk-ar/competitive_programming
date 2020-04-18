#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys,bisect
sys.setrecursionlimit(15000)

st = []
ar = 0
while True:
  n = int(sys.stdin.readline())
  if n == 0:
    break
  a = [int(sys.stdin.readline()) for _ in range(n)]
  ml = mg = a[0]
  #print(a)
  for i in range(1,n):
    ml = max(ml+a[i],a[i])
    mg = max(mg,ml)
    #print(ml,mg,a[i])
  print(mg)
