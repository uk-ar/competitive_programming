#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
# i = int(sys.stdin.readline())
import sys,collections
sys.setrecursionlimit(15000)

T = int(sys.stdin.readline())
for test in range(T):
  N = int(sys.stdin.readline())
  ts = [None]*N
  for i in range(N):
    S,E = map(int,sys.stdin.readline().split())
    ts[i] = [S,E,i]
  #print(ts)
  ts.sort()
  ret = [None]*N
  d = ["C","J"]
  q = []
  for S,E,i in ts:
    if not q:
      ret[i] = d[0] # "C"
      q.append([E,0])
    else:
      for j in range(len(q))[::-1]:
        if q[j][0] <= S: #remove finished
          q.pop(j)
      #print(q,E,S,i,ret)
      if len(q) >= 2:
        ret =[]
        break
      if not q:
        ret[i] = d[0] # "C"
        q.append([E,0])
      else:
        ret[i] = d[q[0][1]^1]
        q.append([E,q[0][1]^1])
    #print(q,E,S,i,ret)
  if not ret:
    ret = "IMPOSSIBLE"
  else:
    ret = "".join(ret)
  print("Case #{}: {}".format(test+1,ret))
