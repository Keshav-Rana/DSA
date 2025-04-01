# Implemented using Doubly Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularQueue:
    def __init__(self, k):
        self.space = k
        # create left and right dummy nodes
        self.left = Node(-1)
        self.right = Node(-1)
        self.left.next = self.right
        self.right.prev = self.left

    def enqueue(self, value):
        # check if the ll is empty
        if self.space <= 0:
            return False
        
        newNode = Node(value)
        newNode.next = self.right
        newNode.prev = self.right.prev

        self.right.prev.next = newNode
        self.right.prev = newNode

        self.space -= 1

        return True

    def dequeue(self):
        if self.isEmpty():
            return False
        
        self.left.next = self.left.next.next
        self.left.next.prev = self.left

        self.space += 1

        return True
    
    def peekFront(self):
        # first check the queue is not empty
        if self.isEmpty():
            return -1
        
        return self.left.next.val

    def peekRear(self):
        if self.isEmpty():
            return -1
        
        return self.right.prev.val

    def isEmpty(self):
        return self.left.next == self.right
    
    def printQueue(self):
        if not self.isEmpty():
            # start from head and print all elements
            head = self.left.next
            # don't print the last node
            while head.next:
                print(head.data, end = ' ')
                head = head.next

if __name__ == '__main__':
    pass
    # test out Circular Queue here
    q = CircularQueue(4)

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    q.printQueue()
    print('\n')

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.printQueue()