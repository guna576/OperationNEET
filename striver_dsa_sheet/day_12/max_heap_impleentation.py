# Check the TC
# Falthu Love Babbar explanation

class Heap:
  def __init__(self):
    self.hp = [-1 for _ in range(100)]
    self.n = 0
  
  
  def heapify(self,l):
    self.n = len(l)
    for x in range(self.n):
      self.hp[x+1] = l[x] 
    
    x = self.n//2
    for i in range(x,0,-1):
      lr = i
      ll = 2*i 
      rr = 2*i + 1 
      
      if ll <= self.n and self.hp[lr] < self.hp[ll]:
        lr = ll 
      if rr <= self.n and self.hp[lr] < self.hp[rr]:
        lr = rr
      if lr != i:
        self.hp[lr],self.hp[i] = self.hp[i], self.hp[lr]
      
      
  def heappush(self, ele):
    self.n += 1 
    self.hp[self.n] = ele 
    i = self.n 
    
    while i > 1:
      par = i // 2 
      if self.hp[i] > self.hp[par]:
        self.hp[i], self.hp[par] = self.hp[par], self.hp[i]
        i = par
      else:
        break
      
  def heappop(self):
    if self.n == 0: return "No element found"
    ele = self.hp[1]
    self.hp[1] = self.hp[self.n]
    self.n -= 1
    i = 1 
    while i <= self.n:
      ll = 2*i 
      rr = 2*i + 1 
      if ll <= self.n and self.hp[i] < self.hp[ll]:
        self.hp[i] , self.hp[ll] = self.hp[ll], self.hp[i]
        
      elif rr <= self.n and self.hp[i] < self.hp[rr]:
         self.hp[i] , self.hp[rr] = self.hp[rr], self.hp[i]
      else: 
        break 
      
    print("The poppped element is ",ele)
    
    
# l = [54,53,55,52,50]
l = [20,30,40,50,60]
heapq = Heap()
heapq.heapify(l)
print(heapq.hp[1:heapq.n+1]) # [60, 20, 40, 50, 30]
heapq.heappush(55)
print(heapq.hp[1:heapq.n+1]) # [60, 20, 55, 50, 30, 40]
heapq.heappop()
print(heapq.hp[1:heapq.n+1]) # [55, 20, 40, 50, 30]
heapq.heappop()
print(heapq.hp[1:heapq.n+1]) # [40, 20, 30, 50]