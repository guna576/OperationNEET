class MinStack:
    def __init__(self):
        self.items = []
        self.min = []

    def push(self, val: int) -> None:
        if not self.items:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)
        
        self.items.append(val)
        
    def pop(self) -> None:
        if self.items[-1] == self.min[-1]:
            self.min.pop()
        self.items.pop()
        
    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min[-1]
    
# Creating an extra stack which should have only min element 
# we are only pushing min element compared to last pushed ele in min stack (increasing order)
# WE dont push if bigger element comes stack becoz the pop wont effect this min stack
# O(N) and O(1)


class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if not self.s:
            self.s += [[val,val]]
        else:
            minEle = val if val < self.s[-1][-1] else self.s[-1][-1]
            self.s += [[val,minEle]]

    def pop(self) -> None:
        return self.s.pop()[0]

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][-1]

# O(2N) still because of pair in stack, but this is very simple