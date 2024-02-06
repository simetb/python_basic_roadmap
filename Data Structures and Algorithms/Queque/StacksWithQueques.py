from queue import LifoQueue

myStack = LifoQueue()

# Put a item into the stack
myStack.put('a') # a
myStack.put('b') # b a
myStack.put('c') # c b a

try:
    while True:
        print(myStack.get_nowait())
except:
    print("Stack vacio")