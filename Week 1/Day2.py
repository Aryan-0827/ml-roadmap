class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def __str__(self):
        return f"{super().__str__()} | ID: {self.student_id} | Grade: {self.grade}"


p = Person("Aryan", 20)
s = Student("Aryan", 20, 101, "A")

print(p)
print(s)