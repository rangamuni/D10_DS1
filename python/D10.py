#----------------------------------------------
#square
# n=4
# m=10
# for i in range(1,n+1):
#     for j in range(1,n+1):print("*",end=" ")
#     print()
#-----------------------------------------------
# rectangle
# for i in range(1,n+1):
#     for j in range(1,n+1):print("*",end=" ")
#     for k in range(1,m+1):print("*",end=" ")
#     print()
#----------------------------------------------
#right angled triangle
# for i in range(1,n+1):
#     for j in range(i):print("*",end=" ")
#     for k in range(n-i):print(" ",end=" ")
#     print()
# print("-------------------------")
# #right angled triangle23
# for i in range(1,n+1):
#     for k in range(n-i):print(" ",end=" ")
#     for j in range(i):print("*",end=" ")
#     print()
# print("--------------------------")
# #inverted right triangle
# for i in range(n,0,-1):
#     for k in range(n-i):print(" ",end=" ")
#     for j in range(i):print("*",end=" ")
# 4   print()
# print("--------------------------------")
# #inverted left triangle
# for i in range(n,0,-1):
#     for j in range(i):print("*",end=" ")
#     for k in range(n-i):print(" ",end=' ')
#     print()
# print("---------------------")
#diamond and rhombus with help of pyramid
# for i in range(1,n+1-1):
#     for j in range(n-i):print(" ",end=" ")
#     for j in range(i): print("*",end=" ")
#     for j in range(i-1): print("*",end=" ")
#     for j in range(n-i):print(" ",end=" ")
#     print()
# for i in range(n,0,-1):
#     for j in range(n-i):print(" ",end=" ")
#     for j in range(i): print("*",end=" ")
#     for j in range(i-1): print("*",end=" ")
#     for j in range(n-i):print(" ",end=" ")
#     print()
#print("---------------")
#LEFT - aligned half diamond
# for i in range(1,n+1):
#     for i in range(i):print("*",end=" ")
#     for j in range(n-i):print(" ",end=' ')
#     print()
# for i in range(n-1,0,-1):
#     for i in range(i):print("*",end=" ")
#     for j in range(n-i):print(" ",end=' ')
#     print()
# #print("----------")
# #left-aligned half diamond
# for i in range(1,n+1):
#     for j in range(n-i):print(" ",end=' ')
#     for i in range(i):print("*",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i):print(" ",end=' ')
#     for i in range(i):print("*",end=" ")
#     print()

# print("----------------------------")
#Sandglass Pattern
# for i in range(n,1,-1):
#     for j in range(n-i):print(" ",end=' ')
#     for i in range(i):print("*",end=" ")
#     print()
# for i in range(1,n+1):
#     for j in range(n-i):print(" ",end=' ')
#     for i in range(i):print("*",end=" ")
#     print()
#--------------------------------------
#butterfly=
# for i in range(1,n-1+1):
    
#     for j in range(i):print("*",end=" ")
#     for j in range(n-i):print(" ",end=" ")
#     for j in range(n-i):print(" ",end=" ")
#     for j in range(i): print("*",end=" ")
#     for j in range(n-i):print(" ",end=" ")
#     print()
# for i in range(n,0,-1):
    
#     for j in range(i): print("*",end=" ")
#     for j in range(n-i):print(" ",end=" ")
#     for j in range(n-i):print(" ",end=" ")
#     for j in range(i): print("*",end=" ")
#     for j in range(n-i):print(" ",end=" ")
#     print()

# chocolates and  find no.of wrapper covers
# amount=21
# wrappers=amount
# r=amount
# while wrappers>=3:
#     extra=wrappers//3
#     r+=extra
#     wrappers=extra+wrappers%3
# print(r)


# l=list(map(int,input("Enter a number:").split()))
# l=[1,2,3]  #[1,2,4]
# s,s1='',[]
# for i in l:
#     s+=str(i)
# m=int(s)+1
# for j in str(m):
#     m=str(j)
#     s1.append(int(m))
# print(s1)
# l1=[]
# s1=0
# for i in l:
#     s1=10*s1+i
# s1+=1
# while s1>0:
#     r=s1%10
#     s1=s1//10
#     l1+=[r]
# print(l1[::-1])
'p=5  2 3 5 7 11'
# n=int(input("Enter a number: "))
# def is_prime(n):
#     if n<2:
#         return False
#     count=0
#     for j in range(1,n+1):
#         if n%j==0:               
#             count+=1
#     if count==2:
#         return True
# x=1
# while n>0:
#     if is_prime(x)==True:
#         print(x)
#         n-=1
#     x+=1





