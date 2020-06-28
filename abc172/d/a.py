#!/usr/bin/env pypy3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys,math

N = int(sys.stdin.readline())
#counting prime
isPrime = [True]*(N+1)
f = [1]*(N+1)

for i in range(2,N+1):
    f[i] += 1
    j = i + i
    while j <= N:
        f[j] += 1
        j += i

sum = 0
for i in range(1,N+1):
    f[i] = f[i]*i
    sum += f[i]

print(sum)
