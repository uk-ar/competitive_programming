#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")

# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_1_B
import sys
sys.setrecursionlimit(1000000)
INF = float("inf")

while True:
    N,K = map(int,sys.stdin.readline().split())
    if N==0 and K==0:
        exit()
    a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param

    com = [0]*(N+1)
    for i in range(N):
        com[i+1]=com[i]+a[i]

    ret = -INF
    for i in range(N-K):
        ret = max(ret,com[i+K]-com[i])
    print(ret)
