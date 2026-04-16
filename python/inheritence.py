class Parent:
    def eat(self):
        print("Eating..!!")
    def sleep(self):
        print("Father is sleeping")
class Child(Parent):
    def sleep(self):
        print("Child is sleeping")
    def drive(self):
        print("Driving..!!")
        
c=Child()
c.eat()#// inherited
c.sleep()#// overridden
c.drive()
print("="*22)
f=Parent()
f.eat()#// inherited
f.sleep()#// overridden
f.drive() # its not working bcz father don not above child drive behavior
