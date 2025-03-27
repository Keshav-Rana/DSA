class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        # to keep track of size of linked list
        self.size = 0

    def insert_at_head(self, val):
        if not self.head:
            node = Node(val)
            self.head = node
            self.size += 1

        else:
            node = Node(val)
            node.next = self.head
            self.head = node
            self.size += 1

    def insert_at_tail(self, val):
        if not self.head:
            node = Node(val)
            self.head = node
            self.size += 1

        else:
            # iterate till the last node
            temp = self.head
            while temp.next:
                temp = temp.next
            
            node = Node(val)
            temp.next = node
            self.size += 1

    # not zero based
    def insert_at_position(self, val, pos):
        # validate position
        if (pos > 0 and pos <= self.size):
            temp = self.head
            node = Node(val)
            for i in range(0, pos-1):
                temp = temp.next

            if temp.next:
                node.next = temp.next
                temp.next = node

            else:
                self.insert_at_tail(val)
            
        # edge case - list is empty and position is 1
        elif (self.size == 0 and pos == 1):
            self.insert_at_tail(val)

        else:
            raise Exception('Invalid position')

    def delete_at_head(self):
        # list has to have something in order to delete
        if self.head:
            self.head = self.head.next
            self.size -= 1

    def delete_at_tail(self):
        # edge case
        if self.head and self.size == 1:
            self.head = None
            self.size -= 1

        elif self.head:
            temp = self.head
            while temp.next.next:
                temp = temp.next

            temp.next = None
            self.size -= 1

    def delete_at_position(self, pos):
        # edge case - delete first node
        if (pos == 1 and self.size >= 1):
            self.head = self.head.next
            self.size -= 1
            return

        # validate position
        if (pos > 0 and pos <= self.size):
            temp = self.head
            prev = self.head
            for i in range(0, pos-1):
                prev = temp
                temp = temp.next

            if temp.next:
                prev.next = temp.next
                self.size -= 1

            else:
                prev.next = None
                self.size -= 1
                
        
        else:
            raise Exception('Invalid position')

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

        print(f'Size of LinkedList: {self.size}')

if __name__ == '__main__':
    # try out Linked List here
    ll = LinkedList()

    ll.insert_at_tail(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    ll.insert_at_tail(4)
    ll.print_list()

    ll.delete_at_position(1)
    ll.print_list()

    ll.delete_at_position(2)
    ll.print_list()

    ll.delete_at_position(2)
    ll.print_list()

    ll.delete_at_position(1)
    ll.print_list()