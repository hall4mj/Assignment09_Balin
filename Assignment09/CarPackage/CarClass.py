'''
Name: Alex Haban
email: habanaj@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that we can collaborate on a project using github and know how to use Object Oriented programming.
Citations:
Anything else that's relevant:
'''
#Purpose: Ferrari wants to keep track of their cars model names, engines, top speeds, acceleration, and power from each of their models. 
class Car():
    def setTopSpeed(self, topSpeed):
        self.validateTopSpeed(topSpeed)
    def validateTopSpeed(self, topSpeed):
        if topSpeed < 0:
            print("A car cannot have negative top speed")
        else:
            self.topSpeed = topSpeed
    def __init__(self, name, engine, topSpeed, acceleration, power):
        self.name = name
        self.engine = engine
        self.validateTopSpeed(topSpeed)
        self.validateAcceleration(acceleration)
        self.power = power
    def __repr__ (self):
        return "Engine is a " + self.engine
    def __str__(self):
        return "Car details are: Name: " + self.name + ", Engine: = " + self.engine + ", Top Speed: " + str(self.topSpeed) + ", Acceleration: " + str(self.acceleration) + ", Power: " + self.power
    def setAcceleration(self, acceleration):
        self.validateAcceleration(acceleration)
    def validateAcceleration(self, acceleration):
        if acceleration < 0:
            print("A car cannot have negative acceleration")
        else:
            self.acceleration = acceleration
    def setPower(self, power):
        self.power = power
    def setName(self, name):
        self.name = name
