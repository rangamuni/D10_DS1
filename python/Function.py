'''
Function:
---------
it is a block of code is to be reduced
Types of Function:
-----------------
-Higher order Function
.function has another function as a parameter
.function 
-Rollback Function
-Lambda Function
-Closure Function
'''
'1.'# Function takes another function has a arguments
# def greet(name):
#     print(name,"Hello!!")
# def show(func):
#     func('Ram')
# show(greet)
'2' # Function return another function 
# def outer():
#     def inner():
#         print("I am inner")
#     return inner
# o=outer()
# o()
'RollBack Function'
# def greet(name):
#     print(name,"hello!!")
# def show(func):
#     func("ram")
# show(greet) # same as HOF but function takes another function as a parameter or argument
'Lambda Function' #anonymous Function -represent in a single line
# lambda (parameters or arguments):Expression
#ex:
# age=34
# n=lambda age:'Child' if age<10 else 'Teenager' if age<18 else 'Adult' if age<35 else 'Senior Citizenship'
# print(n(age))
#ex 
# a=0
# n1=lambda a : 5 if 0 else 1
# print(n1(a))
'closure'
# def greet():
#     x=10
#     def show():
#         print(x)
#     show()
# greet()
def outer():
    x=10
    def inner():
        print(x)
    return inner
res=outer()
res()