"""tuple same as the list methods but the difference is immutable(can't be changed)
-safe can't be change any data by mistake --(date of birth,pan card no.,etc.)
-fast than list bcz immutable
-static memory allocation-(declared or fixed size) and --dynamic memory allocation-(size can be changed in list)
properties:
----------
-indexing and slicing
-order
-duplicates allowed
-heterogeneous(allow different data types)

Methods:
-------
-index()
-count()

""" 'Note : true is consider has 1 and 0->False'
t=tuple({1:'one','two':2}.values())
print(t)
t=("apple", 1, 1, 23, 3.14, False, True, (2,), [3,4,5],3+4j, {2,3,4,45}, {"name":"john","age":20,"address":"Gadwal"})
t[8].remove(3)
print(t)
t[10].discard(2)
print(t)
# print(t.count(1))
# print(t.count((3,4,5)))
# print(t.count(0))
# print(t)
# print(type(t))           #which follows order and duplicates and different data types
# print(t[6])         #index
# print(t[3:-1:-1])   #slicing

# #methods:
# # #--------
# print(t.index("apple"))
# print(t.count("apple"))
print("----------------")
""" packing--(storing of values in a tuple) and unpacking of tuple--(storing of values in variables from tuple)"""

# t=1,2,3,4,5,6 #->packing
# # a,b,*c=t      #->unpacking
# # a,*b,c=t
# *a,b,c=t
# # print(t)
# print(a,b,c)
# # print("----------------")
# # a=10
# # b=20
# # b,a=a,b
# # print(b,a)


# import keyword
# print(keyword.kwlist)

# j=10
# # j=01
# j=0x09Af
# j=0o021
# print(j)
# k=3e3  #e or E ==10**n
# print(k)
# True=1
# False=0
# print(int('1'))
# print(int(True))
# h=(2+3j)*(4+2j)*(3+4j)
# print(h.real)
# print(h.imag)
# print(h)

