import copy
#Deepcopy
s1=[['Python','SQL'],'Java']
s2=copy.deepcopy(s1)
s2[0][0]='C++'
print(s1)
print(s2)
print('='*33)
#swallow copy
s1=[['Python','SQL'],'Java']
s2=copy.copy(s1)
s2[0][0]='C++'
print(s1)
print(s2)
