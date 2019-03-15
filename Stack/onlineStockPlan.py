https://leetcode.com/problems/online-stock-span/
class StockSpanner:


    def __init__(self):
        self.stack = []
        
    #find first item on left that is strick greater than current
    #descending stack
    #we save [price, currentLeftSpan]
    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            prevRes = self.stack.pop()
            res += prevRes[1]
        self.stack.append([price, res])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

    def __init__(self):
        self.stack = []

    def next(self, price):
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res