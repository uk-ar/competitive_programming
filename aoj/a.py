#!/usr/bin/env python3
import sys,collections
n = int(sys.stdin.readline())
#A = list(map(int,sys.stdin.readline().split()))
A = [[x,int(y)] for x,y in [line.split() for line in sys.stdin.readlines()]]
d = {}
for i,p in enumerate(A):
  d[str(p)]=i
def partition(A,p,r):
  x = A[r][1] #pivod
  i = p    #high-start
  for j in range(p,r): #high-end
    if A[j][1] <= x:
      A[i],A[j] = A[j],A[i]
      i += 1
  A[i],A[r] = A[r],A[i]
  return i
def quicksort(A,p,r):
  if p < r:
    q = partition(A,p,r)
    quicksort(A,p,q-1)
    quicksort(A,q+1,r)
quicksort(A,0,len(A)-1)
for i in range(1,n):
  if A[i-1][1]==A[i][1] and d[str(A[i-1])] > d[str(A[i])]:
    print("Not stable")
    print("\n".join([p[0]+" "+str(p[1]) for p in A]))
    exit(0)
print("Stable")
print("\n".join([p[0]+" "+str(p[1]) for p in A]))
#print(" ".join([str(e) if i != q else "["+str(e)+"]" for i,e in enumerate(A)]))
