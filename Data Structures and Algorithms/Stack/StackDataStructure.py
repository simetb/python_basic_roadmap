# Stack data structure follow the LIFO rule
# LIFO (Last in, First out)

# You can represent a LIFO DATA STRUCTURE with an array o a deque colleciton

# But we will represent it  with a class

class StackNode:
    
    def __init__(self,data):
        self.value = data
        self.next = None

class Stack:
    
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = StackNode("head")
        self.size = 0
        
    
    # String representation of stack
    def __str__(self) -> str:
        current = self.head.next
        out = ""
        while current:
            out += str(current.value) + "->"
            current = current.next
        return out[:-2]
    
    # Get the current size of the stack
    def getSize(self):
        return self.size
 
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
    
    # Get the top item of the stack
    def peek(self):
        
        # Sanitary check to see if wee are peeking an empty stakc
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        
        return self.head.next.value
    
    # Push a value into the stack.
    def push(self, value):
        node = StackNode(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        
    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

# Driver Code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
 
    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
    