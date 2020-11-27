#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections,math,fractions
sys.setrecursionlimit(1000000)
INF = float("inf")

N = int(sys.stdin.readline())
A = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
#3 8 9 10 11 12
left = [A[0]]*(N)
for i in range(1,N):
    left[i] = fractions.gcd(left[i-1],A[i])

right =[A[N-1]]*(N)
for i in range(N-1)[::-1]:
    right[i] = fractions.gcd(right[i+1],A[i])

#print(left,right)

ret = -INF
for i in range(N):
    if i-1 >= 0 and i+1 < N:
        a = fractions.gcd(left[i-1],right[i+1])
    elif i-1 >= 0:
        a = left[i-1]
    else:
        a = right[i+1]
    ret = max(ret,a)
print(ret)
