#!/usr/bin/env python3
import sys,collections
n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
def partition(A,p,r):
  x = A[r] #pivod
  i = p    #high-start
  for j in range(p,r): #high-end
    if A[j] <= x:
      A[i],A[j] = A[j],A[i]
      i += 1
  A[i],A[r] = A[r],A[i]
  return i
q = partition(A,0,len(A)-1)
print(" ".join([str(e) if i != q else "["+str(e)+"]" for i,e in enumerate(A)]))
