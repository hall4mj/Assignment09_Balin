'''
Name: Group Balin
email: hall4mj@ucmail.uc.edu , zimmese@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that we can collaborate on a project using github and know how to use Object Oriented programming.
Citations:
Anything else that's relevant:
'''
print("Mammal Module Results:")
from ClassPackage.MammalClass import Mammal

if __name__ == "__main__":
# Instaniates the myAnimal object
    myAnimal = Mammal("Bear", "Fish", "Forest")
    # here is the __str___ requirement
    print (myAnimal.__str__())

### Inventory Module ###
print("Inventory Module Results:")
from InventoryPackage.Inventory import *

#Instances of class
JB_01 = Jerseys("Joe Burrow Jersey", "Short", "Black", 16)
JC_01 = Jerseys("Ja'Marr Chase Jersey", "Long", "White", 10)

# Dunder Results
print(JB_01.__repr__())
print(JC_01.__str__())

# Method Results
print(JC_01.restock())
print(JB_01.changeQuantity(30))
