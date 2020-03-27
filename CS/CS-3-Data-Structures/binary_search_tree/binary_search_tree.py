import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else: # self.value <= value in this case
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else: # self.value <= target in this case
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.left == None and self.right == None:
            self.value = cb(self.value)
            return
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)
        cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left != None: 
            node.in_order_print(node.left)  # take care of the left value
        print(node.value)                   # then print the current value
        if node.right != None:              # Finally, print the right value
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node) # Initialize queue with parent node
        while q.len() > 0: # strategy: place left then right in a queue
            node = q.dequeue() # deque and if that node has a children, recursively add
            print(node.value)   # to the queue. This ensures breadth over depth
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node) # Initialize stack with parent node
        while stack.len() > 0: # strategy: place left then right on stack
            node = stack.pop() # pop the stack and if that has "children", recurse
            print(node.value)  # this ensures we go deeper rather than broader
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left != None:
            self.pre_order_dft(node.left)
        if node.right != None:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left != None:
            self.post_order_dft(node.left)
        if node.right != None:
            self.post_order_dft(node.right)
        print(node.value)

