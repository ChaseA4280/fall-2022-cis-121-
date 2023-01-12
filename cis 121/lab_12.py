import random
class Company:
    def __init__(self,id,name):
        self.id = id
        self.name = name

class Car:
    def __init__(self,company,miles,speed,):
        self.company = company
        self.miles = miles
        self.speed = speed
        self.status =""
    
    def Accelerate(self,number):
        self.speed += int(number)
        self.status = "Accelerating"

    def stop(self):
        self.speed = 0 
        self.status = "stopped"

    def Decrease(self,number):
        self.speed -= int(number)
        self.status = "decreaseing"

    def info(self):
        print("===Company Info===")
        print(f"company: {self.company.name}")
        print(f"miles: {self.miles}")
        print(f"speed: {self.speed}")
        print(f"status: {self.status}")
        print("==================")


Ford = Company(12345,"Ford")

F150 = Car(Ford ,420000 , 97)

F150.info()

F150.Accelerate(98)

F150.info()

F150.stop()

F150.info()

F150.Decrease(20)

F150.info()



car1 = Car(Ford, 20000, 0)
car2 = Car(Ford, 20000, 0)
car3 = Car(Ford, 20000, 0)

def TimeTo60(Car):

    time = 0

    while Car.speed <= 60:
        temp = random.randint(1,50)
        Car.Accelerate(temp)
        time += 1
        print("vroom vroom")

    return time

info = {
    "car1": TimeTo60(car1),
    "car2": TimeTo60(car2),
    "car3": TimeTo60(car3)
}



print(info["car1"])


if info["car1"] < info["car2"] and info["car1"] < info["car3"]:
    print("car1 wins!")
elif info["car2"] < info["car1"] and info["car2"] < info["car3"]:
    print("car2 wins!")
elif info["car3"] < info["car1"] and info["car3"] < info["car2"]:
    print("car3 wins!")
else:
    print("it's a tie!")
