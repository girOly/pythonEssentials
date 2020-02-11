# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

# def average(sequence):
#     return sum(sequence)/ len(sequence)

# print(average(student["grades"]))

# # print(student.average())

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades= grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Joe", (80,75,60,98))       
print(student.name)
print(student.average_grade())