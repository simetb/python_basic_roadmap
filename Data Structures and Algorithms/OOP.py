# Oriented Object Programing Example

class Human:

    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex

    
    def __str__(self) -> str:
        return "{} sex {} is {} years old".format(self.name, self.sex, self.age)
    
class Employee(Human):

    def __init__(self, name, age, sex, salary) -> None:
        self.deparment = None
        self.salary = salary
        super().__init__(name, age, sex)

    def __add__(self, other):
        if isinstance(other, Employee):
            return (self.salary + other.salary)
        else:
            raise("Err0r")
        

    def __len__(self):
        return self.salary

    
    @property
    def Department(self):
        return self.deparment
    
    @Department.setter
    def Department(self,new_value):
        self.deparment = new_value


    @Department.deleter
    def Department(self):
        if self.department is not None:
            print(f"{self.department} was deleted")
            self.department = None
        else:
            raise AttributeError("Department is already None")
        



# Object testing

# Driver Code
if __name__ == "__main__":
    test_human = Employee("Temis", "22", "M",200)
    test_alien = Employee("Temis", "22", "M",300)
    print(test_human)
    print(test_human.deparment)
    test_human.deparment = "Anything"
    print(test_human.deparment)
    del test_human.deparment
    print(test_human+test_alien)
    print(len(test_human))
    