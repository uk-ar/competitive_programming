#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# A = list(map(int,sys.stdin.readline().split()))
# A = [sys.stdin.readline() for _ in range(N)]
# A = [list(map(int,sys.stdin.readline())) for _ in range(N)]
# A = [int(sys.stdin.readline()) for _ in range(N)]
# S = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
import sys,bisect,math
sys.setrecursionlimit(15000)

N = int(sys.stdin.readline())
ret = []
n = N
for i in range(2,math.floor(pow(N,0.5))+1):
  #print(n,i,n%i)
  while n%i==0:
    ret.append(i)
    n = n//i
if n != 1:
    ret.append(n)
print("{}: {}".format(N," ".join(map(str,ret))))
#print("{}: {}".format(N,str(ret)[1:-1]))
