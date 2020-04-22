#!/usr/bin/env pypy3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# d = collections.defaultdict(list)
# h = list() heapify(h)
# product('ABCD', repeat=2)# AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)  # AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)  # AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2) #AA AB AC AD BB BC BD CC CD DD
import math
from functools import reduce
import sys
sys.setrecursionlimit(15000)

n,k = map(int,sys.stdin.readline().split())
dp = [0]*(k+1)
s = 0
#print("nk:",n,k)
l = 0
for x in range(1,k+1)[::-1]:
    dp[x] = pow(k//x,n,1000000007)
    j = 2
    #print(2*x,k+1,x)
    for j in range(2*x,k+1,x):
        #print("j",x,j,k,n)
        dp[x] -= dp[j]
    s = (s + (dp[x]*x))%1000000007
#return reduce(math.gcd, numbers)
#sum += gcd(a,b,c)
#print(sum(dp[n-1][j] for j in range(k)))
#print(dp)
print(s)
