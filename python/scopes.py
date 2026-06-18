'scopes Local-(viswak), global-(ram charan), non local,bulit in, enclosed-pspk(son)'

# # #                                               Global variable

# hero='Mahesh Babu'
# def tollywood():
#     print(" i am from tollywood")
#     print(hero)
# def bollywood():
#     print("i am from bollywood")
#     print(hero)
# def hollywood():
#     print("i am from hollywood")
#     print(hero)
# tollywood()
# bollywood()
# hollywood()

#                                                 Local variable

# def tollywood():
#     hero_t="viswak sen"
#     print("i am from tollywood")
#     print(hero_t)
# def bollywood():
#     hero_b="shahid kapoor"
#     print("i am from bollywood")
#     print(hero_b)
# def hollywood():
#     hero_h="james"
#     print("i am from hollywood")
#     print(hero_h)
# tollywood()
# bollywood()
# hollywood()


def outer():
    ip='hello'
    def inner():
        global ip         # not supported for non local variable
        ip='something'
    inner()
    print(ip)
outer()
print(ip)

# x =10 
# def outer():
#     x = 20
#     def inner():
#         x = 30
#     print(x)
#     inner()
# print(x)
# outer()