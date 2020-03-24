import sys
n = int(sys.stdin.readline())
#lines = sys.stdin.readlines()
#n = int(input())
#import collections
#dll = collections.deque()
class Node:
  def __init__(self,v):
    self.val = v
    self.prev = None
    self.next = None
class DLL():
  def __init__(self):
    self.head = Node(None)
  def insert(self,x):
    n = Node(x)
    pre = self.head.next
    if pre:
      pre.prev = n
      n.next = pre
    self.head.next = n
  def delete(self,x):
    node = self.head
    while node:
      if node.val == x:
        p = node.prev
        n = node.next
        p.next = n
        if n:
          n.prev = p
        return
      node = node.next
  def deleteFirst(self):
    pre = self.head.next
    if not pre:
      return
    self.head.next = pre.next
    if pre.next:
      pre.next.prev = self.head
  def deleteLast(self):
    if not self.head.next:
      return
    node = self.head
    while node.next:
      node = node.next
    node.prev.next = None
  def inspect(self):
    node = self.head.next
    ret = []
    while node:
      ret.append(str(node.val))
      node = node.next
    print(" ".join(ret))
dll=DLL()
for i in range(n):
  q = sys.stdin.readline().split()#input()
  if q[0] == "deleteLast":
      dll.deleteLast()
      #dll.pop()
  elif q[0] == "deleteFirst":
      dll.deleteFirst()
      #dll.popleft()
  else:
      if q[0] == "insert":
          dll.insert(int(q[1]))
          #dll.appendleft(int(q[1]))
      else:
          b = int(q[1])
          #if b in dll:
          dll.delete(int(q[1]))
            #dll.remove(b)
dll.inspect()
#print(" ".join(map(str,dll)))
