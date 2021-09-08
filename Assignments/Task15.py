# Tue, 7 Sep 2021
# Task 15
# Take a tur of Class, Object, methods of class, properties of class and object
class Student:
    college_name = "SVERI's COE (Poly.), Pandharpur" # Static Varible, It is property of class
    def __init__(self, rno, name, mark) -> None:
        self.rno = rno  # instance variable
        self.name = name  # instance variable
        self.mark = mark  # instance variable
        # instance variables are properties of object
    
    def show_info(self):
        print(f"Student Info \n\tRoll No : {self.rno}\n\tName : {self.name}\n\tMark : {self.mark}\n\tCollege Name : {self.college_name}")

Tony = Student(1, "Tony Stark", 100)
Tony.show_info()
Tony.grade = "A+"
print("\nProperties of Object :", Tony.__dict__)
print("\nProperties of Class :", Student.__dict__)
del Tony.grade
print("\nProperties of Object :", Tony.__dict__)
