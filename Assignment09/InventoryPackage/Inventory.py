'''
Name: Sarah Zimmer (Group Balin)
email:zimmese@mail.uc.edu
Assignment: Assignment09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that we can collaborate on a project using github and know how to use Object Oriented programming.
Citations:
Anything else that's relevant:

Purpose: Model inventory at the Cincinnati Bengals merchandise store
'''
class Jerseys:
# Getter / Setters
    # name
    def get_name(self):
        return self.get_name 
    def set_name(self, name):
        self.get_name(name)
    # sleeve length
    def get_sleeves(self, sleeves):
        if sleeves == "Short" or "Long":
            print("Sleeve length must be either Short or Long.")
        else:
            return self.get_sleeves
    def set_sleeves(self, sleeves):
        self.get_sleeves(sleeves)
    # jersey color
    def get_color(self, color):
        if color == "Black" or "White" or "Orange" or "Pink":
            print("Not a valid jersey color.")
        else:
            return self.get_color
    def set_color(self, color):
        self.get_color(color)
    # quantity
    def get_quantity(self, quantity):
        if quantity < 0:
            print("Jersey quantity cannot be less than zero")
        else:
            self.get_quantity(quantity)
    def set_quantity(self, quantity):
        self.get_quantity(quantity)
# init 
    def __init__(self, name, sleeves, color, quantity):
        self.name = name;
        self.sleeves = sleeves;
        self.color = color;
        self.quantity = quantity;
        
# Dunder methods
    def __str__(self):
        return "Name= " + self.name + ", Sleeve Length= " + str(self.sleeves) + ", Color= " + str(self.color) + ", Stock quantity= " + str(self.quantity)
    def __repr__(self):
        return "Name: " + self.name + ", Sleeve Length: " + self.sleeves + ", Color: " + self.color + ", Stock quantity: " + str(self.quantity)
    
# Method 1: Check if an item is needed to be restocked
    def restock(self):
        if self.quantity <= 10:
            return "Additional stock of " + self.name + " needs to be ordered."
        else:
            return "Acceptable quantity in inventory."
    
# Method 2: Change the value of quantity for an instance
    def changeQuantity(self,x):
        self.quantity = x
        return "The updated quantity of " + self.name + " is " + str(self.quantity) + "."