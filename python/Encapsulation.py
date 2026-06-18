'''
"OCIPEA"-> Object,Class,Inheritance,Polymerphism,Encapsulation,Abstraction
Encapsulation:
-------------
wrapping or binding the data(Attributes) and members(method) in a single unit(Class) 
restricting direct access

Types of access modifiers
-------------------------
public    -> within class/subclass/outer class -> self.public
protected ->same class(within class)/subclass  -> self._protected
private   ->same class(within class)           -> self.__private

'''
# class Bank:
#     def __init__(self,act_name,pin):
#         self.act_name=act_name
#         self._pin=pin    
#     def __str__(self):
#         return f'{self.act_name,self._pin}'    
# b=Bank('ramesh',1947)
# print(b)
# print(b._pin)         # not recommended
# print(b.pin)          # supported
# print(b.__pin)        # not supported

'Getter and Setter-----------------------------'
# class Student():
#     def __init__(self,name,marks):
#         self.name=''
#         self.__marks=0
#     #setters
#     def setter(self,n,m):
#         self.__name=n
#         self.__marks=m
#     # Getter
#     def get_marks(self):
#         return self.__name,self.__marks
# s=Student('ranga',35)
# s.setter('abhi',90)
# print('name'',''marks:' , s.get_marks())
    


'-------------------------Types of Access Modifiers------------------------'

# class Parent(object):
#     def public_method(self):
#         print("This is Public Method")
#     def _protected_method(self):
#         print("This is protected method ")
#     def __private_method(self):
#         print("This is private method ")
#     def access_private_method(self):
#         self.__private_method()
# class Child(Parent):
#     def access_public_method(self):
#         super().public_method()
#     def access_protected_method(self):
#         super()._protected_method()
#     def access_private_method(self):
#         super().access_private_method()
# p=Parent()
# p.public_method()           # recommended
# p._protected_method()       # not recommended
# p._Parent__private_method() # by using _superclass
# print('='*22)
# c=Child()
# c.access_public_method()
# c.access_protected_method()
# c.access_private_method()    #done by the Parent function/method

'---------------------------Types of Attributes and types of methods--------------------'

# class Student (object):
#     clg_name="10k coders"        # class Attribute
#     def __init__(self,id,name):
#         self.id=id               # 
#         self.name=name
#         age=22                   # Local Attribute
#         print(age)
# s=Student(1,'Rangamuni')
# print(s.id)
# print(s.name)
# print(Student.clg_name)
# print(s.clg_name)

'Ex'
# y=20  #Global
# class Student():
#         x=10   # Local 
#         print(x)
# Student()
# print(y)
# print(x)  # x is not defined 

class Hyd(object):
    country_name='India'
    def __init__(self,hyd,blg,viz):
        self.hyd=hyd
        self.blg=blg
        self.viz=viz
    @classmethod
    def change_country_name(cls,new_name):         # class method
        Hyd.country_name=new_name
        
    def change_blg(self,new_blg):                  # instance method
        self.blg=new_blg
        
    @staticmethod                                  # static method
    def greet():
        print("Welcome to..!")
        
        
h=Hyd('charminar','tea','rushikonda beach')
print(h.hyd)
print(h.blg)
print(h.viz)

print(Hyd.country_name)     # class
h.change_country_name('USA')
print(h.country_name)

h.change_blg('Mahesh') # instance
print(h.blg)

h.greet()  #static
Hyd.greet()

print('='*33)
# h1=Hyd('sachvalayam','tea1','rk beach')
# print(h1.hyd)
# print(h1.blg)
# print(h1.viz)
# print(Hyd.country_name)
# h1.change_country_name('UK')
# print(h1.country_name)
# print('='*33)
# h2=Hyd('Golconda fort','tea2','kailasha giri')
# print(h2.hyd)
# print(h2.blg)
# print(h2.viz)
# print(Hyd.country_name)
# h2.change_country_name('Australia')
# print(h2.country_name)



