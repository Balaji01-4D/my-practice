class vehicles:
    wheels=6
    power_steering=True
    def moveforward(self):
        print("moving forward")
class benz(vehicles):
    airbags=4

class mercedes(vehicles):
    def movebackward(self):
        print("moving backward")



class mercedes_benz(benz,mercedes):
    speed=100.9
    def moveforward(self):
        return super().moveforward()
    def movebackward(self):
        print("i am the mercedesbenz moving backwards")


car1=mercedes_benz()
print(car1.speed)
car1.moveforward()
car1.movebackward()