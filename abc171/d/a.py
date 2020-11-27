#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections

N = int(sys.stdin.readline())
A = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
Q = int(sys.stdin.readline())
BC = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(Q)) # multi line with multi param
co = collections.Counter(A)
s = sum(A)

for b,c in BC:
    if b in co:
        n = co[b]
        del(co[b])
        co[c] += n
        s += (c-b)*n
    print(s)
