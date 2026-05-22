'''
1.procedural programming language
disadvantages:
-------------
-no. of lines of code more
-code redundency
-no flexibility
-
2.functional programming language: advantages above points
but apply only for small project 

3. oops:
-----
object oriented programming languages--used for large built-in projects
it is a programming approach using class and objects
class is a blue print of object      ---imaginary planning
object is an instance of class      ---physical we can tough 
'''
# class Student:
#     id=1
#     name="range"
#     age=23
#     place="hyd"
#     def eat(self):
#         print("eating")
#     def studying(self):
#         print("studying")
# s1=Student()
# print(s1.id)
# print(s1.name)
# print(s1.age)
# print(s1.place)
# s1.eat()
# s1.studying()
#-----------------------------------------#
# car class
#how to use multiple properties//values in oops methods are same we can not change 
class Car:
    def car_details(self,name,color,price,mileage):
        self.name=name
        self.color=color
        self.price=price
        self.mileage=mileage
    def info(self):
        print("Car Name: ",self.name)
        print("Car Color: ",self.color)
        print("Car Price: ",self.price)
        print("Car Mileage: ",self.mileage)
    def start(self):
        print("start")
    def stop(self):
        print("stop")
c1=Car()                                               #-->  object creation
c1.car_details("MG","black",15,50)
c1.info()
c1.start()
c1.stop()
print("="*22)
c2=Car()
c2.car_details("benz","blue",100000,60)
c2.info()
c2.start()
c2.stop()
print("="*22)
c3=Car()
c3.car_details("tata","black&white",145000,70)
c3.info()
c3.start()
c3.stop()