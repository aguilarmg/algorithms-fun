class Heap:
    def __init__(self):
        """
        For every object `x`, the key of `x` is less than or equal to the keys
        of its children.
        """
        self.heap = []
        self.N = 0

    def insert(self, val):
        """
        Insert `val` into self.heap, without violating the heap property.
        1. Stick the new object at the end of the heap and increment the heap
           size.
        2. Repeatedly swap the new object with its parent until the heap
           property is restored.

        Runtime: O(logN)
        """
        self.heap.append(val)
        c_index = self.N # Index of the latest object in the heap array
        if c_index > 0:
            # The concept of the parent of the new node only exists if this
            # isn't the first node that we are inserting.

            # Calculate the parent index
            p_index = (c_index-1)//2
            
            while self.heap[p_index] > self.heap[c_index]:
                # There is a violation of the heap property.
                # Swap the objects.
                tmp = self.heap[p_index]
                self.heap[p_index] = self.heap[c_index]
                self.heap[c_index] = tmp

                # Now update the indices of the child and parent and reevaluate for
                # any violations.
                c_index = p_index
                p_index = (c_index-1)//2

            # Increment the heap size.
        self.N += 1
        print(f"insert    : Current state of the heap: ({self.N}): {self.heap}")

    def extractMin(self):
        """
        Given a heap H, remove and return from H an object with the smallest
        key.
        self.heap[0] is guaranteed to be the object with the smallest key.
        However, we must ensure that once self.heap[0] is removed, the 
        heap is still full and still satisfies the heap property.

        1. Overwrite the root with the last object `x` in the heap, and
           decrement the heap size.
        2. Repeatedly swap `x` with its smaller child until the heap property is
           restored.

        Runtime: O(logN)
        """
        if self.N == 0:
            print(f"This heap is empty. There is nothing to return from it.")
            return

        minNode = self.heap[0]

        if self.N == 1:
            # There was only one element in this heap.
            # Removing it yields an empty heap.
            self.heap = []
            self.N = 0
        elif self.N > 1:
            # Overwrite the root with the last object `x` in the heap
            self.heap[0] = self.heap[self.N-1] 
            # Remove the last item from the heap.
            self.heap.pop()
            self.N -= 1

            p_index = 0
            # Calculate the children indices
            l_c_index = 2*p_index+1
            r_c_index = 2*p_index+2

            while (self.heap[p_index] > self.heap[l_c_index] 
                    or self.heap[p_index] > self.heap[r_c_index]):
                # Determine smaller child
                if self.heap[l_c_index] < self.heap[r_c_index]:
                    smaller_c_index = l_c_index
                else:
                    smaller_c_index = r_c_index

                # Swap the objects.
                tmp = self.heap[p_index]
                self.heap[p_index] = self.heap[smaller_c_index]
                self.heap[smaller_c_index] = tmp

                # Update the indices of the child and parent and reevaluate for any
                # violations
                p_index = smaller_c_index
                l_c_index = 2*p_index + 1
                r_c_index = 2*p_index + 2

                # No need to continue if you've reached the lowest level of the
                # tree.
                if l_c_index > self.N or r_c_index > self.N:
                    break

        print(f"extractMin: Current state of the heap: ({self.N}): {self.heap}")
        return minNode

    def findMin(self):
        """
        Given a heap H, return an object with the smallest key.
        """
        return self.heap[0]

def main():
    heap = Heap()
    heap.insert(4)
    heap.insert(4)
    heap.insert(8)
    heap.insert(9)
    heap.insert(4)
    heap.insert(12)
    heap.insert(9)
    heap.insert(11)
    heap.insert(13)
    heap.insert(7)
    heap.insert(10)
    heap.insert(5)
    heap.extractMin()

if __name__=='__main__':
    main()
