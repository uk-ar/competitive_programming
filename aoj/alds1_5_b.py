#!/usr/bin/env python3
import sys,collections
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
c = 0
def merge(a,left,mid,right):
  n1 = mid - left
  n2 = right - mid
  L = a[left:mid]
  R = a[mid:right]
  L.append(float("inf"))
  R.append(float("inf"))
  i = 0
  j = 0
  for k in range(left,right):
    global c
    c += 1
    if L[i] <= R[j]:
      a[k] = L[i]
      i += 1
    else:
      a[k] = R[j]
      j += 1

def mergeSort(a,left,right):
  if 1 < right - left:
    mid = (left+right)//2
    mergeSort(a,left,mid)
    mergeSort(a,mid,right)
    merge(a,left,mid,right)

mergeSort(a,0,n)
print(" ".join(map(str,a)))
print(c)
