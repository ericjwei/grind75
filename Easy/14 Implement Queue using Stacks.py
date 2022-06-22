class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        temp = []
        for _ in range(len(self.stack)):
            temp.append(self.stack.pop(-1))
        self.stack.append(x)
        for _ in range(len(temp)):
            self.stack.append(temp.pop(-1))

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return None if self.empty() else self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0

q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(*q.stack)

