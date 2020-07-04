#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys

N,M = map(int,sys.stdin.readline().split())
s = sys.stdin.readline().rstrip()
Q = tuple(sys.stdin.readline().rstrip() for _ in range(M)) # multi line with single param

#https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
MOD = 2**61-1 #prime
A = [ord(c) - ord('a')+1 for c in s]
pows = [1]*(N+1)
shash = [0]*(N+1)
for i in range(N):
    pows[i+1] = (pows[i]*27)%MOD
    shash[i+1] = (shash[i]*27+A[i])%MOD
#print(shash)
l = 0
r = 0
d = set()
h = A[l]
for q in Q:
    if q == "L++":
        #print(r-l,A[l],h-A[l]*pow(26,r-l,MOD))
        #h = (h-A[l]*pows[r-l])%MOD
        l += 1
    elif q == "L--":
        l -= 1
        #h = (h+A[l]*pows[r-l])%MOD
    elif q == "R++":
        r += 1
        #print(A[r],r)
        #h = ((h*27)+A[r])%MOD
    elif q == "R--":
        r -= 1
        #h = h//27
    #print(h,r,l,s[l:r+1],shash[r+1]-shash[l]*pows[r+1-l])
    #assert(h==(shash[r+1]-shash[l]*pows[r+1-l])%MOD)
    #print(s[l:r+1],h,q)
    assert(l<=r)
    assert(0<=l)
    assert(0<=r)
    d.add((shash[r+1]-shash[l]*pows[r+1-l])%MOD)
#print(d)
print(len(d))
# #https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
# MOD = 2**61-1 #prime
# A = [ord(c) for c in T]
# pows = list(reversed([126**i for i in range(np)]))
# ch = (sum(pows[i]*A[i] for i in range(np)))%MOD
# ph = (sum(pows[i]*(ord(P[i])) for i in range(np)))%MOD
# po = pow(126,np,MOD)
# if ch == ph:
#     print(0)
# for i in range(len(T)-np):
#     ch = (ch*126-po*A[i]+A[i+np])%MOD
#     if ch == ph:
#         print(i+1)
