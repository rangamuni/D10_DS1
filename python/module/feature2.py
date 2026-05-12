from feature1 import *
x=20
def f2():
    print("I am f2")
f1()

# print(4<<2)
# print(bin(6))
# print(oct(9))
# print(hex(90))
# print(4>>2)
# 4^5   ^->xor  &-> and | -> or, ~ ->not,  ls-> <<, rs -> >>
# print(4^5) 000100
#            000101
#            000001-> 1(res)
'terinary operations'
# time=-1
# x="gudevg" if time<4 else "gudmrng" "mom "if time >0 else 'dad'
# print(x)
# n=890
# x='+ve' if n>0 else '-ve'
# print(x)
n=int(input("Enter a number: "))
x='even' if n&1==0 else 'odd'
print(x)
if n& 1==0:print("even")
else:print("odd")
