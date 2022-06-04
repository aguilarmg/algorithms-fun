class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

    def setParent(self, p):
        self.parent = p

    def setLeftChild(self, left):
        self.left = left

    def setRightChild(self, right):
        self.right = right

    def getParent(self):
        return self.parent
        
    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def __str__(self):
        parent_val = "None" if not self.parent else self.parent.val
        left_child_v = "None" if not self.left else self.left.val
        right_child_v = "None" if not self.right else self.right.val
        return f"Value: {self.val}, Parent: {parent_val}, Left Child: {left_child_v}, Right Child: {right_child_v}"

    def __repr__(self):
        parent_val = "None" if not self.parent else self.parent.val
        left_child_v = "None" if not self.left else self.left.val
        right_child_v = "None" if not self.right else self.right.val
        return f"Value: {self.val}, Parent: {parent_val}, Left Child: {left_child_v}, Right Child: {right_child_v}"

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """
        Runtime: O(height(BST))
        """
        newNode = Node(val, None, None, None)
        if not self.root:
            # If the tree is empty, create a new node and set it as the root
            self.root = newNode
        else:
            """
            Start at the root node.
            Repeatedly traverse left and right child pointers, until a null
            pointer is encountered.
            Replace the null pointer with one to the new object. Set the new
            node's parent pointer to its parent, and its child pointers to None.
            """
            curr = self.root
            parent = None
            setLeftChild = False
            while curr:
                parent = curr
                if val <= curr.val:
                    setLeftChild = True
                    curr = curr.left
                else:
                    setLeftChild = False
                    curr = curr.right
            newNode.setParent(parent)
            if setLeftChild:
                parent.setLeftChild(newNode)
            else:
                parent.setRightChild(newNode)
    
    def _outputSorted(self, x):
        if not x:
            return " "
        return (self._outputSorted(x.left) + str(x.val)
    + self._outputSorted(x.right))

    def outputSorted(self):
        ret =  self._outputSorted(self.root)
        print(f"{ret}")

    def _min(self, x):
        """
        Start at x and traverse the left child pointers until you encounter
        a null left child pointer.
        """
        curr = x
        while curr.left:
            curr = curr.left
        return curr

    def getMin(self):
        """
        Start at x and traverse the left child pointers until you encounter
        a null left child pointer.
        """
        return self._min(self.root) 

    def _max(self, x):
        """
        Start at x and traverse the right child pointers until you encounter
        a null right child pointer.
        """
        curr = x
        while curr.right:
            curr = curr.right
        return curr

    def getMax(self):
        """
        Start at x and traverse the right child pointers until you encounter
        a null right child pointer.
        """
        return self._max(self.root) 

    def _search(self, node, val):
        curr = node
        while curr:
            if val == curr.val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def search(self, val):
        return self._search(self.root, val)

    def delete(self, val):
        """
        For a key `val`, delete an object with key `val` from the data structure, if one exists.
        """
        node = self.search(val)
        if not node:
            return
        # Three cases:
        # node has 0 children
        if not node.left and not node.right:
            # If node has 0 children, just remove it from the tree.
            p = node.parent
            if not p:
                # This would be the case where the tree is literally just one
                # node and it is the one being removed.
                self.root = None
                return
            if (p.left == node):
                p.left = None
            else:
                p.right = None
            return
        
        # node has 1 child 
        if (node.left and not node.right) or (not node.left and node.right):
            child = node.left if node.left else node.right
            p = node.parent
            if not p:
                self.root = child
            # Set the child's parent as the removee's parent
            child.parent = p
            # Set the parent's child pointers to the removee's child
            if (node == p.left):
                p.left = child
            else:
                p.right = child
            return

        # node has 2 children

def main():
    tree = BST()
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)
    tree.insert(5)
    tree.insert(4)
    tree.insert(0)
    tree.outputSorted()
    print(f"How is the 3 node configured before deleting its child? : {tree.search(3)}")
    print(f"How is the 4 node configured before deleting its parent?: {tree.search(4)}")
    tree.delete(5)
    tree.outputSorted()
    print(f"How is the 3 node configured after deleting its child?  : {tree.search(3)}")
    print(f"How is the 4 node configured after deleting its parent? : {tree.search(4)}")


if __name__=='__main__':
    main()
