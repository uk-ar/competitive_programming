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
NT = len(T)
P = sys.stdin.readline().rstrip()
NP = len(P)
if NT < NP:
    exit()
#https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
MOD = 2**61-1 #prime
A = [ord(c) for c in T]
pows = [1]*(NT+1)
shash = [0]*(NT+1)
for i in range(NT):
    pows[i+1] = (pows[i]*126)%MOD
    shash[i+1] = (shash[i]*126+A[i])%MOD
ph = 0
for i in range(NP):
    ph = (ph*126+ord(P[i]))%MOD
for i in range(len(T)-NP+1):
    if ph == (shash[i+NP]-shash[i]*pows[NP])%MOD:
        print(i)
