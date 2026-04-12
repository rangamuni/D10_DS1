"""
Basic 

"""
# #area of square
# # slide=5
# # area = slide*slide
# # print(area)
# #area of rectangle
# # nums=list(map(int,input("enter two numbers: ").split()))
# # area=nums[0]*nums[1]

# # print(area)
# #area of triangle
# # base=10
# # height=5
# # area=(1/2)*base*height
# # print(area)
# #perimeter of square
# slide=5
# perimeter=4*slide
# print(perimeter)
# #perimeter of rectangle
# length=10
# breadth=5
# perimeter=2*(length+breadth)
# print(perimeter)
# #perimeter of triangle
# slide1=2
# slide2=3
# slide3=6
# perimeter=slide1+slide2+slide3
# print(perimeter)
#

# 1.even or odd
# n=int(input("Enter a number: "))
# if n%2==0:
#     print('even')
# else:
#     print('odd')

# #2.divisible but 5 but not by 10
# if n%5==0 and n%10!=0:
#     print("satisfy")
# else:
#     print("Not satisfy")
    
#3. biggest among three numbers
# a,b,c=map(int,input("Enter numbers: ").split())
# if a>b and a>c :
#     print(a)
# elif b>c and b>a:
#     print(b)
# else:
#     print(c)
# # smallest among three numbers
# if a<b and a<c :
#     print(a)
# elif b<c and b<a:
#     print(b)
# else:
#     print(c)
    
#4. divisible by 2 ,3 and 6.
# if n%2==0 and n%3==0 and n%6==0:
#     print("satisfy")
# else:
#     print("Not satisfy")

# #5. voting eligibility
# if n<18:
#     print("Not eligible for voting")
# else:
    # print("Eligible for voting")
    
#6. Student pass or fail Based on the marks on all subjects >=35.
# m,p,c=map(int,input(" Enter Marks: ").split())
# if m>=35 and p>=-35 and c>=35:
#     print("pass")
# else:
#     print("fail")
#6. Student pass if passed any one subjects >=35.   

# if m>=35 or p>=-35 or c>=35:
#     print("pass") 
# else:
#     print("fail")

#6. Student pass if passed any two subjects >=35. 
# if m>=35:
#      if p>=35 or c>=35:
#          print("pass")
#      else:
#          print("fail")
# else:
#     if p>=35 and c>=35:
#         print("pass")
#     else:
#         print("fail")

# #7. perfect square number
# sqrt=n**0.5
# if sqrt*sqrt==n:
#     print("perfect square")
# else:
#     print("Not a perfect square")

#8.Cars required for members (Max 5 per car)
# members=int(input("Enter no.of members: "))
# car_required=members//5
# if members%5!=0:
#     car_required+=1
#     print(car_required)
# else:
#     print(car_required)

#9.Second largest among three numbers:

# if a>b and a<c or a>c and a<b:
#     print(a)
# elif b>a and b<c or b>c and b<a:
#     print(b)
# else:
#     print(c)
    
#10.leap year
# if n%4==0 and n%100!=0 or n%400==0:
#     print("leap year")
# else:
#     print("Not a leap year")

'strings , loops and operations'
#1. print natural no. m to n
# n,m=map(int,input("Enter numbers: ").split())
# n=int(input("Enter a number: "))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("Prime")
# else:
#     print("Not Prime")
#---------------------------------------
# m,n=map(int,input("Enter a no: ").split())
#armstrong number
# n=371
# temp=n
# count=0
# t=n
# while t>0:
#     t=t//10
#     count+=1
# sum1=0
# while temp>0:
#     rem=temp%10
#     sum1+=rem**count 
#     temp=temp//10
# if n==sum1:
#     print("A")
# else:
#     print("Not A")

#-----------------------------
#---palindrome
# n=122
# temp=n
# rev=0
# while temp>0:
#     rem=temp%10
#     rev=rev*10+rem
#     temp=temp//10 
# if rev==n:
#     print("P")
# else:
#     print("N P")
#---------------------
#strong number
# for n in range(1,146):
#     t=n
#     sum=0
#     while t>0:
#         rem=t%10
#         t=t//10
#         fact=1
#         i=1
#         while i <=rem:
#             fact=fact*i
#             i+=1
#         sum+=fact
#     if sum==n:
#         print(n)
#--------------------
#input sum of digits and check divisible by input--harshad
# for n in range(50,101):
#     t=n
#     sum=0
#     while t>0:
#         rem=t%10
#         t=t//10
#     sum=sum+rem
#     if n%sum==0:
#         print(n)
#--------------------------
#fibonacci
# # This code snippet is an implementation of the Fibonacci sequence.
# n=int(input("Enter a number: "))
# a=0
# b=1
# for i in range(n):
#     print(a,end=' ')
#     temp=a  
#     a=b
#     b=temp+b
#-----------------------
#wap to enter input 5 display the 5 prime values
# def check_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     else:
#         return True
# n=int(input("Enter number: "))
# c=2
# while n>0:
#     if check_prime(c):
#         print(c,end=" ")
#         n-=1
#     c+=1
    


            

