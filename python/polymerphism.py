"""
poly -> many  morphism -> forms

polymorphism means one method behaves different depends upon different object call  

types:
-----
1.Duck Typing
2.method overriding
3.method overloading
4.operator overloading
"""

# class Robo(object):
#     def walk(self):
#         print("walking..")
#     def talk(self):
#         print("talking..")
# class FighterRobo(Robo):
#     def talk(self):
#         print("FighterRobo can talk")
#     def fight(self):
#         print('FighterRobo can Fight')
# class TeacherRobo(Robo):
#     def talk(self):
#         print("TeacherRobo can talk")
#     def teach(self):
#         print("TeacherRobo can Teach")
# class DriverRobo(Robo):
#     def talk(self):
#         print("DriverRobo can talk")
#     def drive(self):
#         print("DriverRobo can Drive")
'Duck Typing -> it should be "flexible" no redundency '
# def access(r):
#     r.walk()
#     r.talk()
#     if isinstance (r,FighterRobo):
#         r.fight()
#     elif isinstance (r,TeacherRobo):
#         r.teach()
#     elif isinstance(r,DriverRobo):
#         r.drive()

# FighterRobo()  #-> Anonymous object goes to garbage collection
# access(FighterRobo())
# print('='*22)
# access(TeacherRobo())
# print('='*22)
# access(DriverRobo())


'method overriding'

# class A :
#     def a(self):
#         print('I am a')
# class B(A):
#     def b(self):
#         print("I am b")
# B=B()
# B.a()
# B.b()

'method overloading --> it is not support for python but we can make with get using default and keywords arguments(* args)'

# class A(object):
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
#     def add(self,a,b,c,d):
#         print(a+b+c+d)
# a=A()
# a.add(12)
# a.add(1,2)
# a.add(1,2,3)
# a.add(1,2,3,4)

# to over come this 
# class A(object):
#     def add(self,a=0,b=0,c=0,d=0):
#         print(a+b+c+d)
# a=A()
# a.add(12)
# a.add(1,2)
# a.add(1,2,3)
# a.add(1,2,3,4)

# # or
# class A(object):
#     def add(self,*nums):
#         sum1=0
#         for n in nums:
#             sum1=sum1+n
#         print(sum1)
#         # print(sum(nums))
# a=A()
# a.add(12)
# a.add(1,2)
# a.add(1,2,3)
# a.add(1,2,3,4)

'operator overloading'
'specialized/ Dunder -> double underscore / magic '
# a=10
# class add1:
#     def __init__(self,marks):
#         self.marks=marks
#     def __str__(self):
#         return f'{self.marks}' 
# n=add1(12)
# print(a)
# print(n) #'n.__str__(self)'

# a=10
# b=20
# class add1:
#     def __init__(self,marks):
#         self.marks=marks
#     def __add__(self,others):
#         return self.marks + others.marks
# n1=add1(12)
# n2=add1(12)
# print(a+b)
# print(n1+n2) #'n1.__add__(n2) -> manual ga kadhu automatic call avtundi '
a=10
b=20
c=90
class add1:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,others):
        return add1(self.x + others.x,self.y + others.y,self.z + others.z)
    def __str__(self):
        return f'{self.x,self.y,self.z}'
n1=add1(12,11,10)
n2=add1(12,11,10)
n3=add1(12,11,10)
print(a+b+c)
print(n1+n2+n3)

class add1:
    def __init__(self,x):
        self.x=x
        
    def __add__(self,others):
        return self.x + others.x
    def __sub__(self,others):
        return self.x - others.x 
    def __mul__(self,others):
        return self.x * others.x
    def __truediv__(self,others):
        return self.x / others.x
    def __floordiv__(self,others):
        return self.x // others.x 
    def __gt__(self,others):
        return self.x > others.x 
    def __lt__(self,others):
        return self.x < others.x 
    def __eq__(self,others):
        return self.x == others.x
    def __leq__(self,others):
        return self.x <= others.x
    def __ge__(self,others):
        return self.x >= others.x
    def __ne__(self,others):
        return self.x != others.x
n1=add1(12)
n2=add1(10)
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1//n2)
print(n1>n2)
print(n1<n2)
print(n1==n2)
print(n1!=n2)
print(n1 <=n2)
print(n1 >=n2)