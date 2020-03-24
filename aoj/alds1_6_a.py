#!/usr/bin/env python3
import sys,collections
n = int(sys.stdin.readline())
#A = list(map(int,sys.stdin.readline().split()))
A = list(map(int,sys.stdin.readline().split()))
def CountingSort(A,B,k):
  #print(A)
  C = [0]*(k)
  for j in range(n):
    C[A[j]] += 1
    #print(C)
  for i in range(1,k):
    C[i] = C[i]+C[i-1]
  #print(C)
  for j in range(n)[::-1]:
    B[C[A[j]]-1] = A[j]
    C[A[j]] -= 1
    #print(B,C)
    #print(B)
B = [0]*n
CountingSort(A,B,10000)
print(" ".join(map(str,B)))
