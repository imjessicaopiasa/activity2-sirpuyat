class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        """Increase the salary by the given amount."""
        if amount > 0:
            self.salary += amount
            print(f"{self.name}'s salary increased by ${amount}. New salary: ${self.salary}")
        else:
            print("Raise amount must be positive.")

    def display_employee(self):
        """Displays the details of the employee."""
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")
        print("-" * 30)

# Create an Employee object
employee1 = Employee(name="Cris", position="Software Developer", salary=5000)

# Display initial employee details
employee1.display_employee()

# Give the employee a raise
employee1.give_raise(6000)

# Display updated employee details
employee1.display_employee()