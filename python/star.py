for j in range(1,4):
    for i in range(3):
        print(i+j,end=' ')
    print()
print('________')
    
#a=65 to ---
    
# """patterns first 3 rows and 
# each row 3 stars"""

for i in range(1,4):
    stars=''
    for j in range(1,4):
        stars+='* '
    print(stars)
print("-----")
    
# # rectangle rows 3 and each row has 6 stars
    
for i in range(1,4):
    stars=''
    for j in range(1,7):
        stars+='* '
    print(stars)
print("-------")
# right triangle 3 row and each row has stars
n=3
for i in range(1,n+1):
    stars=''
    for j in range(1,1+i):
        stars+='* '
    print(stars)    
print("-------")
#pyramid and rhombus pattern 4 rows and each row has spaces and stars 
n=4
for i in range(1,n+1):
    spaces=''
    for j in range(1,n+1-i):
        spaces+=' '
    stars=''
    for k in range(1,n-n+i+1):
        stars+='* '
    print(spaces+stars)
for i in range(n-1,0,-1):
    spaces=''
    for j in range(1,n+1-i):
        spaces+=' '
    stars=''
    for k in range(1,n-n+i+1):
        stars+='* '
    print(spaces+stars)
    
print("-------")    
#numbers,ascii values A-65 and a-97 NOTE-use chr(i+j)

for i in range(65,68):
    for j in range(3):
        print(chr(i+j),end=' ')
    print()     
    
print("-------")
for i in range(97,100):
    for j in range(3):
        print(chr(i+j),end=' ')
    print()  
print("-------")     
#same values
for i in range(97,100):
    for j in range(3):
        print(chr(i),end=' ')
    print()  
