# Implicit conversion
number_int = 1
number_float = 2.5
implicit_conversion = number_int + number_float # Float implicit conversion
print(type(implicit_conversion))

# Explicit conversion
num_string = '12'
explicit_conversion = int(num_string)

# Exceptions
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! that was no valid number. Try again...")

# Multiple exceptions
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B,C,D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
    
# Exceptions with parameters
try:
    raise Exception('spam','eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args   
    print('x =', x)
    print('y =', y)

# Exception finally clause
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
    
# Exception in function
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Custom Mesage') from exc