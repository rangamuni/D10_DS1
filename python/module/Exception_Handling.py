'''
Exception Handling:
------------------
Exception- It is a mistake occur during run time 
Types of exception:
------------------
Two Types
1)Build-in  Exception(Generic)
2)custom Exception(Specific)
'''
'ZeroDivisionError Exception'
# try:
#     a=10
#     b=0
#     c=a//b
# except ZeroDivisionError as e:
#     print(e)
'NameError'
# try:
#     print(x)
# except NameError as e:
#     print(e)
'ValueError'
# try:
#     n=int('r')
# except ValueError as e:
#     print(e)
'TypeError'
# try:
#     a='i'+0
# except TypeError as e:
#     print(e)
'KeyError'
# try:
#     a={'one':1}
#     print(a['b'])
#     # print(a.keys())
# except KeyError as e:
#     print(e)
'FileNotFoundError'
# try:
#     a=open('abc.txt')
# except FileNotFoundError as e:
    # print(e)
#1)  a=10
#    b=0
# 2) c=a//b
# 3) n=int('r')
# 4) a='i'+0
# 5) a=open('abc.txt')
# print(x)
'specific or custom Exceptions'
# class MyError(Exception):
#         pass
# try:
#     age=-5
#     if age<0:
#         raise MyError("\033[31mInvalid Age!\033[0m")
# except MyError as e:
#     print(e)
# else:
#     print(age)
#Example2:
# class InsufficientFunds(Exception):
#     pass
# try:
#     balance=1000
#     withdrawal=2000
#     if withdrawal>balance:
#         raise InsufficientFunds("\033[31mInvalid Enter Funds!\033[0m")
# except InsufficientFunds as e:
#     print(e)
'Combinations'
#try+except
#try+else
#try+except+finally
#try+else+finally
#multiple except blocks
# try:
#     a=9+'r'
#     print(a)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)   
# except FileNotFoundError as e:
#     print(e)   
# except KeyError as e:
#     print(e)
# except NameError as e:
#     print(e)
# except Exception as e:
#     print(e)
'nested all'
try:
    try:
        pass
    except :
        pass
    else:
        pass
    finally:
        pass
except:
    try:
        pass
    except:
        pass
    else:
        pass
    finally:
        pass
else:
    try:
        try:
            pass
        except:
            pass
    except:
        pass
    else:
        try:
            pass
        except:
            pass
        else:
            pass
        finally:
            pass
    finally:
        pass
finally:
    try:
        pass
    except:
        pass
    else:
        pass
    finally:
        pass
    ''