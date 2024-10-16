from random import sample, randint
from math import log, floor

# ! TODO: Hash Map, Bit Mask, Sliding Window, Backtracing, DFS, BFS, Dijkstra's, Bellman-Ford, KNP, Kruskal's, Prim's, Topological Sort, Floyd Warshall's, Dynamic Programming, Kth Smallest Element (O(n) using divide and conquer), Huffman Coding Tree, Flow Network

# ~ IN PROGRESS: Adjacency List, Adjacency Matrix

# * DONE: Node, Stack, Queue, Linked List, Circular Doubly-linked List, Binary Search Tree, Heap, Binary Search, Insertion Sort, Heap Sort, Quicksort, Merge Sort

def main() -> None:

    array = sample(range(0, 15), 10)
    target = randint(0, 15)

    print(f"\033[95m{"INSERTION SORT ||"}\033[00m", end = " ")
    print(f"Input: {array} | Output:", insertion_sort(array.copy()))

    print(f"\033[95m{"HEAP SORT ||"}\033[00m", end = " ")
    print(f"Input: {array} | Output:", heap_sort(array.copy()))

    print(f"\033[95m{"QUICKSORT ||"}\033[00m", end = " ")
    print(f"Input: {array} | Output:", quicksort(array, 0, len(array) - 1))

    print(f"\033[95m{"MERGE SORT ||"}\033[00m", end = " ")
    print(f"Input: {array} | Output:", merge_sort(array))

    print(f"\033[95m{"BINARY SEARCH RECURSIVE ||"}\033[00m", end = " ")
    print(f"Array: {array} | Target: {target} | Found at index:", 
          binary_search_recursive(array, target, 0, len(array) - 1))
    
    print(f"\033[95m{"BINARY SEARCH ITERATIVE ||"}\033[00m", end = " ")
    print(f"Array: {array} | Target: {target} | Found at index:", 
          binary_search_iterative(array, target, 0, len(array) - 1))

# This class implements a stack using a list
class Stack():
    def __init__(self) -> None: self.stack = []
    def empty(self) -> bool: return len(self.stack) == 0
    def size(self) -> int: return len(self.stack)
    def top(self) -> int: return self.stack[len(self.stack) - 1]
    def push(self, x) -> None: self.stack.append(x)
    def pop(self) -> int: 
        if not self.empty(): 
            output = self.stack[-1]
            self.stack.pop(-1)
            return output

# This class implements a queue using a list
class Queue():
    def __init__(self) -> None: self.queue = []
    def front(self) -> int: 
        if len(self.queue) != 0:
            return self.queue[0]
    def back(self) -> int: 
        if len(self.queue) != 0:
            return self.queue[-1]
    def enqueue(self, x) -> None: 
        self.queue.append(x)
    def dequeue(self) -> int:
        output = self.queue[-1]
        self.queue.pop()
        return output

# This class implements a graph node with a value and left and right pointers
class Node():
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# This class implements a linked list of nodes
class Linked_List():
    def __init__(self, head=None) -> None:
        self.head = head

    def size(self) -> int:
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.right
        return count
    
    def insert(self, val) -> None:
        node = Node(val)
        if not self.head: 
            self.head = node
            return
        temp = self.head
        while temp.right:
            temp = temp.right
        temp.right = node
    
    def delete(self, val) -> Node:
        if not self.head: return None
        elif self.head == val:
            node = self.head
            self.head = self.head.right
            return node
        parent = self.head
        node = self.head.right
        while node:
            if node.val == val:
                parent.right = node.right
                return node
            parent = node
            node = node.right
        return None
                
    def reverse(self) -> None:
        if not self.head: return
        p1 = None
        p2 = self.head.right
        while self.head:
            self.head.right = p1
            p1 = self.head
            self.head = p2
            if p2: p2 = p2.right
        self.head = p1

    def print(self) -> None:
        node = self.head
        while node: 
            print(node.val, end=" ")
            node = node.right
        print()

# This class implements a circular doubly-linked list of nodes
class Circular_Doubly_linked_list():
    def __init__(self, head=None) -> None:
        self.head = head
    
    def size(self) -> int:
        if not self.head: return 0
        count = 1
        temp = self.head.right
        while temp != self.head:
            count += 1
            temp = temp.right
        return count

    def insert(self, val):
        node = Node(val)
        if not self.head: 
            node.right = node
            node.left = node
            self.head = node
            return
        
        node.right = self.head
        node.left = self.head.left
        self.head.left = node
        node.left.right = node

    def delete(self, val) -> Node:

        # deleting root
        if not self.head: return None
        elif self.head.val == val and self.head.right == self.head:
            node = self.head
            self.head = None
            return node
        elif self.head.val == val:
            node = self.head
            self.head = self.head.right
            self.head.left = node.left
            node.left.right = self.head
            return node

        node = self.head.right
        while node != self.head:
            if node.val == val:
                node.left.right = node.right
                node.right.left = node.left
                return node
            node = node.right
        return None

    def print(self) -> None:
        if not self.head: return
        print(self.head.val, end=" ")
        node = self.head.right
        while node != self.head:
            print(node.val, end=" ")
            node = node.right
        print()

# This class implements a binary search tree data structure with insertion, deletion, traversal, searching, and re-balancing
class BST():
    def __init__(self, root=None) -> None:
        self.root = root

    def insert(self, val) -> None:
        node = Node(val)
        if not self.root: self.root = node
        else:
            i = self.root
            while i.left != node and i.right != node:
                if node.val <= i.val:
                    if i.left: i = i.left
                    else: i.left = node
                else:
                    if i.right: i = i.right
                    else: i.right = node

    def delete(self, val=None) -> bool:
        if val == None:
            self.root = None
            return True
        elif not self.root: return False

        parent = None
        i = self.root
        while i and i.val != val: # finding target value
            parent = i
            if val <= i.val: i = i.left
            else: i = i.right
        if not i: return False

        # helper function for replacing the node i with its predecessor
        def replace_predecessor(i, parent) -> None:
            j = i.left
            if not j.right: # predecessor has no right child, replace i with it
                if parent and parent.left == i: parent.left = j
                elif parent: parent.right = j
                else: self.root = j
                j.right = i.right
            else:
                print(True)
                while j.right:
                    j_parent = j
                    j = j.right
                j_parent.right = j.left # remove predecessor

                # replace i with predecessor
                if parent and parent.left == i: parent.left = j
                elif parent: parent.right = j
                else: self.root = j
                j.left = i.left
                j.right = i.right

        if not parent: # deleting root node
            if not i.left or not i.right:
                self.root = i.left if i.left else i.right
            else:
                replace_predecessor(i, None)

        # deleting a node with less than 2 children
        elif not i.left or not i.right:
            if parent.left == i: parent.left = i.left if i.left else i.right
            else: parent.right = i.right if i.right else i.left

        else: # replace node with predecessor (can be successor)
            replace_predecessor(i, parent)

        return True
    
    # traverse() prints the tree traversal in pre-order, in-order, or post-order
    def traverse(self, node, pre=False, post=False) -> Node:
        if not node: return
        if pre and not post: # pre-order
            print(node.val, end=" ")
            self.traverse(node.left, pre=pre)
            self.traverse(node.right, pre=pre)
        elif post and not pre: #post-order
            self.traverse(node.left, post=post)
            self.traverse(node.right, post=post)
            print(node.val, end=" ")
        else: # in-order
            self.traverse(node.left)
            print(node.val, end=" ")
            self.traverse(node.right)
        if node == self.root: print()
        return node
    
    def search(self, val) -> Node:
        i = self.root
        while i:
            if val == i.val: return i
            elif val < i.val: i = i.left
            else: i = i.right
        return None
    
    # balance() uses the Day–Stout–Warren algorithm to form a complete BST: 
    # https://en.wikipedia.org/wiki/Day%E2%80%93Stout%E2%80%93Warren_algorithm
    def balance(self):
        if not self.root: return
        pseudo_root = Node(right=self.root)
        size = 0 # number of elements in the tree
        tail = pseudo_root # the node at the end of the sorted linked list
        rest = pseudo_root.right # root node of remaining tree to be converted
        while rest: 
            
            # no left node means we have a linked list of sorted nodes up to node rest, so proceed to the remaining unconverted tree
            if not rest.left:
                tail = rest
                rest = rest.right
                size += 1 # update size as rest traverses the linked list
            
            # rotate the node to the left of rest to be the parent, putting it in sorted order and in a linked list
            else:
                temp = rest.left
                rest.left = temp.right
                temp.right = rest
                rest = temp
                tail.right = temp

        # helper function that rotates a tree (in the form of a vine) into a complete tree by using the known number of nodes at a height, count, in a complete tree and rotating count number of nodes into that level
        def compress(root, count) -> None:
            scanner = root
            for _ in range(count): # rotates nodes to the left
                child = scanner.right
                scanner.right = child.right
                scanner = scanner.right
                child.right = scanner.left
                scanner.left = child
            
        # number of leaves in the bottom level of a complete tree
        # leaves = size + 1 − 2^{⌊log2(size + 1)⌋}
        leaves = size + 1 - pow(2, floor(log(size + 1, 2)))
        compress(pseudo_root, leaves)
        size = size - leaves # number of leaves one level up
        while size > 1:
            compress(pseudo_root, size // 2)
            size = size // 2
        self.root = pseudo_root.right

# This class implements a min heap using a list
class Min_Heap():
    def __init__(self, heap=None) -> None:
        if not heap: self.heap = []
        else: 
            self.min_heapify(heap)
            self.heap = heap
        
    def min_heapify(self, heap) -> None:
        n = (len(heap) - 1) // 2
        for i in range(n, -1, -1):
            self.sink_down(heap, i)

    def insert(self, val) -> None:
        self.heap.append(val)
        self.swim_up(self.heap, len(self.heap) - 1)
    
    def delete(self, val) -> bool:
        try: index = self.heap.index(val)
        except ValueError: return False
        self.heap[index] = float('-inf')
        self.swim_up(self.heap, index)
        self.pop()
        return True
    
    def pop(self) -> int:
        if not self.heap or len(self.heap) < 1: return None
        ret = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.sink_down(self.heap, 0)
        return ret
    
    def peek(self) -> int:
        if not self.heap or len(self.heap) < 1: return None
        return self.heap[0]

    def sink_down(self, heap, index) -> None:
        L = (index * 2) + 1
        R = (index * 2) + 2
        swap = index

        if L < len(heap) and heap[L] < heap[index]: swap = L
        if R < len(heap) and heap[R] < heap[swap]: swap = R
        
        if swap != index:
            heap[index], heap[swap] = heap[swap], heap[index]
            self.sink_down(heap, swap)

    def swim_up(self, heap, index) -> None:
        if index == 0: return
        parent = (index - 1) // 2
        if heap[parent] > heap[index]:
            heap[parent], heap[index] = heap[index], heap[parent]
            self.swim_up(heap, parent)

# This class implements a graph as an adjacency list where adjacent nodes are stored as linked lists
class Adjacency_List:
    def __init__(self):
        self.adjacent = {}
        
    def add_edge(self,u,v, weight):
        return

    def delete_edge(self,u,v) -> bool:
        return

    #returns the linked list of the given vertex
    def getNeighbors(self,u):
        return

    #returns whether or not two vertices are neighbors
    def isAdjacent(self,u,v) -> bool:
        return

# insertion_sort sorts an array in O(n^2)
def insertion_sort(array) -> list:
    for i in range(len(array) - 1):
        j = i + 1
        if array[j] < array[i]:
            while j > 0 and array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j -1], array[j]
                j -= 1
    return array

# heap_sort sorts an array in O(n log n) using a min heap data structure
def heap_sort(array) -> list:
    heap = Min_Heap(array)
    A = []
    while len(heap.heap) > 0:
        A.append(heap.pop())
    return A

# quicksort sorts an array in O(n log n) in place recursively
def quicksort(array, low, high) -> list:
    if low >= high: return
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[high], array[i + 1] = array[i + 1], array[high] # swap in pivot
    quicksort(array, low, i)
    quicksort(array, i + 2, high)
    return array

# merge_sort sorts an array in O(n log n) recursively
def merge_sort(array) -> list:
    if len(array) <= 1: return array
    mid = len(array) // 2
    L = merge_sort(array[:mid])
    R = merge_sort(array[mid:])

    i = j = 0
    A = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A.append(L[i])
            i += 1
        else: 
            A.append(R[j])
            j+= 1
    A.extend(L[i:])
    A.extend(R[j:])
    return A
    
# binary_search_recursive finds a target value from the low to high indices in a sorted array in O(log n) time.
def binary_search_recursive(array, target, low, high) -> int:
    mid = (high + low) // 2
    if low > high: return
    elif array[mid] == target: return mid
    elif array[mid] > target: 
        return binary_search_recursive(array, target, low, mid - 1)
    else: return binary_search_recursive(array, target, mid + 1, high)
    
# binary_search_iterative finds a target value from the low to high indices in a sorted array in O(log n) time.
def binary_search_iterative(array, target, low, high) -> int:
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target: return mid
        elif array[mid] > target: high = mid - 1
        else: low = mid + 1

if __name__ == '__main__':
    main()