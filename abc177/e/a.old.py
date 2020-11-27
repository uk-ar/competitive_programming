#!/usr/bin/env pypy3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections

N = int(sys.stdin.readline())
#a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
a = list(map(int,input().split()))

import math
acc = a[0]
LIMIT=max(a)
minPrime = [0]*(LIMIT+1)
minPrime[1] = 1
def make():
    for i in range(2,LIMIT+1):
        if minPrime[i] == 0:
            minPrime[i] = i
            #print(i)
            for j in range(i+i,LIMIT+1,i):
                #print(i,j)
                if minPrime[j] == 0:
                    minPrime[j] = i
make()
# def factrial(N):
#     ret = []
#     while minPrime[N] != N:
#         ret.append(minPrime[N])
#         N = N//minPrime[N]
#     if N != 1:
#         ret.append(N)
#     return ret

def factrial(N):
    ret = set()
    while 1 != N:
        ret.add(minPrime[N])
        N = N//minPrime[N]
    if N != 1:
        ret.add(N)
    return ret

for i in range(N):
    acc = math.gcd(acc,a[i])
if acc != 1:
    print("not coprime")
    exit()

pairwise = True
p = set() #all prime
for e in a:
    if not pairwise:
        break
    f = factrial(e)
    if p & f != set():
        pairwise = False
        print("setwise coprime")
        exit(0)
    p = p | f

if pairwise:
    print("pairwise coprime")
else:
    print("setwise coprime")
