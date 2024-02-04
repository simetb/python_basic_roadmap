# Imrpoting the array functionality
import array as arr

# How you would create an array
# arr.array()

# How you would create a list
test_list = []
#or
test_list = list()

# Defining an array in python
test = arr.array('i',[10,20,30])

print(test)

# Length
print(len(test))

# Accessing to a data
print(test[0]) # Expected output 10 

# Search through an array
print(test.index(20)) # Expected output 1 (If there is more than one element, it will returns the first element)

# Append a new value
test.append(40)

print(test)

# Extending the array
test.extend([50,60,70])
print(test)

# Insert a value
test.insert(0,99)
print(test)

# Remove a value (Works same as index)
test.remove(99)
print(test)

# Pop an array index
test.pop(-1) 
print(test)


