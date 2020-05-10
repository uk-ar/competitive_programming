#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for _ in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys,bisect,math,collections,itertools
sys.setrecursionlimit(15000)
from functools import reduce
N = int(sys.stdin.readline())
n = N
ret = []
for i in range(1,math.floor(pow(N,0.5))+1):
  #print(n,i,n%i)
    if n%i==0:
        ret.append(i)
        n = n//i
ret.append(n)
for i in range(1,len(ret)):
    for t in map(list,list(itertools.combinations(ret,i))):
        if len(t)>1:
            a = reduce(lambda a,b: a*b,t)
        else:
            a = t[0]
