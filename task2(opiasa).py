class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")

# Create three student objects
student1 = Student("Dayna", 24, "Agriculutre")
student2 = Student("Delmar", 26, "Civil Engineering")
student3 = Student("April Jane", 22, "Information Technology")

# Call the introduce() method for each student
student1.introduce()
student2.introduce()
student3.introduce()