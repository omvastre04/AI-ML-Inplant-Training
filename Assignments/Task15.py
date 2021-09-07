# Tue, 7 Sep 2021
# Task 15
# Take a tur of Class, Object, methods of class, properties of class and object
class Student:
    def __init__(self, rno, name, mark) -> None:
        self.rno = rno
        self.name = name
        self.mark = mark
    
    def show_info(self):
        print(f"Student Info \n\tRoll No : {self.rno}\n\tName : {self.name}\n\tMark : {self.mark}")

Tony = Student(1, "Tony Stark", 100)
Tony.show_info()
Tony.grade = "A+"
print("Properties of Object :", Tony.__dict__)