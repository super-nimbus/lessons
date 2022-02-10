'''
A class is a definition of requirements/schema OR a template OR a guarantee of structure for a group of related objects 

Double underscore functions (ex __init__, __print__, __iter___, etc) - come back to this 

java/ in any OOP (object oriented programming) (also functional programming, imperative programming = programming paradigms)
- constructors
- destructors
- other implementation methods (in python, we call them the double underscore class methods, a special naming convention)
double underscore AKA dunder methods are a set of special keywords 
'''
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # how to intrepret this class/object as a string?
#     def __str__(self):
#         return f"i am {self.name} and i am {self.age} years old"

#     # attribute function
#     def sayHello(self):
#         print("hello! my name is ", self.name)

# allen = Person("allen", 20)
# # allen.sayHello()
# kevin = Person("kevin", 21)

# allen.sayHello

# print(allen)
# print(kevin)

# lets talk about class inheritance
'''
class inheritance
the child class inherits all of the parent class's attributes and attribute functions
'''
# a car (child class) is one type of vehicle (parent class)


class Vehicle:
    def __init__(self, maker, color, numWheels, topSpeed, gasCapacity):
        self.maker = maker
        self.color = color
        self.numWheels = numWheels
        self.topSpeed = topSpeed
        self.gasCapacity = gasCapacity
    
    def honkHorn(self):
        print("beep beep I have ", self.numWheels, " wheels")


class Motorcycle(Vehicle):
     def __init__(self, maker, color, helmets):
        # super() returns the parent class (here super() = Vehicle)
        super().__init__(maker, color, 2, 150, 30)

        self.helmets = helmets

myBike = Motorcycle("honda", "red", 2)
print("helmets", myBike.helmets)
print("bike topspeed", myBike.topSpeed)
myBike.honkHorn()
#sads


class Car(Vehicle): # an idea or an blueprint

    # __init__ is your constructor, pass in all the information you need to "create" or "define" a Car
    # def __init__(self, manufacturer, model, license_plate, color):
    def __init__(self, maker, color, front_seats, back_seats):
        # super() returns the parent class (here super() = Vehicle)
        super().__init__(maker, color, 4, 100, 75)

        # each self._____ is an attribute attached to the self, which an instance (an object) of the class
        # self.model = model
        # self.plate = license_plate
        self.front_row_seats = front_seats
        self.back_row_seats = back_seats

    #attribute functions
    def printColor(self):
        print(self.color)
        return(self.color)

    def getCapacity(self):
        return(self.front_row_seats + self.back_row_seats)

#Car() # call the class constructor to create a car
# myCar is an actual Car object
# myCar = Car('Toyota', 'Camry', 'bigmoney3fast', 'silver')
# kevinsCar = Car('Mercedes', 'GWagon', 'movefastmakecash', 'black')

kevinsCar = Car('Ford', "silver", 2, 3)
allensCar = Car("mini", "red", 1, 1)
print("kevin's car color:", kevinsCar.color)
kevinsCar.honkHorn()

# print(isinstance(kevinsCar, Vehicle))
# print(isinstance(kevinsCar, Car))

# print(kevinsCar.color)
# kevinsCar.printColor()

# print("kevins car has ", kevinsCar.getCapacity(), " seats")
# print("allens car has ", allensCar.getCapacity(), " seats")


# print(hasattr(myCar, "plate"))
# print(hasattr(myCar, "num_seats"))

# exception = error, diff languages call it different names but its the same concept

# sometimes an exception is unexpected and crashes our program (see below)
# print(getattr(myCar, "num_seats"))
# print("after error")

# try: 
#     if not hasattr(myCar, "num_seats"):
#         raise Exception("im broken")
# except Exception(e):
#     print(e)

# print("my car is made by: ", myCar.maker)
# print("my car model is: ", myCar.model)
# print("my license plate is: ", myCar.plate)
# print("my car is colored: ", myCar.color)

# ourCars = [myCar, kevinsCar]

# print("here are our cars")
# for car in ourCars:
#     print(car.plate)

# "allen is an object instance of a Person"
# print(isinstance(allen, Person))
# print(isinstance(allen, Car))
# print(isinstance())







#------- person example

# Kevin = {
# 	'Name': 'kevin',
# 	"Age" : 20,
# 	"Height (cm)": 180,
# }

# Allen = {
# 	'Name': 'allen',
# 	"Age" : 20,
# 	"Height (cm)": 180,
# }

# Jeff = {
# 	'Name': 'Jeff',
# }
# # '' # single quotes OR apostrophes
# # "" # double quotes OR quotation marks

# people = [Jeff]

# # sum = 0 
# try: 
#     for person in people:
#         print(person["Name"])
#         sum += person["Age"]
#     print(sum/len(people))
# except Exception: # an exception handler --> handles and resolves the error as appropriate
#     print("an error occured")
#     raise KeyError("you messed up")

# print("end")
