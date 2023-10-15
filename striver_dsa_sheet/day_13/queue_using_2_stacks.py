class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1 += [x]

    def pop(self) -> int:
        if not self.s2:
            self.fill()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            self.fill()
        peekEle = self.s2.pop()
        self.s2 += [peekEle]
        return peekEle

    def empty(self) -> bool:
        return not len(self.s1) and not len(self.s2)

    def fill(self):
        while self.s1:
            self.s2 += [self.s1.pop()]
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()