'''
comprehensions- it is a short and clean way to create a list/tuple.. etc
list comprehensions: it is a short and clean readable way to create a list in python
syntax:
-------
list=[expressions for i in sequence()]
expression+loop+optional condition 

advantages:
-----------
-easy and simple and clean way to understand
-fast accessing and execution
-interview and projects mainly used onces
-perfect filtering and formations/modifications 
'''
#----------------------------------------------------------
# # ternary operations in python:
# age = 17
# res= 'child' if age<12  else 'teenager' if age <=17  else 'adult' if age<28 else 'senior citizen' 
# print(res)
#--------------------------------------------------------------------
#problem solving in list comprehension
#####--right -> filtering(required values taken from given lst) 
#    --left ->modify based on the condition --#######
#-----------------------------------------
# 1.square of no. as a output lst=[1,2,3,4,5]
# lst=[1,2,3,4,5]
# lst1= [i**2 for i in range(1,len(lst))]/[i*i for i in lst]
# print(lst1)

# 2. even and odd
# lst=[i for i in range(1,11) if i%2!=0]
# print(lst)

# 3.from square root display only even and odd no. squares
# lst=[ i**2 for i in range(1,11) if i%2==0]
# print(lst)

# 4.Even or Odd labelling 
# lst=[f'{i} : Even' if i%2==0 else f'{i} : Odd' for i in range(1,11)]
# print(lst)

# 5.Uppercase characters
# char='Python'
# lst=[ch.upper() for ch in char]
# print(lst)


# 6. Extract vowels and consonants
# word="mississippI"
# lst=[i for i in word if i not in "aeiouAEIOU"]
# print(lst)

# 7. Flatten Matrixes
# matrix=[[[5,6],[3,4],[1,2]]]
# lst=[k for i in matrix for j in i for k in j]
# print(lst)

# #8. length of words
# words=["python","is","awesome"]
# lst=[len(i) for i in words ]
# print(lst)

'comprehension on tuple'

# 1.square of no. as a output lst=[1,2,3,4,5]
lst=tuple((1,2,3,4,5))
lst1= tuple([i**2 for i in range(1,len(lst))])                                 #/[i*i for i in lst]
print(lst1)

# # 2. even and odd
lst=tuple([i for i in range(1,11) if i%2!=0])
print(lst)

# # 3.from square root display only even and odd no. squares
lst=tuple([ i**2 for i in range(1,11) if i%2==0])
print(lst)

# # 4.Even or Odd labelling 
lst=tuple([f'{i} : Even' if i%2==0 else f'{i} : Odd' for i in range(1,11)])
print(lst)

# # 5.Uppercase characters
char='Python'
lst=tuple([ch.upper() for ch in char])
print(lst)


# # 6. Extract vowels and consonants
word="mississippI"
lst=tuple([i for i in word if i not in "aeiouAEIOU"])
print(lst)

# # 7. Flatten Matrixes
matrix=tuple((((5,6),(3,4),(1,2))))
lst=tuple((j for i in matrix for j in i for k in j))
print(lst)

# #8. length of words
words=["python","is","awesome"]
lst=tuple([len(i) for i in words ])
print(lst)


' comprehensions in set '

# 1.square of no. as a output lst=[1,2,3,4,5]
lst=tuple((1,2,3,4,5))
lst1= tuple([i**2 for i in range(1,len(lst))])                                 #/[i*i for i in lst]
print(lst1)

# # 2. even and odd
lst=tuple([i for i in range(1,11) if i%2!=0])
print(lst)

# # 3.from square root display only even and odd no. squares
lst=tuple([ i**2 for i in range(1,11) if i%2==0])
print(lst)

# # 4.Even or Odd labelling 
lst=tuple([f'{i} : Even' if i%2==0 else f'{i} : Odd' for i in range(1,11)])
print(lst)

# # 5.Uppercase characters
char='Python'
lst=tuple([ch.upper() for ch in char])
print(lst)


# # 6. Extract vowels and consonants
word="mississippI"
lst=tuple([i for i in word if i not in "aeiouAEIOU"])
print(lst)

# # 7. Flatten Matrixes
matrix={((5,6),(3,4),(1,2))}
lst={j for i in matrix for j in i for k in j}
print(lst)

# #8. length of words
words={"python","is","awesome"}
lst={len(i) for i in words }
print(lst)

