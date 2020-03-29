#!/usr/bin/env pypy3
import sys
sys.setrecursionlimit(15000)
n,x,y = map(int,input().split())

nums = [0]*n
for i in range(n):
    for j in range(i+1,n):
        d = min(j-i,abs(j-y+1)+1+abs(i-x+1))
        nums[d] += 1
        #print(d,i,j)
print(*nums[1:],sep='\n')
