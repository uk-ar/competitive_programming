#!/usr/bin/env pypy3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import math,sys
P = 1000000007
# def modpow(a,n,mod):
#     res = 1
#     while n > 0:
#         if n & 1:
#             res = res * a % mod
#         a = a * a % mod
#         n >>= 1
#     return res

N = int(sys.stdin.readline())
print((pow(10,N,P)-pow(9,N,P)-pow(9,N,P)+pow(8,N,P))%P)
