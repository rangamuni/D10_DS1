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
'practice -------------------'
# s='a[4]b[3]c[2]d[1]' #aaaabbbccd
# ch=''
# dig=''
# res=''
# for i in s:
#     if i.isalpha():
#         ch=i
#     elif i.isdigit():
#         dig=int(i)
#     elif i==']':
#         res=ch * dig
#         print(res,end='')      
# print() 
# s1='ab[2]bc[1]c[2]' #ababbcc
# ch=''
# dig=''
# res=''
# for i in s1:
#     if i.isalpha():
#         ch=ch + i
#     elif i.isdigit():
#         dig=int(i)
#     elif i==']':
#         res=ch * dig
#         ch=''
#         dig=''
#         print(res,end='')
# print()
# s3='a[10]b[1]' #aaaaaaaaaab
# s1='ab[2]bc[1]c[2]'
# s='a[0]b[3]c[2]d[1]' #aaaabbbccd
# ch=''
# dig=0
# res=''
# for i in s:
#     if i.isalpha():
#         ch=ch+i
#     elif i.isdigit():
#         dig=dig * 10 +int(i)
#     elif i==']':
#         res=ch * dig
#         ch=''
#         dig=0
#         print(res,end='')
# s='fourthreetwoone' #4321
# d={'zero':0,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
# res=''
# ch=''
# for i in s :
#     ch=ch+i
#     if ch in d:
#         res+=str(d[ch])
#         ch=''
# print(res)
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):print("   ",end='')
#     for j in range(i-1): print(" * ",end='')
#     for j in range(i): print(" * ",end='')
#     for j in range(n-i):print("   ",end='')
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i):print("   ",end='')
#     for j in range(i-1): print(" * ",end='')
#     for j in range(i): print(" * ",end='')
#     for j in range(n-i):print("   ",end='')
#     print()
'Basic problems'
'1'
# lst=[3,7,17,2,14]
# res=[]
# r=[]
# for i in lst:
#     if i%2==0:
#         res.append(i)
#     else:
#         r.append(i)
# print(res)
# print(r)
'2'
# lst=[3,14,16,6,10] #[17,7,11]
# res=[]
# for i in lst:
#     res.append(i+1)
# # factor checking
# r=[]
# for j in res:
#     c=0
#     for i in range(2,j+1):
#         if j%i==0:
#             c+=1
#     if c==1:
#         r.append(j)
# print(r)
'3'
# lst=[5,9,8,16,10] #res=[5,9,16]
# r=[]
# for i in lst:
#     # checking factors for lst
#     f=0
#     for j in range(1,i+1):
#         if i%j==0 :
#             f+=1  #2,3,4,5,4
#     # checking prime for f 
#     c=0
#     for k in range(1,f):
#         if f%k==0:
#             c+=1
#     if c==1 and f>1:
#         r.append(i)
# print(r)   

# 'prime'
# a=10
# n=lambda a : 'P' if all(a%i!=0 for i in range(2,a)) else 'NP'  
# print(n(a))
'Max number in a list''-------------------------------------------------------------------------------------'
# lst=[12,89,22,34,56,6,56,89]  #[56]
# # lst.sort()
# # print(lst)
# high=second_high=third=four=0
# for i in lst:
#     if i>high:
#         high=i
#     elif i>high:
#         four=third
#         third=second_high
#         second_high=high
#         high=i
#     elif i>second_high and i!=high:
#         four=third
#         third=second_high
#         second_high=i
#     elif i>third and i!=second_high and i!=high:
#         four=third
#         third=i
#     elif i>four and i!=third and i!=second_high and i!=high:
#         four=i
# print(high)
# print(second_high)
# print(third)
# print(four)


# max=[]
# for i in lst:
#     for j in lst:
#         if i<j:
#             i=j
# max.append(i)
# print(max)
''
# res=[]
# for i in lst:
#     for j in lst:
#         if j>i:
#             i=j
# res=res+[i]
# print(res)
''
# n=int(input("Enter a number"))
# if n%2==0:
#     print("E")
# else:
#     print("O")
'largest of three numbers'
# a,b,c=map(int,input("Enter a numbers:").split())
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)

'2'
# lst=[12,89,22,34,56,6,56,89]  #[56]
# f=s=t=0
# for i in lst:
#     if i>f:
#         t=s
#         s=f
#         f=i
#     elif i>s and i!=f:
#         t=s
#         s=i
#     elif i>t and i!=s and i!=f:
#         t=i
# print(s)
# print(t)
'13-05-26'
# lst=[123,456,243,768,129] #res =[123,456,129]
# res=[]
# for i in lst:
#     for j in str(i):
#         print(j,end=' ')
'7'

def s1(nums):
    f=s=0
    for i in nums:
        if i>f:
            s=f
            f=i
        elif i>s and i!=f:
            s=i
    return s
nums=[2,1,3,4,8,6,4]
print(s1(nums))
