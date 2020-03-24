#!/usr/bin/env python3
import sys,collections
n,k = map(int,sys.stdin.readline().split())
w = list(map(int,sys.stdin.readlines()))
ng = sum(w)//k-1
ok = sum(w)
def isOK(p):
  j = 0
  for i in range(k):
    s = 0
    while j < n and s + w[j] <= p:
      s += w[j]
      j += 1
  return j == n
while ok - ng > 1:
  mid = (ok+ng)//2
  t = collections.Counter(w)
  if isOK(mid):
    ok = mid
  else:
    ng = mid
print(ok)
