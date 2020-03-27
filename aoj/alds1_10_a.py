#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n = int(input())

memo = {0:1,1:1}

def fib(n):
  if n < 2:
    return memo[n]
  if not n in memo:
    memo[n] = fib(n-1)+fib(n-2)
  return memo[n]

print(fib(n))
