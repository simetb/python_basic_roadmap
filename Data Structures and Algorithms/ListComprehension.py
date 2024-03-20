# List Comprehension Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# Get all the elements that has an "a" in the element
new_list = [x for x in fruits if "a" in x]
print(new_list)

# The Syntax
# [expression for item in iterable if condition == true]
# Or
# [expression for item in iterable]

# Get all the elements that are not apple
new_list = [x for x in fruits if "apple" != x]
print(new_list)

# Get all the fruits
new_list = [x for x in fruits]
print(new_list)

# Get an array of numbers with range expresion
new_list = [x for x in range(10)]
print(new_list)

# Accept numbers lower than five
new_list = [x for x in range(10) if x < 5]
print(new_list)

# Return orange instead of banana
new_list = [x if x != "banana" else "orange" for x in fruits]
print(new_list)
