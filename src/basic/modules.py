import fun

if fun.is_male:
    print("hello world")
else:
    print("else")

# Objects and classes


class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


class SpecialStudent(Student):
    def __init__(self, name, major, gpa):
        super().__init__(name, major, gpa)


student = Student("Edgar", "Aeros", 4)
student2 = SpecialStudent("Edgar", "Aeros", 3)

print(student.name)
print(student.on_honor_roll())
print(student2.on_honor_roll())
