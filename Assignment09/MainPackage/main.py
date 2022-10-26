'''
Name: Group Balin: Matthew Hall, Joshua Earley, Sarah Zimmer, Alex Haban
email: hall4mj@ucmail.uc.edu, earleyja@mail.uc.edu, zimmese@mail.uc.edu, habanaj@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that we can collaborate on a project using github and know how to use Object Oriented programming.
Citations:
Anything else that's relevant:
'''
from ClassPackage.ConcessionClass import *
from ClassPackage.CarClass import *
from InventoryPackage.Inventory import *


# from the ConcessionClass
concession = Hamburger("American", 1)

PattyString = concession.__repr__() # shows that __repr__ method can be called on
print(PattyString)

cheeseString = concession.__str__() # shows that my __str__ method works 
print(cheeseString) 

concession.setpattynumber(0) # shows that the non dunder method works 
concession.setpattynumber(3) # putting something the if/else will accept

print(concession.__repr__())


#BREAK
print(" ")

# Inventory Module
print("Inventory Module Results: ")

#Instances of class
JB_01 = Jerseys("Joe Burrow Jersey", "Short", "Black", 15)
JC_01 = Jerseys("Ja'Marr Chase Jersey", "Long", "White", 8)

#Dunder Results
print(JB_01.__repr__())
print(JC_01.__str__())

#Method Result
print(JC_01.restock())
print(JB_01.changeQuantity(45))


#BREAK
print(" ")


#Car class
ferrariCars = Car("Ferrari 812 GTS", "V12", 211, 2.8, "8500 rpm")
#Print engine type
print(ferrariCars.engine)
#All car details
print(ferrariCars.__str__())
#Error checking
ferrariCars.setTopSpeed(-230)
ferrariCars.setAcceleration(-2.8)
# Fixing errors
ferrariCars.setTopSpeed(211)
ferrariCars.setAcceleration(2.8)

#Lists of multiple Ferrari cars
ferrariCars = [Car("Ferrari 812 GTS", "V12", 211, 2.8, "8500 rpm"),
               Car("Ferrari SF90 Stradale", "V8", 211, 2.5, "9200 rpm"),
               Car("Ferrari Portofino M", "V8", 199, 3.1, "7200 rpm"),
               Car("Ferrari Roma", "V8", 199, 3.2, "7500 rpm")]
#Details of every car in lists
for ferrariCars in ferrariCars:
        print(ferrariCars.__str__())

