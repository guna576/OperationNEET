# https://leetcode.com/problems/online-stock-span/description/

class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, p: int) -> int:
        c = 1
        while self.st and self.st[-1][0] <= p:
            c += self.st.pop()[1]

        self.st += [(p,c)]
        return c


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# you are taking the count of number of poped items and and putting it as key value while inserting

# Monatonic stack