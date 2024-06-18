class car:
    def __init__(self,name,wheels,mileage,airbags):
        print("i am the construstor")       
        self.__wheels=wheels
        self.mileage=mileage
        self.airbags=airbags
        self.carname=name


    def __str__(self):
        return (self.carname)

    
    def __del__(self):
        print("i am the destructor")

    def moveforward(self,speed):
        print(self,"is moving forward",speed)
    def movebackward(self,speed):
        print(self,"is moving backward",speed)
    
    #getter 
    def gwheels(self):
        return (self.__wheels)
    #setter
    def swheels(self,wheels):
        self.__wheels=wheels

car1=car("benz",8,6,7)

print(car1.carname)
print(car1.gwheels())
car1.swheels(9)
print(car1.gwheels())
print(car1.mileage)
print(car1.airbags)