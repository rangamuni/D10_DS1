''''
define:
-------
set is a  unordered and unique collection of items.it is a mutable data type

properties:
----------
-unordered
-unique
-mutable
-does not support indexing and slicing
-dynamic allocation
-set only allows immutable type of data--hashable for mutable -- unhashable
methods:
-------
-add()      #for list append()
-update()   #for list extend()
-remove()  -through error
-discard()  -does not through error ---ex: any application can run without any error even if the element is not in set 
-pop()       -actually has two ways to work, 1.pop index of element 2.pop last element but set pop random value
-clear()
-copy()

--methods of set operations:
-------------------------
union()
intersection()
difference()
symmetric_difference()

--update methods(modify inside original set):
------------------------------------------
intersection_update()
difference_update()
symmetric_difference_update()

--Boolean return methods:
------------------------
issubset()
issuperset()
isdisjoint()


'''
# s={}#dict---- #s={1}#set
# print(s)
# s=set({'key':'values'}.keys())
# print(s)
# s={1,"string",3.14,False,3+4j,(1,2,3),{0,9,8}}   #indexing and slicing not allowed so do not enter list,dict and set (mutable data types)
# print(s)
# s={1,2,8,3,4,5}
# s.add((10,11))
# s.add(0)
# print(s)
# s.update([1,2,3,4,5,6,7,9])
# print(s)
# s.remove(0)
# #s.remove(11)
# s.discard(11)
# s.discard(9)
# print(s)
# s.pop() # random value deleted
# print(s)
# s.clear()
# print(s)


# s={1,2,3,9,6,5,4}
# print(id(s))
# print(s)
# # s1=s.copy()
# # print(id(s1))
# # print(s1)

# print("-----")

# s=s.copy()
# print(id(s))
# print(s)

# main methods of set
#union 
# s={12,3,4,56,6}
# s1={1,2,3,4,5}
# s2=s.union(s1)
# s2.add((3,4))
# print(s2)
#intersection
# s2=s.intersection(s1)
# # s2=s.difference(s1)
# s2=s.symmetric_difference(s1)
#print(s2)

#methods of update set (modify inside original set)
# s={12,3,4,56,6}
# print(id(s))
# s1={1,2,3,4,5}
# s.intersection_update(s1)
# s.difference_update(s1)
# s.symmetric_difference_update(s1)
# print(s)
# print(id(s))

#methods of boolean return
# s={1,2}
# s1={1,2,3,4,5}
# print(s.issubset(s1))
# print(s1.issuperset(s))
# print(s.isdisjoint(s1))

#---------------------------------------------------------------------------------------------------------------------------------------------#
''' 
Frozenset: symbol : frozenset()
same as set but only difference is immutable
----------
-it is an immutable frozen set
-static allocation
not allow to modify elements inside the frozenset
methods:
-copy()         --all immutable data types address can not change while copying and creating new object but mutable vice-versa
-union()
intersection()
difference()
symmetric_difference()
'''
fs=frozenset([1,2,3,4,5,"string",frozenset((1,2))]) # insert all immutable data types like int,float,bool,complex,tuple,frozenset,string.
# print(id(fs))
# print(fs)

#copy()
# fs1=fs.copy()
# print(id(fs1))
# print(fs1)

#union
fs1=frozenset([6,7,8,9,10])
# fs2=fs.union(fs1)
# fs2=fs.intersection(fs1)
# fs2=fs.difference(fs1)
fs2=fs.symmetric_difference(fs1)
print(fs2)


#and remaining methods are not works(can not modify)









