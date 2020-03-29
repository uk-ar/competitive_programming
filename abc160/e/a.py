#!/usr/bin/env pypy3
import sys
sys.setrecursionlimit(15000)
x,y,a,b,c = map(int,input().split())
p = list(sorted(map(int,input().split()),reverse=True))[:x] # x
q = list(sorted(map(int,input().split()),reverse=True))[:y] # y
r = list(sorted(map(int,input().split()),reverse=True))
print(sum(sorted(p+q+r,reverse=True)[:x+y]))
