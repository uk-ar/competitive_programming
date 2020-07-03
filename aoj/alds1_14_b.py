#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys

T = sys.stdin.readline().rstrip()
nt = len(T)
P = sys.stdin.readline().rstrip()
np = len(P)
if nt < np:
    exit()
#https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
MOD = 2**61-1 #prime
A = [ord(c) for c in T]
pows = list(reversed([126**i for i in range(np)]))
ch = (sum(pows[i]*A[i] for i in range(np)))%MOD
ph = (sum(pows[i]*(ord(P[i])) for i in range(np)))%MOD
po = pow(126,np,MOD)
if ch == ph:
    print(0)
for i in range(len(T)-np):
    ch = (ch*126-po*A[i]+A[i+np])%MOD
    if ch == ph:
        print(i+1)
