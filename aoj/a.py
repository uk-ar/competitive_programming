#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
import sys,bisect
sys.setrecursionlimit(15000)
s = sys.stdin.readline().rstrip()
st = []
ars = []
ar = 0
for i,c in enumerate(s):
  if c == "\\":
    st.append(i)
  elif c == "/":
    if st:
      j = st.pop()
      ar += i-j
      while ars and j < ars[-1][1]:
        ar0,_ = ars.pop()
        ar += ar0
      ars.append([ar,j])
      ar = 0
print(sum([ar for ar,_ in ars]))
if len(ars):
  print(0)
else:
  print(len(ars)," ".join(map(str,[ar for ar,_ in ars])))
