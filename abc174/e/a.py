#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
INF = float("inf")
import sys,collections,heapq,math

N,K = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split())) # single line with multi param
a.sort(reverse=True)

ng = 0
ok = a[0]

def isOK(v):
    k = K
    i = 0
    while k >= 0 and i < N:
        k = k - (((a[i]+v-1)//v) - 1)
        #k = k - (math.ceil(a[i]/v) - 1)
        i += 1
    return k >= 0

while abs(ng-ok) > 1:
    mid = (ok+ng)//2
    if isOK(mid):#ok condition?
        ok = mid #move ok
    else:
        ng = mid
print(math.ceil(ok))
