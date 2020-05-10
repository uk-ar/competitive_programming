#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections

N,K = map(int,sys.stdin.readline().split())
A = tuple(map(int,sys.stdin.readline().split())) # single line with multi param

d = {}
a = []
n = 1
i = 0
while True:
    #print(n)
    d[n] = i
    i += 1
    a.append(n)
    n = A[n-1]
    if n in d:
        break
pre = d[n]
cycle = a[pre:]
#print(pre,a,cycle)
if K < pre:
    print(a[K])
else:
    print(a[pre+(K-pre)%(len(cycle))])
