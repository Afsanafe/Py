# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class


class Student:

    class_year = 2025 # class variable, available to all instants
    num_students = 0


    def __init__(self, name, age):
        self.name = name # These are instance variables
        self.age = age # self refers to the object we are currently working with
        Student.num_students += 1 # Rather than referring to the object, we are referring to the class variable, so scope is global

def run():
    student1 = Student("Spongebob", 25)
    student2 = Student("Patrick", 26)
    student3 = Student("Squidward", 32)
    student4 = Student("Mr.Krabs", 48)

    print(student1.name)
    print(student1.age)
    print(student1.class_year)
    
    print(student2.name)
    print(student2.class_year)
    print()
    print(Student.class_year) # We are accessing this variable directly from the class INSTEAD OF an instance, this is explicit
    print()

    print(f"My graduation class of {Student.class_year} has {Student.num_students} students")
    print(student1.name)
    print(student2.name)
    print(student3.name)
    print(student4.name)