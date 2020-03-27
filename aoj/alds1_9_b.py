#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n = int(input())
A = [0]+list(map(int,input().split()))

def maxHeapify(A, i):
  l = i*2
  r = i*2+1
  if l <= n and A[l] > A[i]:
    largest = l
  else:
    largest = i
  if r <= n and A[r] > A[largest]:
    largest = r
  if largest != i:
    A[i],A[largest]=A[largest],A[i]
    maxHeapify(A,largest)

def buildMaxHeap(A):
  for i in range(n//2,0,-1):
    maxHeapify(A,i)

buildMaxHeap(A)
print(" ",end="")
print(" ".join(map(str,A[1:])))
