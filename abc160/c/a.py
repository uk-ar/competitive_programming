#!/usr/bin/env pypy3
import sys
sys.setrecursionlimit(15000)
k,n = map(int,input().split())
a = list(map(int,input().split()))
d = [a[i]-a[i-1] for i in range(1,n)]+[a[0]+k-a[-1]]
#print(d)
m = max(d)
s = sum(d)
print(s-m)
