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

H,W,Q = map(int,sys.stdin.readline().split())
a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
b = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
q = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(Q)) # multi line with multi param

B = [0]*(W+1)

sign = 1
for c in range(W):
    B[c+1] += B[c]+sign*b[c]
    sign *= -1

sign = 1
A = [0]*(H+1)
for r in range(H):
    A[r+1] += A[r]+sign*a[r]
    sign *= -1

ans=[0]*Q
for i in range(Q):
    px,py,qx,qy = q[i]
    print((A[qx]-A[px-1])*(B[qy]-B[py-1]))
