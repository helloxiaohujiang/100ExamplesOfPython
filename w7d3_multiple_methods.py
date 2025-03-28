# Create a Student Class with Multiple Methods

class Student:
    school = "Rise High"
    
    def __init__(self, fname, lname, id, gender, grade):
        self.__fname = fname
        self.__lname = lname
        self.__id = id
        self.gender = gender
        self.grade = grade

    def get_fullname(self):
        return f"{self.__fname} {self.__lname}"
    
    def get_id(self):
        return self.__id
    
    def set_id(self, new_id):
        if isinstance(new_id, int) and new_id > 0:
            self.__id = new_id
        else:
            print("Invalid ID!")
            
    def get_gender(self):
        return self.gender
    
    def get_grade(self):
        return self.grade
    
    def update_grade(self, newgrade):
        self.grade = newgrade
        
    def display_info(self):
        print(f"ID: {self.__id}, Name: {self.get_fullname()}," 
              f"Gender: {self.gender}, Grade: {self.grade}, School: {self.school}")
    
    @classmethod
    def change_school(cls, newschool):
        cls.school = newschool        
    
    @staticmethod
    def is_passing(grade):
        return grade > 50
        
s1 = Student("Jack", "Smith", 1, "Male", 45)
s2 = Student("Meimei", "Wang", 2, "Female", 80)

s1.display_info()
s2.display_info()

s1.set_id(8)
s1.display_info()

print(s1.get_fullname())
print(s1.get_id())
print(s1.get_gender())
print(s1.get_grade())

s1.update_grade(65)
print(s1.get_grade())
print(Student.is_passing(s1.get_grade()))

print(s1.school)
Student.change_school("ABC")
print(s1.school)