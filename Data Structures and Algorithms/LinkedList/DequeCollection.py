from collections import deque

# Creating a linkedList
llist = deque(["a","b","c"])

# Append an element into TAIL
llist.append("TAIL")
print(llist)

# Deleting an TAIL element 
llist.pop()
print(llist)

# Append an element into HEAD
llist.appendleft("HEAD")
print(llist)

# Deleting an HEAD element 
llist.popleft()
print(llist)

