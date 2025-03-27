class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0 # makes it easy to handle deletion and insertion

    def insertNode(self, value, pos):
        # handle three cases - inserting at head, middle, and tail
        # head
        if pos == 0:
            node = Node(value)
            node.next = self.head
            self.head = node

            self.size += 1

        # tail
        elif pos == self.size:
            temp = self.head
            while temp.next:
                temp = temp.next

            node = Node(value)
            temp.next = node
            node.prev = temp

            self.size += 1

        # insert a middle node
        else:
            # validate position
            if pos >= 0 and pos < self.size:
                # print(f"Position requested: {pos}")

                temp = self.head
                i = 0
                while i < pos-1 and temp:
                    temp = temp.next
                    i += 1

                node = Node(value)
                nextNode = temp.next
                # integrate new node with previous node
                temp.next = node
                node.prev = temp
                # integrate new node with next node
                node.next = nextNode
                nextNode.prev = node

                self.size += 1  

            else:
                raise Exception('Invalid position for inserting a node') 

    def deleteNode(self, pos):
        # three cases - delete at head, delete in middle, delete at tail
        if pos == 0:
            raise Exception('Not a valid position')
        # head
        elif pos == 1:
            if self.head:
                self.head = self.head.next
                self.size -= 1

        # deleting at tail
        elif pos == self.size:
            temp = self.head
            i = 1
            # iterate till second last node
            while i < pos-1:
                temp = temp.next
                i += 1

            if temp.next:
                nextNode = temp.next
                temp.next = None
                nextNode.prev = None
            
            self.size -= 1
        
        # middle node
        else:
            if pos > 0 and pos <= self.size:
                temp = self.head
                i = 1
                while i < pos-1:
                    temp = temp.next
                    i += 1

                nodeToPointTo = temp.next.next
                # connect curr node with next available node
                temp.next = nodeToPointTo
                nodeToPointTo.prev = temp

                self.size -= 1



    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

if __name__ == '__main__':
    # test out doubly linked list here
    '''When inserting node the position index starts from 0. 
       When deleting node the position index starts from 1.'''
    dl = DoublyLinkedList()

    dl.insertNode(1, 0)
    dl.insertNode(2, 1)
    dl.insertNode(4, 0)
    dl.insertNode(5, 3)
    dl.insertNode(6, 1)
    dl.insertNode(7, 2)
    
    dl.traverse()
    print('\n')

    dl.deleteNode(1)
    dl.deleteNode(5)
    dl.deleteNode(3)
    dl.deleteNode(2)
    dl.deleteNode(2)
    dl.deleteNode(1)
    dl.traverse()