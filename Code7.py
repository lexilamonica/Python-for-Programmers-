#
# Author: Lexi LaMonica
# All rights reserved
#

class Vehicle:
    def __init__(self, mode, maxPassengers, odometer):
        self.mode = mode
        self.maxPassengers = maxPassengers
        self.odometer = odometer

    def odometerAdd(self, value):
        self.odometer += value
  
    def __eq__(self, other):
        if self.mode!= other.mode or self.maxPassengers != other.maxPassengers or self.odometer != other.odometer:
            return False
        else:
             return True
  
    def __str__(self):
        record = "The mode of transport is: " + self.mode + "\n"
        record += "Can carry up to: " + str(self.maxPassengers) + "\n"
        record += "Odometer: "+ str(self.odometer)
        return record

class Car(Vehicle):
    def __init__(self, mode, maxPassengers, odometer, make, model, color):
        super().__init__(mode, maxPassengers, odometer)
        self.make = make
        self.model = model
        self.color = color

class Boat(Vehicle):
    def __init__(self, mode, maxPassengers, odometer, length, horsepower):
        super().__init__(mode, maxPassengers, odometer)
        self.length = length
        self.horsepower = horsepower


