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
l = 0
r = 0
d = set()
h = A[l]
for q in Q:
    if q == "L++":
        #print(r-l,A[l],h-A[l]*pow(26,r-l,MOD))
        h = (h-A[l]*pow(27,r-l,MOD))%MOD
        l += 1
    elif q == "L--":
        l -= 1
        h = (h+A[l]*pow(27,r-l,MOD))%MOD
    elif q == "R++":
        r += 1
        #print(A[r],r)
        h = ((h*27)+A[r])%MOD
    elif q == "R--":
        r -= 1
        h = h//27
    #print(s[l:r+1],h,q)
    assert(l<=r)
    assert(0<=l)
    assert(0<=r)
    d.add(h)
#print(d)
print(len(d))
