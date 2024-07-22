from abc import ABCMeta, abstractmethod, abstractstaticmethod  #abstract class
#component interface
class department(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,employee):
        '''implement in child class '''
    @abstractstaticmethod
    def print_department():
        '''implement in child class'''
#leaf class
class accounting(department):
    def __init__(self,employee):
        self.employee=employee
        
    def print_department(self):
        print(f"accounting department {self.employee}")
#leaf class     
class development(department):
    def __init__(self,employee):
        self.employee=employee
        
    def print_department(self):
        print(f"development department {self.employee}")

#composite class
class parentdepartment(department):
    def __init__(self, employee):
        self.employee=employee
        self.base_employee=employee
        self.sub_dept=[]
        
    def add(self,dept):
        self.sub_dept.append(dept)
        self.employee=self.employee+dept.employee
        
    def print_department(self):
        print("parent department")
        print(f"parent department base employees : {self.base_employee}")
        for dept in self.sub_dept:
            dept.print_department()
        print(f"total number {self.employee}")
        
dept1=accounting(100) #leaf obj
dept2=development(200)
parent_dept=parentdepartment(20) #composite class obj
parent_dept.add(dept1)#add leaf obj to composite obj
parent_dept.add(dept2)
parent_dept.print_department()