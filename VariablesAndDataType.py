# Saving the value
n = 300

# Saving  multiple values
a = b = c = 100
# Or
a,b = 1,2

# Assigment types
# Int assigment
integer = 43

# Float assigment
floating = 14.4

# String assigment
string = "Temis"

# Boolean assigment
bool = True

# None assigment
none_type = None

# Complex assigment
cpx = (2+3j)

# Local assigment
def localAssigment():
    local_variable = "Im a local variable"
    print(local_variable)

# Global assigment
def globalAssigment():
    print(global_variable)

global_variable = "Im a global variable"

# Global assigment inside a function
def globalFunctionAssigment():
    global global_variable_function
    global_variable_function = "Im a global variable function"

# Exec
localAssigment()
globalAssigment()
globalFunctionAssigment()

# Outputs
print(global_variable_function)
    # Type
print(type(a))

# Base Interpreter
# Bynary base
print(0b10)

# Octal base
print(0o10)

# Hexadecimal base
print(0x10)
