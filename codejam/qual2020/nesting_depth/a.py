#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
# i = int(sys.stdin.readline())
import sys,bisect
sys.setrecursionlimit(15000)

n = int(sys.stdin.readline())
for i in range(n):
  ret = []
  depth = 0
  for c in sys.stdin.readline().rstrip():
    num = int(c)
    if num == depth:
      ret.append(c)
    elif num > depth:
      ret += ["("]*(num - depth)
      ret.append(c)
    elif num < depth:
      ret += [")"]*(depth - num)
      ret.append(c)
    depth = num
  if depth > 0:
    ret += [")"]*(depth)
  print("Case #{}: {}".format(i+1,"".join(ret)))
