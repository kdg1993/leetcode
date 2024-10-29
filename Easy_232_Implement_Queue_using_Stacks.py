class MyQueue:

    def __init__(self):
        self.main = []
        self.sub = []

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        for i in range(len(self.main)-1):
            self.sub.append(self.main.pop())

        x = self.main.pop()

        for j in range(len(self.sub)):
            self.main.append(self.sub.pop())

        return x

    def peek(self) -> int:
        for i in range(len(self.main)-1):
            self.sub.append(self.main.pop())

        x = self.main.pop()
        self.main.append(x)

        for j in range(len(self.sub)):
            self.main.append(self.sub.pop())

        return x


    def empty(self) -> bool:
        if len(self.main) == 0:
            return True
        else:
            return False       


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()