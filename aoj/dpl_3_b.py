#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
import sys,bisect
sys.setrecursionlimit(15000)
h,w = map(int,sys.stdin.readline().split())
c = [[0]*(w+1) for _ in range(h)]

for r in range(h):
  a = list(map(int,sys.stdin.readline().split()))
  for col in range(w):
    if a[col] == 1:
      c[r][col] = 0
    elif r == 0:
      c[0][col] = 1
    else:
      c[r][col] = c[r-1][col]+1
m = 0

for r,row in enumerate(c):
  st = [{"h":0,"p":-1}]
  for i in range(w+1):
    n = {"h":row[i],"p":i}
    if not st:
      st.append(n)
    elif st[-1]["h"] < row[i]:
      st.append(n)
    elif st[-1]["h"] == row[i]:
      continue
    elif st[-1]["h"] > row[i]:
      n = {"h":row[i],"p":st[-1]["p"]}
      while st and st[-1]["h"] >= row[i]:
        n = {"h":row[i],"p":st[-1]["p"]}
        a = st.pop()
        m = max(m,(i-a["p"])*a["h"])
      if st and st[-1]["h"] < row[i]:
        st.append(n)
  if st:
    a = st.pop()
    m = max(m,(i-a["p"])*a["h"])
    #if r == 8:
    #   print(r,i,row,st,m)
print(m)
