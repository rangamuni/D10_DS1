# class Parent:
#     def eat(self):
#         print("Eating..!!")
#     def sleep(self):
#         print("Father is sleeping")
# class Child(Parent):
#     def sleep(self):
#         print("Child is sleeping")
#     def drive(self):
#         print("Driving..!!")
        
# c=Child()
# c.eat()#// inherited
# c.sleep()#// overridden
# c.drive()
# print("="*22)
# f=Parent()
# f.eat()#// inherited method
# f.sleep()#// overridden method
# f.drive() # its not working bcz father don not above child drive behavior  --specialized/specific method

# inheritence hierarchical level 
# class Mother:
#     def voice(self):
#         print("talking..")
# class Son(Mother):
#     def fight(self):
#         print("fight for family..")
# class Dau(Mother):
#     def Learn(self):
#         print("Learning..")
# s= Son()
# s.fight()
# s.voice()
# d= Dau()
# d.Learn()
# d.voice()

# multiple inheritence 
class F1:
    def Learn(self):
        print("F1 is learning..")
class F2:
    # def Learn(self):
    #     print("F2 is learning..")
    pass
class Child(F2,F1):
    # def Learn(self):
        # print("Child is Learning..")
        pass
d= Child()
d.Learn()
# MRO -> method resolution order - C3 Linearization  Algorithms

