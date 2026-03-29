"""tuple same as the list methods but the difference is immutable(can't be changed)
-safe can't be change any data by mistake --(date of birth,pan card no.,etc.)
-fast than list bcz immutable
-static memory allocation-(declared or fixed size) and --dynamic memory allocation-(size can be changed in list)
properties:
----------
-indexing and slicing
-order
-duplicates allowed
-heterogeneous(allow differernt data types)

Methods:
-------
-index()
-count()

"""
# t=("apple", 1, 1, 23, 3.14,  True, (2,), [3,4,5],3+4j, {2,3,4,45}, {"name":"john","age":20,"address":"gadwal"})
# print(type(t))           #which follows order and duplicates and different data types
# print(t[6])         #index
# print(t[3:-1:-1])   #slicing

# #methods:
# #--------
# t[7].append(4)
# print(t.index("apple"))
# print(t.count("apple"))
print("----------------")
""" packing--(storing of values in a tuple) and unpacking of tuple--(storing of values in variables from tuple)"""

t=1,2,3,4,5,6
a,b,*c=t
a,*b,c=t
*a,b,c=t
a,b,*c=t
print(t)
print(a,b,c)
print("----------------")
a=10
b=20
b,a=a,b
print(b,a)







