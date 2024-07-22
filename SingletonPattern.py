from abc import ABCMeta, abstractmethod  #abstract class
class Iperson(metaclass=ABCMeta):
    @abstractmethod
    def print_data():
        '''Implement in child class'''

class singletonperson(Iperson):
    __instance=None #private, None means instance is not created yet when program start running initially
    @staticmethod
    def get_instance(): #this method is associated with singletonperson class not associated with perticular instance for that we don't use self here
        if singletonperson.__instance==None:
            singletonperson("default",0)
        return singletonperson.__instance
    def __init__(self,name,age):
        if singletonperson.__instance != None:
            raise Exception("singleton cannot be instantiated more than once")
        else:
            self.name=name
            self.age=age
            singletonperson.__instance=self
    @staticmethod
    def print_data():
        print(f"Name: {singletonperson.__instance.name}, Age : {singletonperson.__instance.age}")
        
        
        
p=singletonperson("payal",20)
q=singletonperson.get_instance()
r=singletonperson.get_instance()
print(q)
print(r)
q.x=5
print(r.x)
print(p)
p.print_data()