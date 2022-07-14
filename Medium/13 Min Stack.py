class MinStack:
    def __init__(self):
        self.trackMin = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.trackMin[-1] if self.trackMin else val)
        self.trackMin.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.trackMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.trackMin[-1]
    
s = MinStack()
s.push(2)


# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.minStack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         val = min(val, self.minStack[-1] if self.minStack else val)
#         self.minStack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()
#         self.minStack.pop()

#     def top(self) -> int:
#         self.stack[-1]
    
#     def getMin(self) -> int:
#         return self.minStack[-1]
    
# s = MinStack()
# s.push(-2)
# s.push(0)
# s.push(-3)
# print(s.getMin())
# s.pop()
# print(s.getMin())