class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# duplicates allowed
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertNodeHelper(self, root, data):
        if not root:
            return TreeNode(data)
        
        # check left and right subtrees
        if data <= root.data:
            root.left = self.insertNodeHelper(root.left, data)

        else:
            root.right = self.insertNodeHelper(root.right, data)

        return root
    
    def insertNode(self, data):
        if not self.root:
            self.root = TreeNode(data)
        
        else:
            self.root = self.insertNodeHelper(self.root, data)

    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.left)
        print(root.data, end = " ")
        self.inorder(root.right)

    def preorder(self, root):
        if not root:
            return
        
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if not root:
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    # returns node with minimum value in the tree
    def findMinimum(self, root):
        if root:
            while root.left:
                root = root.left

        # return node with smallest value
        return root

    def deleteNodeHelper(self, root, data):
        # base case - found the node to delete
        if root.data == data:
            # leaf node
            if not root.left and not root.right:
                root = None
                return root
            
            # node with one child (left)
            elif root.left and not root.right:
                root = root.left
                return root
            
            # node with one child (right)
            elif root.right and not root.left:
                root = root.right
                return root
            
            # node with two or more children
            elif root.left and root.right:
                # find the minimum node in the right subtree and swap that with root
                minNodeInRight = self.findMinimum(root.right)
                root.data = minNodeInRight.data
                # delete the minimum node in right subtree and update the right subtree
                root.right = self.deleteNodeHelper(root.right, minNodeInRight.data)
                return root
            
        # find the node to delete in left and right subtree
        if data < root.data:
            root.left = self.deleteNodeHelper(root.left, data)

        else:
            root.right = self.deleteNodeHelper(root.right, data)

        return root
    
    def deleteNode(self, data):
        if not self.root:
            raise Exception("cannot delete in empty tree")
        
        self.root = self.deleteNodeHelper(self.root, data)


if __name__ == "__main__":
    # Test out binary search tree here
    bt = BinarySearchTree()

    bt.insertNode(4)
    bt.insertNode(2)
    bt.insertNode(6)
    bt.insertNode(1)
    bt.insertNode(3)
    bt.insertNode(5)
    bt.insertNode(7)

    bt.inorder(bt.root)
    print('\n')

    bt.deleteNode(6)

    bt.inorder(bt.root)
    print('\n')

    smallestNode = bt.findMinimum(bt.root)
    print(smallestNode.data)


