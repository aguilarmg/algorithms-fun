from utils import genFrequencyMap
from heapq import heappush, heappop

class Node:
    def __init__(self, char, parent=None, left=None, right=None, p_a=float('inf')):
        self.label = char
        self.parent = parent
        self.left = left
        self.right = right
        self.p_a = p_a

    def __lt__(self, y):
        return self.p_a < y.p_a

    def __str__(self):
        left_child_v = "None" if not self.left else self.left.label
        right_child_v = "None" if not self.right else self.right.label
        return f"Label: {self.label}, Frequency: {self.p_a}, Left: {left_child_v}, Right: {right_child_v}"

def genPrefixTree(freq):
    insert = heappush
    extractMin = heappop

    forest = []
    for char in freq.keys():
        newLeaf = Node(char, p_a=freq[char])
        insert(forest, newLeaf)

    # for leaf in forest:
    #     print(leaf)

    while len(forest) > 1:
        # Get the two lowest freq trees
        T_1 = extractMin(forest)
        T_2 = extractMin(forest)

        sum_p_a = T_1.p_a + T_2.p_a
        T_3 = Node(char=None, parent=None, left=T_2, right=T_1, p_a=sum_p_a)
        insert(forest, T_3)

    return extractMin(forest)

def decode(code, prefixTreeRoot):
    node_pointer = prefixTreeRoot
        
    decoded_str = ""
 
    for b in code:
        print(f"{node_pointer}")
        print(f"{b}")
        if b == '0':
            node_pointer = node_pointer.left
            print(node_pointer)
        else:
            node_pointer = node_pointer.right
        if (not node_pointer.left and not node_pointer.right):
            # we're at a leaf
            print(f"Label of this leaf: {node_pointer.label}")
            decoded_str += node_pointer.label
            node_pointer = prefixTreeRoot
    return decoded_str

def main():
    # test_str = 12*"A" + 5*"B" + 2*"C" + 1*"D"
    test_str = 3*"A" + 2*"B" + 6*"C" + 8*"D" + 2*"E" + 6*"F"
    freq = genFrequencyMap(test_str)
    prefixTreeRoot = genPrefixTree(freq) 
    decoded_str = decode("010110111", prefixTreeRoot)
    print(f"Look at this decoded string: {decoded_str}")


    



if __name__=='__main__':
    main()
