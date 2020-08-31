#!/usr/bin/env pypy3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import math,sys

n = int(sys.stdin.readline())
a = tuple(map(int,sys.stdin.readline().split()))
#n = int(input())
#a = list(map(int,input().split()))
g = math.gcd(a[0],a[1])
for i in range(2,n):
    g = math.gcd(g,a[i])
M = max(a)
acc = a[0]
for i in range(n):
    acc = math.gcd(acc,a[i])
if acc != 1:
    print("not coprime")
    exit()

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
def factrial(N):
     ret = []
     while minPrime[N] != N:
         ret.append(minPrime[N])
         N = N//minPrime[N]
     if N != 1:
         ret.append(N)
     return ret

judge = set([])

for e in a:
    asf = set(factrial(e))
    if judge & asf != set():
        print("setwise coprime")
        exit()
    judge |= asf
    #judge = judge | asf #too slow
print("pairwise coprime")
