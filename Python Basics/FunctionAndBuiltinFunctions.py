# Basic function example
def myFunction(text):
    print(text)
myFunction("Hello World")

# With return statement
def opFunction(num_multiply):
    return num_multiply * 2
print(opFunction(5))

# Function with unknow number of parameters
def kidsFunction(*kids):
    print("The youngest child is " + kids[-1])
kidsFunction("Emil", "Tobias", "Linus")

# Function with keyboard arguments
def namesFunction(name_one,name_two,name_three):
    print("The names are: ",name_one, name_two, name_three)
namesFunction(name_two="Alfredo", name_three="Gerardo",name_one="Miguel")

# Function with arbitrary keyword arguments
def arbitraryArguments(**keys):
    print(keys)
arbitraryArguments(second_key = "Im the second Key", first_key = "Im the first key")

# Function with default value
def defaultValueFunction(name="Temis"):
    print("My name is", name)
defaultValueFunction()
defaultValueFunction("Marcel")

# Function that only expect one argument
def oneArgumentFunction(x,/):
    print(x)
oneArgumentFunction("x")

# Function with only keywords
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
