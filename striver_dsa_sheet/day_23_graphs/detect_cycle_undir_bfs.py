from collections import defaultdict

class Graph:
  def __init__(self, n):
    self.grp = defaultdict(list)
    self.n = n 
  def addEdge(self,u,v):
    self.grp[u] += [v]
    
  def isCycle(self,i, vis):
    vis[i] = 1 
    q = [(i,-1)]
    
    while q:
      nd, par = q.pop(0)
      
      for ngbr in self.grp[nd]:
        if vis[ngbr] == 0:
          vis[ngbr] = 1 
          q += [(ngbr,nd)]
        elif ngbr != par:
          return True
    
    return False
  
n,e = map(int,input().split())
g = Graph(n)

for _ in range(e):
  u,v = map(int,input().split())
  g.addEdge(u,v)
  
print(g.grp)


vis = [0]*(n+1)
for i in range(1,n+1):
  if vis[i]==0:
    if g.isCycle(i,vis):
      print("There is a Cycle")
      break
else:
  print("No Cycle")

# O(V) + O(V+2E) and O(V)
  
