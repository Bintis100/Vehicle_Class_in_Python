# Name: Binta Drammeh
# email: Drammeba@mail.uc.edu
# Assignment Number: Inclass Assignment
# Due Date: February 27, 2024
# Course/Section: IS 4030 - 002
# Semester/Year: Spring 2024
# Brief Description of the assignment: In Class Assignment
# Citations:
# Anything else that's relevant:

# main.py

#add import statement
from VehiclePackage.VehicleClass import *


if __name__ == "__main__":
    #instantiate an object if type Vehicle
    myCorvette = Vehicle ("car", 120)   #trigger  call to to constructor
    myCorvette.printType()  #invoke the method on the object 
    
    #Invoke the getter for maximum speed, store the return in a variable
    #print that to the console
    maximum_speed = myCorvette.getSpeed() 
    print("Maximum speed:",maximum_speed)
    
    #instantiate another Vehicle object. You van name it
    myCorolla = Vehicle("Car") # myCorolla is an object to the object type
    
    #I want a list of 3 Vehicles: Car, Boat, space Ship
    #You can pick the names and properties
    #I want some friendly output to demonstrate what you just did
    myVehicles = [ Vehicle("Nissan",150),
                  Vehicle ("Boat",10),
                 Vehicle ("Ultimate Spaceship", 10000)]
    #iterate over the list
    for vehicle in myVehicles:
            vehicle.printType()
            print(vehicle.getSpeed())
            
    