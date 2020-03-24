#!/usr/bin/env python3
n = int(input())
S = list(map(int,input().split())) + [0]
q = int(input())
T = map(int,input().split())
ret = 0
for t in T:
  i = 0
  S[n] = t
  while t != S[i]:
    i += 1
  if i != n:
    ret += 1
print(ret)
