'''
constructor:
-----------
it is a specialized method and used __init__ to initialized the object/attributes , automatically called when object it is created..!! 
'''
# class Car:
#     def __init__ (self,name,price,brand,color,speed):
#         self.name=name
#         self.price=price
#         self.brand=brand
#         self.color=color
#         self.speed=speed
#     def info(self):
#         print("Car Name: ",self.name)
#         print("Car Price: ",self.price)
#         print("Car brand :",self.brand)
#         print("Car color :",self.color)
#     def start(self):
#         if self.speed<=100:
#             print(f"{self.speed+10} Accelerate..!")
#     def stop(self):
#         if self.speed>=10:
#             print(f"{self.speed-10} brake..!")
# c=Car("suzuki",4900000,"tata","white",0)
# c.info()
# c.start()
# c.stop()
# print("="*22)
# c3=Car("tata",145000,"tata","black&white",40)
# c3.info()
# c3.start()
# c3.stop()

'''------------------------Types of constructors-------------------
1)default constructor      ->it has no parameters
2)parameterized constructor ->it is like polymerphism  types(method overloading)
''' 
'Default constructor'
# class Student:
#     def __init__(self):
#         pass
# Student()
# 'or'
# class Student:    # automatically consider as a default constructor method
#     pass
# Student()
# 'or'
# class Student:
#     def __init__(self):
#         self.id=0
#         self.name="Unknown"
#         self.place='not mentioned'
# s=Student()
# # s.id=1
# # s.name='ranga'
# # s.place='ieeja'
# print(s.id)
# print(s.name)
# print(s.place)

'Parameterized Constructor'
# class Number(object):
#     def __init__(self):
#         pass
#     def __init__(self,a):
#         self.a=a
#         print(self.a)
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a+self.b)
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#         print(self.a+self.b+self.c)
#     def __init__(self,a,b,c,d):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
#         print(self.a+self.b+self.c+self.d)
# t=Number(1)
# t=Number(1,2)
# t=Number(1,2,3)
# t=Number(1,2,3,4)
'''to over come this
In method overloading directly python can not access but can access by using 0 and *args
'''
# class Number:
#     def __init__(self,a=0,b=0,c=0,d=0):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
#         print(self.a+self.b+self.c+self.d)
# t=Number()
# t=Number(1)
# t=Number(1,2)
# t=Number(1,2,3)
# t=Number(1,2,3,4)
'or *args->tuple can store & **args-> dictionary format if we give key result as values'
class Number:
    def __init__(self,*num):
        self.num=num
        sum1=0
        for n in num:
            sum1+=n
        print(sum1)
        # print(sum(args))
t=Number()
t=Number(1,2,3,4,5,6,7,8,9,10)
'or another method'
# class Student:
#     def __init__(self,*nums):
#         if len(nums) ==0:
#             print("default constructor")
#         elif len(nums)==1:
#             self.a=nums[0]
#             print(self.a)
#         elif len(nums)==2:
#             self.a=nums[0]
#             self.b=nums[1]
#             print(self.a+self.b)
#         elif len(nums)==3:
#             self.a=nums[0]
#             self.b=nums[1]
#             self.c=nums[2]
#             print(self.a+self.b+self.c)
#         else:
#             print(sum(nums))
# s=Student()
# s=Student(1,2,3)
# s=Student(1,2,3,4,5,6,7,8,9,10)