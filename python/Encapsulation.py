'''
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


'Types of Access Modifiers'
class Parent(object):
    def public_method(self):
        print("This is Public Method")
    def _protected_method(self):
        print("This is protected method ")
    def __private_method(self):
        print("This is private method ")
    def access_private_method(self):
        self.__private_method()
class Child(Parent):
    def access_public_method(self):
        super().public_method()
    def access_protected_method(self):
        super()._protected_method()
    def access_private_method(self):
        super().access_private_method()
p=Parent()
p.public_method()           # recommended
p._protected_method()       # not recommended
p._Parent__private_method() # by using _superclass
print('='*22)
c=Child()
c.access_public_method()
c.access_protected_method()
c.access_private_method()    #done by the 

