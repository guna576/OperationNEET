### using single queue
class MyStack:

    def __init__(self):
        self.que = []

    def push(self, x: int) -> None:
        size = len(self.que)
        self.que += [x]
        for _ in range(size):
            self.que += [self.que.pop(0)]

    def pop(self) -> int:
        return self.que.pop(0)

    def top(self) -> int:
        return self.que[0]

    def empty(self) -> bool:
        return len(self.que) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



### Stack using 2 queues wooooooooooooooooooooooooooooooooah

class MyStack:

    def __init__(self):
        self.que1 = []
        self.que2 = []

    def push(self, x: int) -> None:
        self.que2 += [x]
        while self.que1:
            self.que2 += [self.que1.pop(0)]
        self.que1, self.que2 = self.que2, self.que1

    def pop(self) -> int:
        return self.que1.pop(0)

    def top(self) -> int:
        return self.que1[0]

    def empty(self) -> bool:
        return len(self.que1) == 0
