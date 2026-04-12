'''
DICTIONARY-- word came with the help of dictionary having word:meaning(fast accessing,meaning,mapping)
DEFINE:
-------
it is a data structure that stores data in key and value pairs.
PROPERTIES:
----------
-ordered
-mutable
-dynamic
-no indexing and slicing only using key -unhashable for mutable onces
-heterogenenous data can store for keys(immutable-can not change--uniqu) for values(all kind of data can store)

METHODS:
-------
-update() changes one or more at a time by using keys and also values
-keys()
-values()
-items()
-get()  does not give error while provide unknown key and give none or we can provide any msg
-pop() particular we can delete from dict
-popitem() delete last item
-clear() remove all keys and values
-setdefault()-- use for can not clear important data if it exits
-fromkeys() --dict.fromkeys()
-copy() 

'''
#values - accept all kind of data types 
#keys-only immutable data types like primitive +tuple+frozenset
# dict={1:'one','string':'ranga',3.14:10.8,True:False,3+4j:4+5j,None:None,(1,2,3):[1,2,3],frozenset([1,2,3]):frozenset([1,2]),2:[1,1],3:{2,2},4:(3,3),5:{1:'one'}}
#----------representation---
# d={}
# dict=dict([(1,2)])
#-------------------------------
# dict[13]=2
# print(dict)
# dict[2]=(33,33)
# print(dict)
#---------------
#METHODS:
#--------
# d={1:"one",2:"two",3:'three'}

#keys(),v,i
# print(d.keys())
# print(d.values())
# print(d.items())

#update()
# d.update({4:"two"})
# d.update({1:"two"})
# print(d)

#setdefault
# print(d.setdefault(1,'five'))
# print(d)

#get()
# dict[13]=2 ---throws error
# print(d.get(4))--it gives None if we can not enter anything
# print(d.get(4,"no value exits!!"))

#pop() and popitem()
# print(d.pop(2))
# print(d.popitem())

#clear()
# print(d.clear())

#copy()
# print(d)
# print(id(d))
# print(d.copy())
# print(id(d))

#fromkeys()
lst=1,             #must be iterable int not iterable if lst=1 -it's not works
print(dict.fromkeys(lst,0))








