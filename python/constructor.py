'''
constructor:
-----------
it is a specialized method and used __init__ to initialized the object , automatically called when object it is created..!! 
'''
class Car:
    def __init__ (self,name,price,brand,color,speed):
        self.name=name
        self.price=price
        self.brand=brand
        self.color=color
        self.speed=speed
    def info(self):
        print("Car Name: ",self.name)
        print("Car Price: ",self.price)
        print("Car brand :",self.brand)
        print("Car color :",self.color)
    def start(self):
        if self.speed<=100:
            print(f"{self.speed+10} Accelerate..!")
    def stop(self):
        if self.speed>=10:
            print(f"{self.speed-10} brake..!")
c=Car("suzuki",4900000,"tata","white",0)
c.info()
c.start()
c.stop()
print("="*22)
# c3=Car("tata",145000,"tata","black&white",40)
# c3.info()
# c3.start()
# c3.stop()

    
