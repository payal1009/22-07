from abc import ABCMeta, abstractmethod  #abstract class
class Iperson(metaclass=ABCMeta):
    @abstractmethod
    def person_method():
        '''Interface method'''
class student(Iperson):
    def __init__(self):
        self.name="student name"
    def person_method(self):
        print("I am a student")
class Teacher(Iperson):
    def __init__(self):
        self.name="Teacher name"
    def person_method(self):
        print("I am a Teacher")

class personFactoryPattern:
    def build_person(person_type):
        print(person_type)
        if person_type=="student":
            return student()
        if person_type=="Teacher":
            return Teacher()
        print("Invalid")
        return None
    
    
if __name__=='__main__':
    choice=input("what type of person student/teacher ? ")
    person=personFactoryPattern.build_person(choice)
    if person:
        person.person_method()
    else:
        print("Invalid")