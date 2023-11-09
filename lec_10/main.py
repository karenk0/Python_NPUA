import vehicle # Or if instead we have written     from vehicle import *        this will import everything from that modul

class Car(vehicle.Vehicle): # and here we could write just Vehicle, instead of vehicle.Vehicle
    def __init__(self, weight, speed):
        super().__init__(weight)
        self.speed = speed   
    def move(self):
        print("A car moves.")

class Plane(vehicle.Vehicle):
    def __init__(self, weight, speed, engineCount):
        super().__init__(weight)
        self.speed = speed
        self.engineCount = engineCount
    def move(self):
        print("A plane moves.")

class Boat(vehicle.Vehicle):
    def __init__(self, weight, speed, maxLoad):
        super().__init__(weight)
        self.speed = speed
        self.maxLoad = maxLoad
    def move(self):
        print("A boat moves.")

class RaceCar(Car):
    def __init__(self, weight, speed, horsePower):
        super().__init__(weight, speed)
        self.horsePower = horsePower
    def move(self):
        print("A race car moves.")
    def __str__(self):
        return f"A racecar with weght - {self.weight}, speed - {self.speed}, horsepower - {self.horsePower} runs!"

myRaceCar = RaceCar(250, 350, 600)
print(myRaceCar)