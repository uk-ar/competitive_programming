#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys

N,M,K = map(int,sys.stdin.readline().split())
a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
b = tuple(map(int,sys.stdin.readline().split())) # single line with multi param

cum_a = [0]*(N+1)
for i in range(N):
    cum_a[i+1] = cum_a[i]+a[i]

cum_b = [0]*(M+1)
for i in range(M):
    cum_b[i+1] = cum_b[i]+b[i]

j = M
ret = 0
for i in range(N+1):
    if cum_a[i] > K:
        break
    while 0 <= j and j <=M and cum_a[i]+cum_b[j]>K:
        j -= 1
    ret = max(ret,i+j)

print(ret)
