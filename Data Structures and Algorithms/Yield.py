
# Yield Generetor expression example 
def squares(length):
    for n in range(length):
        yield n**2
        
for square in squares(5):
    print(square)
    
    
# Or you can use a sintax similar to list comprehension
squares_two = (n** 2 for n in range(5))
for square in squares_two:
    print(square)