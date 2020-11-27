# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections
N = int(sys.stdin.readline())
a = tuple(sys.stdin.readline().rstrip() for _ in range(N)) # multi line with single param

class TrieNode:
    #def __init__(self,parent,children={}):
    def __init__(self):
        self.parent = None
        self.children = {}
        #self.end = False
    def add(self,key):
        self.children[key] = TrieNode()
        self.children[key].parent = self
        self.children[key].label = key
        return self.children[key]
    # def end(self):
    #     self.end = True
    # def __repr__(self):
    #     return 'TrieNode(%s,%s)' % (str(self.parent),str(self.children))
    def __str__(self):
        return 'TrieNode(%s)' % (repr(self.children))

#root = TrieNode(None)
ends = set()
root = TrieNode()
for s in a:
    n = root
    for c in s[::-1]:
        if not c in n.children:
            #n.children[c] = TrieNode(n)
            n.add(c)
        n = n.children[c]
    ends.add(n)
# print(ends)
# print(root)
