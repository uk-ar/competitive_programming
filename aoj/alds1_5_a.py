#!/usr/bin/env python3
import sys,collections
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
q = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))
def isOK(rest,i):
  if rest == 0:
    return True
  if i == n or rest < 0:
    return False
  if sum(a[i:]) < rest:
    return False
  if isOK(rest-a[i],i+1):
    return True
  return isOK(rest,i+1)
for mi in m:
  if isOK(mi,0):
    print("yes")
  else:
    print("no")
