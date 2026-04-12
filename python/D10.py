#---------------------
#square
n=4
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
#--------------------------------------------
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
# #-------------------------
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
for i in range(1,n-1+1):
    
    for j in range(i):print("*",end=" ")
    for j in range(n-i):print(" ",end=" ")
    for j in range(n-i):print(" ",end=" ")
    for j in range(i): print("*",end=" ")
    for j in range(n-i):print(" ",end=" ")
    print()
for i in range(n,0,-1):
    
    for j in range(i): print("*",end=" ")
    for j in range(n-i):print(" ",end=" ")
    for j in range(n-i):print(" ",end=" ")
    for j in range(i): print("*",end=" ")
    for j in range(n-i):print(" ",end=" ")
    print()



