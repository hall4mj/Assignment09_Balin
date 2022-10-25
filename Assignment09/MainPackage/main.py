'''
Name: Group Balin: Matthew Hall, Joshua Earley, Sarah Zimmer, Alex Haban
email: hall4mj@ucmail.uc.edu, earleyja@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that we can collaborate on a project using github and know how to use Object Oriented programming.
Citations:
Anything else that's relevant:
'''
from ClassPackage.ConcessionClass import *



# from the ConcessionClass
concession = Hamburger("American", 1)

PattyString = concession.__repr__() # shows that __repr__ method can be called on
print(PattyString)

cheeseString = concession.__str__() # shows that my __str__ method works 
print(cheeseString) 

concession.setpattynumber(0) # shows that the non dunder method works 
concession.setpattynumber(3) # putting something the if/else will accept

print(concession.__repr__())