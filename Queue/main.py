# queue implementation using linked list to achieve constant complexity for most operations
# methods to define - len, print, enqueue, dequeue, peek

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        # two pointers to keep track of the rear and front
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def __str__(self):
        queue = []
        temp = self.front
        while temp:
            queue.append(str(temp.data))
            temp = temp.next

        return ', '.join(queue)
    
    def enqueue(self, value):
        # if queue is empty
        if not self.rear:
            self.front = self.rear = Node(value)
            self.size += 1
            return

        # insert at the end
        node = Node(value)
        self.rear.next = node
        self.rear = self.rear.next

        self.size += 1

    def dequeue(self):
        if not self.front:
            raise Exception('Cannot dequeue from empty queue.')
        
        val = self.front.data
        self.front = self.front.next
        # edge case, we only had one element in the queue, handle the rear as well
        if not self.front:
            self.rear = None

        self.size -= 1

        return val

    def peek(self):
        if self.front:
            return self.front.data
        
        raise Exception('Cannot peek in an empty queue')

if __name__ == '__main__':
    # test out queue here
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q)
    print(len(q))

    q.dequeue()
    q.dequeue()

    # print(q.peek())
    print(len(q))

    print(q)

    q.dequeue()