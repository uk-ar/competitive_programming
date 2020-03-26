#!/usr/bin/env python3
import sys
n = int(input())
class Node:
  def __init__(self):
    self.p = -1 # parent
    self.l = -1 # left most child
    self.r = -1 # right sibling

T = [Node() for _ in range(n)]
D = [0]*n
sys.setrecursionlimit(1500)
def rec(u,p):
  D[u] = p
  if T[u].r != -1: rec(T[u].r,p)
  if T[u].l != -1: rec(T[u].l,p+1)

H = [0]*n
def rec1(u):
  r = l = 0
  if T[u].r != -1: r = rec(T[u].r)
  if T[u].l != -1: l = rec(T[u].l)
  H[u] = max(r,l)
  return H[u]

for i in range(n):
    v,l,r = map(int,input().split())
    T[v].r = r
    if T[v].p != -1 and T[v].r != -1:
      T[r].p = T[v].p
    c = T[v].l = l
    print(i)
    while c != -1:
      T[c].p = v
      c = T[c].r

for i in range(n):
  if T[i].p == -1 : r = i

rec(r,0)
rec1(r)
for i in range(n):
  if T[i].p == -1:
    kind = "root"
  elif T[i].l != None: kind = "internal node"
  else: kind = "leaf"
  d = 0
  n = T[i].l
  while n != None:
    d += 1
    n = T[n].r
  print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}"
        .format(i,T[i].p,T[i].r,d,D[i],H[i],kind))
