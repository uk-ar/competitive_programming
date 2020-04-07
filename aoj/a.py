#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
import sys,bisect
sys.setrecursionlimit(15000)
h,w = map(int,sys.stdin.readline().split())
buffer = [None for _ in range(h)]
T = [[0]*(w+1) for _ in range(h)]

for r in range(h):
  buffer = list(map(int,sys.stdin.readline().split()))
  for col in range(w):
    if buffer[col] == 1:
      T[r][col] = 0
    elif r == 0:
      T[0][col] = 1
    else:
      T[r][col] = T[r-1][col]+1
m = 0

for buffer in T:
  stack = []
  for i in range(w+1):
    if not stack:
      stack.append({"h":buffer[i],"p":i})
    elif stack[-1]["h"] < buffer[i]:
      stack.append({"h":buffer[i],"p":i})
    elif stack[-1]["h"] == buffer[i]:
      continue
    elif stack[-1]["h"] > buffer[i]:
      while stack and stack[-1]["h"] >= buffer[i]:
        pre = stack.pop()
        m = max(m,pre["h"]*(i-pre["p"]))
      stack.append({"h":buffer[i],"p":pre["p"]})
print(m)
