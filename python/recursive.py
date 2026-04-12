'''
recursive function : Algorithms-step by step process
function calls itself and return based on the base condition in a function
'''
"Example"
# def num(n): 
#     if n==5: # or increase n value without using print(n)--base condition
#         print(n)
#         return n
#     num(n+1)
#     print(n)
# num(1)

#factorial using recursion
# def fact(n):
#     if n==0:
#         return 1
#     return n * fact(n-1)
    
# print(fact(5))

#---------------------
# 1. Print Numbers (1 to N)
# Example output for n=5 -> 1 2 3 4 5
# n=int(input("Enter: "))
# i=1   
# while i<=n:
#     print(i)
#     i+=1
# def num(n,i):
#     if i==n:
#         return n
#     else:
#         print(i)
#         return num(n,i+1)
# n=5
# i=1
# print(num(n,i))
#-------------------------
# 3. Sum of First N Numbers
# n=5 -> 1+2+3+4+5 = 15
# def sum(n,s=0):
#     if n==0:
#         return s
#     else:
#         s+=n
#         return sum(n-1,s)
# n=5        
# print(sum(n))
#----------------------
# 4. Factorial
# 5! = 120
# def fact(n,f=1):
#     if n==0:
#         return f
#     f*=n
#     return fact(n-1,f)
# n=5
# print(fact(n))    
#------------------------
# 5. Reverse a Number and one condition called palindrome(121)
# 123 -> 321
# def rev(n,r=0):
#     if n==0:
#         return r
#     rem=n%10
#     r=r*10+rem
#     return rev(n//10,r)
# n=3256
# if rev(n)==n:
#     print("palindrome")
# else:
#     print("Not a palindrome")
#---------------------
#6. Count Digits in Number
# # 1234 -> 4
# def count(n,c=0):
#     if n==0:
#         return c
#     else:
#         c+=1
#         return count(n//10,c)
# n=123
# print(count(n))
#---------------------
# 7. Sum of Digits
# # 123 -> 6
# def sum(n,s=0):
#     if n==0:
#         return s
#     else:
#         s+=n%10
#         return sum(n//10,s)
# n=123
# print(sum(n))
#---------------------
# 9. Find Factors
# # 6 -> 4
# def factor(n,i,c=0):
#     if i==n:
#         c+=1
#         return c
#     else:
#         if n%i!=0:
#             return factor(n,i+1,c)
#         else:
#             return factor(n,i+1,c+1)
# n=5
# i=1
# print(factor(n,i))
#---------------------
# 10. Check Prime Number
# # 7 -> Prime Number
# def factor(n,i,c=0):
#     if i==n:
#         c+=1
#         return c
#     else:
#         if n%i!=0:
#             return factor(n,i+1,c)
#         else:
#             return factor(n,i+1,c+1)
# n=6
# i=1
# if factor(n,i)==2:
#     print("prime")
# else:
#     print("Not a Prime")

