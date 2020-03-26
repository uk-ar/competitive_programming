#!/usr/bin/env python3
n = int(input())
children = [0]*n
parents = [-1]*n
for i in range(n):
    a = input().split()
    id = int(a[0])
    children[id]=list(map(int,a[2:]))
    for c in children[id]:
        parents[c] = id
depths = [0]*n
depth = 0
root = 0
while parents[root]!=-1:
    root += 1
nodes = [root]
while nodes:
    nodes_new = []
    for node in nodes:
        nodes_new.extend(children[node])
        depths[node] = depth
    nodes = nodes_new
    depth += 1
for i in range(n):
    if i == root:
        kind = "root"
    elif not children[i]:
        kind = "leaf"
    else:
        kind = "internal node"
    print("node {}: parent = {}, depth = {}, {}, {}"
          .format(i,parents[i],depths[i],kind,children[i]))
