#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# INF = float("inf")
# sys.setrecursionlimit(10000)
import sys,collections
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
if 0 in a:
    print(0)
    exit()
ret = 1
i = 0
lim = 10**18
while i < len(a):
    ret *= a[i]
    if lim < ret:
        print(-1)
        exit()
    i += 1
print(ret)
