
#Activity 1: designing a class

#class
class Vehicle:
	#attribute and a constructor method
  def __init__(self):
    self.color = "Red"  
    
  def model(self):
    print("Audi")

#inherit a vehicle class
class Car(Vehicle):
  def drive(self):
    	#print color of a car
    return self.color
        
#objects        
car = Car()
vehicle = Vehicle()

print(car.drive())
vehicle.model()


#Activity 2: Polymorphism
#Class
class Horse:
  def move(self):
    return "Horse move with four feet."
        
class Chicken:
  def move(self):
    return "Chicken move with 2 feet."
        
for animal in [Horse(),Chicken()]:
  print(animal.move())
