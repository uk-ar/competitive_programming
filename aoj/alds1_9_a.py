#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n = int(input())
A = [0]+list(map(int,input().split()))

for i in range(1,n+1):
  if i != 1:
    parent = "parent key = {}, ".format(str(A[(i)//2]))
  else:
    parent = ""
  if i*2 < n+1:
    left = "left key = {}, ".format(str(A[i*2]))
  else:
    left = ""
  if i*2+1 < n+1:
    right = "right key = {}, ".format(str(A[i*2+1]))
  else:
    right = ""
  print("node {}: key = {}, {}{}{}".format(i,str(A[i]),parent,left,right))
