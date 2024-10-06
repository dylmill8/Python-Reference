from random import sample, randint

# ! TODO: Hash Map, Bit Mask, Linked List (circular doubly-linked), heap, Sliding Window, Backtracing, Insertion Sort, Quicksort, DFS, BFS, Adjacency Matrix/List Dijkstra's, Bellman Ford, KNP, Kruskal's, Prim's, Topological Sort, Floyd Warshall's, Dynamic Programming, Kth Smallest Element (O(n) using divide and conquer)

# ~ IN PROGRESS: Binary Tree

# * DONE: Node, Stack, Queue, Binary Search, Merge Sort

def main() -> None:

    # BST Testing
    """
    BT = BST()
    BT.insert(node(5))
    BT.insert(node(1))
    BT.insert(node(11))
    BT.insert(node(7))
    BT.insert(node(18))
    BT.insert(node(0))
    BT.traverse(BT.root)
    print(BT.delete(1))
    BT.traverse(BT.root)
    print(BT.delete(11))
    BT.traverse(BT.root)
    print(BT.delete(0))
    BT.traverse(BT.root)
    print(BT.delete(5))
    BT.traverse(BT.root)
    print(BT.delete(7))
    BT.traverse(BT.root)
    print(BT.delete(18))
    BT.traverse(BT.root)
    print(BT.delete(5))
    BT.traverse(BT.root)
            5
        1       11
    0       7       18
    """

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

# This class implements a stack from scratch using a list
class stack():
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

# This class implements a queue from scratch using a list
class queue():
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
class node():
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# This class implements a binary search tree data structure with insertion, deletion, traversal, and re-balancing
class BST():
    def __init__(self, root=None) -> None:
        self.root = root

    # insert() adds a new node to the tree
    def insert(self, node) -> None:
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

    # delete() removes the node with the target value from the tree
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

        if not parent: # deleting root node
            if not i.left or not i.right:
                self.root = i.left if i.left else i.right
            else:
                j = i
                while j.left or j.right:
                    j_parent = j
                    if j.left: j = j.left
                    else: j = j.right
                if j_parent.left == j: j_parent.left = None
                else: j_parent.right = None
                self.root = j
                j.left = i.left
                j.right = i.right

        # deleting a node with less than 2 children
        elif not i.left or not i.right:
            if parent.left == i: parent.left = i.left if i.left else i.right
            else: parent.right = i.right if i.right else i.left

        else: # replace node with predecessor (can be successor)
            j = i
            while j.left or j.right:
                j_parent = j
                if j.left: j = j.left
                else: j = j.right
            if j_parent.left == j: j_parent.left = None
            else: j_parent.right = None
            if parent.left == i: parent.left = j
            else: parent.right = j
            j.left = i.left
            j.right = i.right
        return True
    
    # traverse() prints the tree traversal in pre-order, in-order, or post-order
    def traverse(self, node, pre=False, post=False) -> node:
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
    
    # search() returns a node with the target value or None
    def search(self, val) -> node:
        i = self.root
        while i and i.val != val: # finding target value
            if val == i.val: return i
            elif val < i.val: i = i.left
            else: i = i.right
        return None
    
    # ! TODO: balance() re-balances the binary search tree
    def balance():
        return
        
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