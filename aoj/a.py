#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys,bisect
sys.setrecursionlimit(15000)
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.append(0)

st = []
ar = 0
for i in range(n+1):
  if not st:
    st.append([i,a[i]])
  elif st[-1][1] < a[i]:
    st.append([i,a[i]])
  elif st[-1][1] == a[i]:
    continue
  elif st[-1][1] > a[i]:
    while st and st[-1][1] >= a[i]:
      j,h = st.pop()
      ar = max(ar,(i-j)*(h))
    st.append([j,a[i]])
  #print(i,ar,st)
#print(a)
print(ar)
