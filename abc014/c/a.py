#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")

# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_1_B
import sys,collections
sys.setrecursionlimit(1000000)
INF = float("inf")

Q = int(sys.stdin.readline())
ab = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(Q)) # multi line with multi param
N = 1000001

cum=[0]*(N+1)

for l,r in ab:
    cum[l] += 1
    if r+1 < N+1: cum[r+1] -= 1

ret = cum[0]
for i in range(N):
    cum[i+1] += cum[i]
    ret = max(ret,cum[i+1])

print(ret)
