import heapq

# We create an unordered list
unordered_list = [3, 1, 5, 7, 4, 9, 2, 6, 8]

# Convert the list into a heap
heapq.heapify(unordered_list)
print("Heap created from the unordered list:", unordered_list)

# Add an element to the heap
heapq.heappush(unordered_list, 0)
print("Heap after adding element 0:", unordered_list)

# Remove and return the smallest element from the heap
min_element = heapq.heappop(unordered_list)
print("Minimum element removed from the heap:", min_element)
print("Heap after removing the minimum element:", unordered_list)

# Get the smallest element from the heap without removing it
min_element = unordered_list[0]
print("Current minimum element of the heap:", min_element)

# Convert a list into a heap and initialize the heap with elements
initial_list = [5, 3, 1, 4, 2]
initialized_heap = heapq.heapify(initial_list)
print("Heap created from the initialized list:", initial_list)

# Get a sorted list using the heap sort function
sorted_list = []
while initial_list:
    min_element = heapq.heappop(initial_list)
    sorted_list.append(min_element)
print("Sorted list using heap sort:", sorted_list)
