# Functions and Class to export

# Export class
class TestClassModule:
    def __init__(self,greeting) -> None:
        self.greeting = greeting
    
    def __str__(self) -> str:
        return f"{self.greeting}"

# Export Function
def testFunctionModule(*,greeting):
    print(f"{greeting}")
        