# question 1
#make vehicle class
class Vehicle:
    # create init fuction for all varibles the class contains
    def __init__(self, numPassengers, manufacturer, numWheels):
        self.numPassengers = int(numPassengers)
        self.manufacturer = manufacturer
        self.numWheels =  int(numWheels)

#make automobile class
class Automobile(Vehicle):
    # create init fuction for all varibles the class contains
    def __init__(self ,numPassengers, manufacturer, numWheels, mpg, model, numDoors):
        # create super for all varibles contained in the parent classes 
        super().__init__(numPassengers, manufacturer, numWheels)
        # create self statments for the new varibles
        self.mpg = float(mpg)
        self.model = model
        self.numDoors = int(numDoors)

#make sedan class
class Sedan(Automobile):
    # create init fuction for all varibles the class contains
    def __init__(self, numPassengers, manufacturer, numWheels, mpg, model, numDoors, type, numCylinders, horsepower):
        # create super for all varibles contained in the parent classes 
        super().__init__(numPassengers, manufacturer, numWheels, mpg, model, numDoors)
        # create self statments for the new varibles
        self.type = type
        self.numCylinders = int(numCylinders)
        self.horsepower = float(horsepower)
  
#make truck class
class Truck(Automobile):
    # create init fuction for all varibles the class contains
    def __init__(self, numPassengers, manufacturer, numWheels, mpg, model, numDoors, type, numAxles, maxTowPayload):
        # create super for all varibles contained in the parent classes 
        super().__init__(numPassengers, manufacturer, numWheels, mpg, model, numDoors)
        # create self statments for the new varibles
        self.type = type
        self.numAxles = int(numAxles)
        self.maxTowPayload = int(maxTowPayload)

#make two wheeler class
class TwoWheeler(Vehicle):
    # create init fuction for all varibles the class contains
    def __init__(self,numPassengers, manufacturer, numWheels, model, weight):
        # create super for all varibles contained in the parent classes 
        super().__init__(numPassengers, manufacturer, numWheels)
        # create self statments for the new varibles
        self.model = model 
        self.weight = int(weight)

#make motorcycle class
class Motorcycle(TwoWheeler):
    # create init fuction for all varibles the class contains
    def __init__(self, numPassengers, manufacturer, numWheels, model, weight, type, mpg, horsepower):
        # create super for all varibles contained in the parent classes 
        super().__init__(numPassengers, manufacturer, numWheels, model, weight)
        # create self statments for the new varibles
        self.type = type
        self.mpg = float(mpg)
        self.horsepower = int(horsepower)


# make bicycle class
class Bicycle(TwoWheeler):
    # create init fuction for all varibles the class contains
    def __init__(self, numPassengers, manufacturer, numWheels, model, weight, hasGears, hasSuspension, wheelSize):
        # create super for all varibles contained in the parent classes 
        super().__init__(numPassengers, manufacturer, numWheels, model, weight)
        # create self statments for the new varibles 
        self.hasGears = hasGears
        self.hasSuspension = hasSuspension
        self.wheelSize = float(wheelSize)


# question 2: vehicle is the first parent class to Automobile and TwoWheeler. and that leads to Automobile being a parent class tp sedan and truck, and Two wheeler class being a parent to Motorcycle and Bicycle class. which mean s Vehicle is the grandparent class to Sedan, Truck, Motocycle, Bicycle.


# question 3: 

# create customer class
class Customer:
    # make init function for all variable in class
    def __init__(self): 
        # make self statements
        self.totalPurchase = 0
        self.discountReached = False
        
    # make a function that determines if the customer recieves 
    def makePurchase(self, totalPurchase):
        
        result = totalPurchase
        # calculate
        if self.discountReached:
            result -= 10
            if result < 0:
                result = 0
            self.discountReached == False
        self.totalPurchase += result
        # check if the customer recieves a discount
        if self.totalPurchase >= 100:
            self.discountReached = True
            print("yay you recieve a discount on your next purchase")
        else:
            self.discountReached = False
            print("if you want to blow your money on another pointless pair of cloths you will recieve a discount")
        self.totalPurchase %= 100
        #return function 
        
        return result

    # return discount reached variable in a function 
    def DiscountReached(self):
        return self.discountReached

# test subjects
subject = Customer()
# create amount of first purchase
subject.makePurchase(100)
# test to see if discount is recieved 
print (subject.DiscountReached())
# make amount for second purchase
subject.makePurchase(100)
# test to see if discount is recieved 
print(subject.DiscountReached())
# make third purchase
subject.makePurchase(20)
# test to see if disocunt is recieved 
print(subject.DiscountReached())


