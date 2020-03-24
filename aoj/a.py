#!/usr/bin/env python3
import sys,collections
n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
def partition(A,p,r):
  x = A[r]
  i = p-1
  for j in range(p,r):
    if A[j] <= x:
      i += 1
      A[i],A[j] = A[j],A[i]
  A[i+1],A[r] = A[r],A[i+1]
  return i+1
q = partition(A,0,len(A)-1)
print(" ".join([str(e) if i != q else "["+str(e)+"]" for i,e in enumerate(A)]))
