# '''take a string , check length is even or odd,
# if even split into half, then check 2 of having equal vowles'''
# # s="rebels"
# # s_s1=0
# # s_s2=0
# # if len(s)%2==0:
# #     s1=s[:len(s)//2]
# #     s2=s[len(s)//2:]
# #     if s1 in "AEIOUaeiou":
# #         s_s1 +=1
# #     elif s2 in "AEIOUaeiou":
# #         s_s2 +=1
# # if s_s1 == s_s2:
# #     print("both are same")    
    
    
# '''s string '''
# s1="aaabbbccdddaa"
# d={}
# for i in s1:
#     if i in d:
#         d[i] +=1
#     else:
#         d[i]=1
# print(d)
# for k,v in d.items():
#     print(f"{k}{v}",end='')
# print()
'-------------------------------------------problem for test----------------------------------------------'
'Area of rectangle'
# s=5
# a=s*s
# print(a)
'rectangle'
# l=7
# b=9
# a=l*b
# print(a)
'triangle'
# b=8
# h=5
# a=(1/2)*(b*h)
# print(a)
'amount'
# amt_1000=amount//1000
# amount%=1000
# amt_500=amount//500
# amount%=500
# remaining_amount=amount
# print(f'1000s:{amt_1000},500s:{amt_500},remainnig_amount:{remaining_amount}')
'seconds'
# ts=3672
# while ts>3600:
#     h=ts//3600
#     ts%=3600
#     while ts>=60:
#         m=ts//60
#         ts%=60
#         s=ts
# print(f"hours:{h},minutes:{m},seconds:{s}")
'divisible 5 not 10'
# n=50
# if n%5==0 and n%10!=0:
#     print('satisfy')
# else:
#     print("NS")
'2,3,6 /'
# n=18
# if n%6==0 and (n%3==0 and n%2==0):
#     print("statify")
'Perfect square root'
# n=41
# square_root=int(n**0.5)
# print(square_root)
# if n==square_root * square_root:
#     print("perfect square")
# else:
#     print("NP")   
'cars required for members'
# m=91
# cars=m//5
# if m%5==0:
#     print(cars)
# else:
#     cars+=1
#     print(cars)
# print('='*33)
'2 biggest among 3numbers'
# a=12
# b=13
# c=90
# if a>b and a<c:
#     print(a)
# elif b>a and a<c:
#     print(b)
# else:
#     print(c)
'Leap Year'
# l=200
# if l%400==0 or (l%4==0 and l%100!=0):
#     print("Leap Year")
# else:
#     print("NL")

'factorial'
# n=4
# f=1
# for i in range(1,n+1):
#     f*=i
# print(f)
'sum of m-n numbers'
# m=2
# n=4
# s=1
# for i in range(m,n+1):
#     s=s*i
# print(s)
'count a number'
# n=7
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
# print(c)
'prime'
# n=12
# if n<2:
#     print("not a prime")
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
# if c==2:
#     print("p")
# else:
#     print("Np")
'reverse a string'
# s="markramr"
# r=''
# for i in s:
#     r=i+r
# if s==r:
#     print("Palindrome")
# else:
#     print("NP")
'reverse a number'
# n=123
# dig=123
# s=1
# while dig>0:
#     rem=dig%10
#     s=s*rem
#     dig=dig//10
# print(s)   
'anagram'
# s1='stop'
# s2='post'
# # if sorted(s1)==sorted(s2):
# #     print("A")
# # else:
# #     print("NA")
# if len(s1)!=len(s2):
#     print("NA")
# else:
#     for ch in s1:
#         c1=0
#         c2=0
#         for i in s1:
#             if i==ch:
#                 c1+=1
#         for j in s2:
#             if j==ch:
#                 c2+=1
#         if c1!=c2:
#             print("NA")
            
#     else:
#         print('A')
'valid parenthesis'
# s='[{()}]'
# s='()])}'
# open=[]
# is_valid=True
# for ch in s:
#     if ch in '({[' :
#         open.append(ch)
#     else:
#         if len(open)!=0:
#             if (ch==')' and open[-1]=='(') or (ch==']' and open[-1]=='[') or (ch=='}' and open[-1]=='{'):
#                 open.pop()
#             else:
#                 is_valid=False
#                 break
#         else:
#             is_valid=False
# if len(open)==0:
#     print(is_valid)      
# else:
#     is_valid=False 
'check a string is palindrome then result = largest palindrome'
s='badcdabad'
def is_palindrome(sub):
    i=0
    j=len(sub)-1
    while i<j:
        if sub[i]!=sub[j]:
            return False  
        else: 
            i+=1
            j-=1
    return True
max_sub=''
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub=s[i:j]
        if is_palindrome(sub)==True:
            if len(sub)>len(max_sub):
                max_sub=sub
print(max_sub)       
        

    

    
    



        
