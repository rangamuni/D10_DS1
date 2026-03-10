'''
lambda is a single line anonymous function. it can take any no. of args .
but can only one expression. evaluate and returned 
'''
"single line with static method."

# x=lambda : print('ranga')
# x()


"# # dynamic method"

# x1=lambda a:a+10
# print(x1(4))

# x2=lambda a,b,c=10:a+b+c
# print(x2(3,3))

# y=lambda *pr:print(pr)
# # print(y(3,2,3))

# def sample(x):
    
#     print('i am sample function')
#     print(x())
# def sample2():
#     print('i am sample2')
# def sample1():
#     print('i am sample1')
# def demo():
#     print('i am demo')
# sample(demo)
# # sample(sample1)
# # sample(sample2)
# def demo(x,y,z):
#     print('this is demo function')
#     x()
#     return 'bye'
# print(demo(lambda:print('i am s1')))

'multiple function in a single line lambda expressions'

# def demo(x,y,z):
#     sum=x()+y()+z()
#     print(sum)
#     return 'Hello'
# print(demo(lambda:5, lambda:1, lambda:4))

'lambda used in list,dict,tuple etc..'

x=['ranga',12,45,lambda :print('this is ram')]
print(x[3]())

x1={'name':'ranga','age':22,'work':lambda : print("ntg is working")}
x1['work']()

x1={'name':'ranga','age':22,'work':lambda bh: print(f"{bh} is working")}
x1['work']('ntg')







