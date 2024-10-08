from random import sample, randint
from math import log, floor

# ! TODO: Hash Map, Bit Mask, Circular Doubly-linked List, heap, Sliding Window, Backtracing, DFS, BFS, Adjacency Matrix/List, Dijkstra's, Bellman-Ford, KNP, Kruskal's, Prim's, Topological Sort, Floyd Warshall's, Dynamic Programming, Kth Smallest Element (O(n) using divide and conquer), Huffman Coding Tree

# ~ IN PROGRESS: Insertion Sort, Quicksort

# * DONE: Node, Stack, Queue, Linked List, Binary Search, Merge Sort, Binary Search Tree

def main() -> None:

    array = sample(range(0, 15), 10)
    target = randint(0, 15)

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

# This class implements a graph node object with a value, left pointer, and right pointer
class Node():
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# This class implements a linked list of nodes using their right pointer with size checking, insertion, deletion, reversal, and printing
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
        
# merge_sort takes an array and returns it in sorted order in O(n log n)
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
    
# binary_search_recursive takes in a sorted array, target value, low search index, and high search index which it will use to recursively find the target value in the array in O(log n) time.
def binary_search_recursive(array, target, low, high) -> int:
    mid = (high + low) // 2
    if low > high: return
    elif array[mid] == target: return mid
    elif array[mid] > target: 
        return binary_search_recursive(array, target, low, mid - 1)
    else: return binary_search_recursive(array, target, mid + 1, high)
    
# binary_search_iterative takes in a sorted array, target value, low search index, and high search index which it will use to iteratively find the target value in the array in O(log n) time.
def binary_search_iterative(array, target, low, high) -> int:
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target: return mid
        elif array[mid] > target: high = mid - 1
        else: low = mid + 1

if __name__ == '__main__':
    main()