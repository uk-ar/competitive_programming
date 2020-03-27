#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n = int(input())
A = list(map(int,input().split()))

for i in range(n):
  if i != 0:
    parent = "parent key = {}, ".format(str(A[(i-1)//2]))
  else:
    parent = ""
  if i*2+1 < n:
    left = "left key = {}, ".format(str(A[i*2+1]))
  else:
    left = ""
  if i*2+2 < n:
    right = "right key = {}, ".format(str(A[i*2+2]))
  else:
    right = ""
  print("node {}: key = {}, {}{}{}".format(i+1,str(A[i]),parent,left,right))
