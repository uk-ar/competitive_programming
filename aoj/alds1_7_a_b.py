#!/usr/bin/env python3
n = int(input())
class Node:
  def __init__(self):
    self.p = -1 # parent
    self.l = None # left most child
    self.r = None # right sibling

T = [Node() for _ in range(n)]
D = [0]*n

def rec(u,p):
  D[u] = p
  if T[u].r != None: rec(T[u].r,p)
  if T[u].l != None: rec(T[u].l,p+1)

for i in range(n):
    a = input().split()
    v = int(a[0])
    for j,c in enumerate(map(int,a[2:])):
      if j == 0: T[v].l = c
      else: T[pre].r = c
      pre = c
      T[c].p = v

for i in range(n):
  if T[i].p == -1 : r = i

rec(r,0)
for i in range(n):
  if T[i].p == -1:
    kind = "root"
  elif T[i].l: kind = "internal node"
  else: kind = "leaf"
  c = []
  n = T[i].l
  while n != None:
    c.append(n)
    n = T[n].r
  print("node {}: parent = {}, depth = {}, {}, {}"
        .format(i,T[i].p,D[i],kind,c))
