#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections
sys.setrecursionlimit(1000000)
INF = float("inf")

N = int(sys.stdin.readline())
A = tuple(map(int,sys.stdin.readline().split())) # single line with multi param

cum = [0]*(N+1)
for i in range(N):
    cum[i+1] = cum[i]+A[i]

for i in range(N):
    ret = 0
    for j in range(N):
        ret = max(ret,cum[min(j+i+1,N)]-cum[j])
    print(ret)
