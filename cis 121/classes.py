class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name 




class SalaryEmployee(Employee):
    def __init__(self,id,name,weekly):
        super().__init__(id,name)
        self.weekly = weekly
    def CalcPayroll(self):
        return self.weekly 
    
    def printInfo(self):
        print("========salary info========")
        print(f"name:{self.name}")
        print(f"id:{self.id}")
        print(f"weekly:{self.weekly}")
        print(f" total salary this week:{self.CalcPayroll()}")




class HourlyEmployee(Employee):
    def __init__(self,id,name, hourly_rate,hours):
        super().__init__(id,name)
        self.hourly_rate = hourly_rate
        self.hours = hours
    def CalcPayroll(self):
        return self.hourly_rate * self.hours

    def printInfo(self):
        print("========comission info========")
        print(f"name:{self.name}")
        print(f"id:{self.id}")
        print(f"weekly:{self.hourly_rate}")
        print(f"hours:{self.hours}")
        print(f" total salary this week:{self.CalcPayroll()}")



class ComissionEmployee(SalaryEmployee):
    def __init__(self,id,name,weekly,comission):
        super().__init__(id,name,weekly)
        self.comission = comission

    def CalcPayroll(self):
        return super().CalcPayroll() + self.comission

    def printInfo(self):
        print("========comission info========")
        print(f"name:{self.name}")
        print(f"id:{self.id}")
        print(f"weekly:{self.weekly}")
        print(f"comission:{self.comission}")
        print(f" total salary this week:{self.CalcPayroll()}")



    
  
