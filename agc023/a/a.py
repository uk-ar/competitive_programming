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

N = int(sys.stdin.readline())
A = tuple(map(int,sys.stdin.readline().split())) # single line with multi param

cum = [0]*(N+1)
d = collections.defaultdict(int)
d[0]=1
ret = 0
for i in range(N):
    cum[i+1] = cum[i]+A[i]
    if cum[i+1] in d:
        ret += d[cum[i+1]]
    d[cum[i+1]] += 1
#print(cum,d)
print(ret)
