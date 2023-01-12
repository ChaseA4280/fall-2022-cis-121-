from lab_12 import *

import random

Ford = Company(1234,"Ford")

Car = Car(Ford, 420000, 0)

time = 0

while Car.speed <= 60:
    temp = random.randint(1,50)
    Car.Accelerate(temp)
    time += 1
    print("vroom vroom")

print(f"car speed:{Car.speed}")
print(f"total time: {time}")