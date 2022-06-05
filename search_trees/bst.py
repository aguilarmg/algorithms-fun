from collections import deque

class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self.size = 1

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
        return f"Value: {self.val}, Parent: {parent_val}, Left Child: {left_child_v}, Right Child: {right_child_v}, Size: {self.size}"

    def __repr__(self):
        parent_val = "None" if not self.parent else self.parent.val
        left_child_v = "None" if not self.left else self.left.val
        right_child_v = "None" if not self.right else self.right.val
        return f"Value: {self.val}, Parent: {parent_val}, Left Child: {left_child_v}, Right Child: {right_child_v}, Size: {self.size}"

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """
        Runtime: O(height)
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
                curr.size += 1
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

    def _search(self, node, val):
        """
        Runtime: O(height)
        """
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
        Runtime: O(height)
        """
        node = self.search(val)
        if not node:
            return

        # If node has two children
        if node.left and node.right:
            # get the predecessor of node
            pre = self.predecessor(node)

            # Swap the two nodes by simply swapping their values and have 
            # `node` now point to where its predecessor was.
            tmp = pre.val
            pre.val = node.val
            node.val = tmp

            node = pre

        # If node has 0 children
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
        
        # If node has 1 child 
        if (node.left and not node.right) or (not node.left and node.right):
            child = node.left if node.left else node.right
            p = node.parent
            if not p:
                self.root = child
                child.parent = None
                return
            # Set the child's parent as the removee's parent
            child.parent = p
            # Set the parent's child pointers to the removee's child
            if (node == p.left):
                p.left = child
            else:
                p.right = child
            return

    def predecessor(self, x):
        """
        Get the predecessor of an object `x`.
        If `x` has a left subtree, return the `MAX` of the left subtree.
        Otherwise, traverse upwards towards the root. If you encounter two
        consecutive nodes `y` and `z`, where `y` is the right child of `z`, return `z`.

        Runtime: O(height)
        """
        if not x:
            print(f"This is a null node!")
            return 
        if x.left:
            return self._max(x.left)
        else:
            curr = x
            parent = x.parent
            while parent:
                if curr == parent.right:
                    return parent
                tmp = parent.parent
                curr = parent
                parent = tmp

    def successor(self, x):
        """
        Get the successor of an object `x`.
        If `x` has a left subtree, return the `MAX` of the left subtree.
        Otherwise, traverse upwards towards the root. If you encounter two
        consecutive nodes `y` and `z`, where `y` is the left child of `z`, return `z`.

        Runtime: O(height)
        """
        if not x:
            print(f"This is a null node!")
            return
        if x.right:
            return self._min(x.right)
        else:
            curr = x
            parent = x.parent
            while parent:
                if curr == parent.left:
                    return parent
                tmp = parent.parent
                curr = parent
                parent = tmp
    
    def _outputSorted(self, x):
        if not x:
            return " "
        return (self._outputSorted(x.left) 
                + str(x.val) 
                + self._outputSorted(x.right))

    def outputSorted(self):
        """
        Runtime: O(n)
        """
        ret =  self._outputSorted(self.root)
        print(f"{ret}")

    def _min(self, x):
        """
        Start at x and traverse the left child pointers until you encounter
        a null left child pointer.
        Runtime: O(height)
        """
        curr = x
        while curr.left:
            curr = curr.left
        return curr

    def getMin(self):
        """
        Start at x and traverse the left child pointers until you encounter
        a null left child pointer.
        Runtime: O(height)
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

    def levelTraversal(self):
        queue = deque()
        queue.append(self.root)

        while queue:
            n = len(queue)
            level_str = ""
            for _ in range(n):
                curr = queue.popleft()
                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
                    level_str += str(curr.val)
                else:
                    level_str += "N"
                level_str += " "
            print(f"{level_str}")

    def _select(self, node, i):
        if node.left:
            j = node.left.size
        else:
            j = 0
        
        if i == j+1:
            return node
        elif i <= j+1:
            # Must look in the left subtree
            return self._select(node.left, i)
        else:
            # Must look in the right subtree
            return self._select(node.right, i-j-1)

    def select(self, i):
        """
        Given a number i, between 1 and the number of objects, return a pointer
        to the object in the data structure with the ith smallest key.
        """
        return self._select(self.root, i)

def main():
    tree = BST()
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)
    tree.insert(5)
    tree.insert(4)
    tree.outputSorted()
    tree.levelTraversal()
    print(f"Tree Root Before Deletion: {tree.root}")
    tree.delete(3)
    print(f"Tree Root After Deletion: {tree.root}")
    tree.outputSorted()
    tree.levelTraversal()


if __name__=='__main__':
    main()
