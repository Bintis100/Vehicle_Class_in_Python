# Name: Binta Drammeh
# email: Drammeba@mail.uc.edu
# Assignment Number: Inclass Assignment
# Due Date: February 27, 2024
# Course/Section: IS 4030 - 002
# Semester/Year: Spring 2024
# Brief Description of the assignment: In class assignment
# Citations:
# Anything else that's relevant:

#VehicleClass.py

class Vehicle:
    '''
    Vehicle Class
    This class models a vehicle and it's on a used car lot
    Change Order: we need to add maximum speed to the model
    Change Order: need a way to 'read' the maximum speed from the model
    Change Order: Some developers need to use the constructor without having to provide a maximum speed
    '''
    #Constructor. It's called when we  .. we instantiate an object of vehicle type   
    def __init__(self, type, max_speed = None):
        '''
        @param: The type of vehicle
        @param max_speed: Maximum speed of the Vehicle, defaults to None 
        '''
        self.type = type;
        self._thisisprivate = 42 #This is a weak attempt to 'support' data hiding
        self.max_speed = max_speed  #saves a copy in the current object

    # A instance method. It operates on an instance of the vehicle class
    def printType(self):
        print(self.type);
        
    def getSpeed(self): #"a getter"
        return self.max_speed;

if __name__ == "__main__":
    # Some code to test the class would go here.
    # If there's no code, just pass
    pass

