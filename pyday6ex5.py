class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")

# Creating instances of Person and Employee
person = Person("Alice", 30)
employee = Employee("Bob", 25, "EMP123")

# Calling display_info() for both instances
print("Person Information:")
person.display_info()
print("\nEmployee Information:")
employee.display_info()
