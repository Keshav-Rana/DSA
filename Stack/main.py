# stack implementation using linked list
# operations - push, pop, peek

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def __str__(self):
        stack = []
        temp = self.top

        while temp:
            stack.append(str(temp.data))
            temp = temp.next

        return ', '.join(stack)
    
    def push(self, value):
        node = Node(value)

        node.next = self.top
        self.top = node

        self.size += 1

    def pop(self):
        if not self.top:
            raise Exception('Cannot pop from an empty stack')
        
        val = self.top.data
        self.top = self.top.next

        self.size -= 1

        return val

    def peek(self):
        if not self.top:
            raise Exception('Cannot peek in empty stack')
        
        return self.top
    
if __name__ == '__main__':
    # test out stack here
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)

    print(s)
    print(len(s))

    s.pop()
    s.pop()

    print(s)
    print(len(s))