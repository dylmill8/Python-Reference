import random

# TODO: Hash Map, Bit Mask, Binary Tree, heap, Sliding Window, Backtracing, Insertion Sort, Quicksort, DFS, BFS, Dijkstra's, Bellman Ford, KNP, Kruskal's, Prim's, Topological Sort, Floyd Warshall's, Dynamic Programming, Kth Smallest Element (in O(n) using divide and conquer)

#DONE: Stack, Queue, Binary Search, Merge Sort

def main() -> None:

    array = random.sample(range(0, 15), 10)
    target = random.randint(0, 15)

    print(f"\033[95m{"MERGE SORT ||"}\033[00m", end = " ")
    print(f"Input: {array} | Output:", merge_sort(array))

    print(f"\033[95m{"BINARY SEARCH RECURSIVE ||"}\033[00m", end = " ")
    print(f"Array: {array} | Target: {target} | Found at index:", 
          binary_search_recursive(array, target, 0, len(array) - 1))
    
    print(f"\033[95m{"BINARY SEARCH ITERATIVE ||"}\033[00m", end = " ")
    print(f"Array: {array} | Target: {target} | Found at index:", 
          binary_search_iterative(array, target, 0, len(array) - 1))

# This stack class implements a stack from scratch using a list
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

# This queue class implements a queue from scratch using a list
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
    elif array[mid] > target: return binary_search_recursive(array, target, low, mid - 1)
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