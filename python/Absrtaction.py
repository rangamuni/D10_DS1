'''
Abstraction:
-----------
Highlighting the important data and hiding unwanted information

Types of Abstraction:
---------------------
1)Concrete class  -> concrete method  
2)Abstract class  -> at least one abstract method
Two Types of methods:
--------------------
1)Concrete Method -> it has previous inherited method/function with different body and pass
2)Abstract Method -> no body, at least one has no body with decoration method (@abstractmethod)  

'''
from abc import ABC,abstractmethod
#Abstract Class
class Teacher(ABC):  # ABC ->Abstract Base Class
    @abstractmethod
    def teach(self):
        print("Teach")
    def take(self):
        print("Teacher can take attendance")
class PhysicsTeacher(Teacher):
    def teach(self):
        pass
    def take(self):
        pass
class ChemistryTeacher(Teacher):
    def teach(self):
        print("Chemistry Teacher can teach")
    def take(self):
        print("chemistry Teacher can take attendance")
class MathsTeacher(Teacher):
    def teach(self):
        print("Maths Teacher can teach")
    def take(self):
        print("Maths Teacher can take attendance")
# t=Teacher()
# t.take()
# t.teach()
print('='*33)
pt=PhysicsTeacher()
pt.take()
pt.teach()
print('='*33)
ct=ChemistryTeacher()
ct.take()
ct.teach()
print('='*33)
mt=MathsTeacher()
mt.take()
mt.teach()