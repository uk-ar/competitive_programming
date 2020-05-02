#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for _ in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys,bisect,math
sys.setrecursionlimit(15000)

A,B,N = map(int,sys.stdin.readline().split())

# if A < B:
#     x = B//2
#     if x < N:
#         m = math.floor(A*i/B)-A*math.floor(i/B)
# else:
#     m = 0
# print(m)
m = -float("inf")
for i in range(N+1):
    res = math.floor(A*i/B)-A*math.floor(i/B)
    if m < res:
        print(i,res)
        m = math.floor(A*i/B)-A*math.floor(i/B)
print(m)
# x = B//2
# print(math.floor(A*x/B)-A*math.floor(x/B))
