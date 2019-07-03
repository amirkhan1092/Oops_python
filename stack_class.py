class Stack:
    'this is stack repr '
    def __init__(self):
        self.stack = list()
        # print('Mandeep sir love xxxxx mam')

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        return self.stack[-1]
    def __str__(self):
        return str(self.stack)


sst = Stack()

sst.push(2)
sst.push(5)
sst.push(7)
sst.pop()
print(sst.peek())
print(sst)