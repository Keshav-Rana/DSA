class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def BFS(self, root):
        if not root:
            return
        
        # initialise queue with root value
        queue = [root]
        
        # pop value in the front of queue and check its left and right child and repeat
        while len(queue) > 0:
            front_node = queue[0]
            front_val = front_node.data
            queue.pop(0)
            print(front_val)

            if front_node.left:
                queue.append(front_node.left)

            if front_node.right:
                queue.append(front_node.right)

if __name__ == "__main__":
    # test binary tree here
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt.root.right.left = Node(6)
    bt.root.right.right = Node(7)

    bt.BFS(bt.root)

