#exam_review

#question 1: from the diagram I can see that there is for classes and it looks like one  parent class and three child classes.

#question 2: address is a parent class to person and grandparent to student and teacher class person class is the parent to teacher and studnet classes.


#question 3
#create Address class
class Address:
    def __init__(self,street,city,county,zipcode,state):
        self.street = street
        self.city = city
        self.county = county
        self.zipcode = zipcode
        self.state = state
#display all variables in the class
    def getAddress(self):
        return self.street

    def getCity(self):
        return self.city

    def getCounty(self):
        return self.county

    def getZipcode(self):
        return self.zipcode
    
    def getState(self):
        return self.state

    

    def getInfo(self):
        print("=====Address Info=====")
        print(f"Address: {self.street}")
        print(f"city: {self.city}")
        print(f"Zip Code:{self.zipcode}")
        print(f"State: {self.state}")
        print(f"County: {self.county}")

#create person class
class Person(Address):
    def __init__(self,street,city,county,zipcode,state,name,phoneNumber,emailAddress):
        super().__init__(street,city,county,zipcode,state)
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
#display all variables in class
    def getInfo(self):
        print("=====Address Info=====")
        print(f"Address: {self.street}")
        print(f"city: {self.city}")
        print(f"Zip Code:{self.zipcode}")
        print(f"State: {self.state}")
        print(f"County: {self.county}")
        print("======Person Info======")
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phoneNumber}")
        print(f"email address: {self.emailAddress}")


#create student class
class Student(Person):
    def __init__(self,street,city,county,zipcode,state,name,phoneNumber,emailAddress,studentNumber,gpa):
        super().__init__(street,city,county,zipcode,state,name,phoneNumber,emailAddress)
        self.studentNumber = int(studentNumber)
        self.gpa = float(gpa)

    def getGPA(self):
        return self.gpa

    def getstudentNumber(self):
        return self.studentNumber

#display all variables in class
    def getInfo(self):
        print("=====Student Address Info=====")
        print(f"Address: {self.street}")
        print(f"city: {self.city}")
        print(f"Zip Code:{self.zipcode}")
        print(f"State: {self.state}")
        print(f"County: {self.county}")
        print("======Student Info======")
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phoneNumber}")
        print(f"email address: {self.emailAddress}") 
        print(f"Stundent Number: {self.studentNumber}")
        print(f"GPA: {self.gpa}")
#create Teacher class
class Teacher(Person):
    def __init__(self,street,city,county,zipcode,state,name,phoneNumber,emailAddress,teacherID,workhours,work_rate,years_of_service):
        super().__init__(street,city,county,zipcode,state,name,phoneNumber,emailAddress)
        self.teacherID = int(teacherID)
        self.workhours = int(workhours)
        self.work_rate = int(work_rate)
        self.years_of_service = int(years_of_service)
#display all variables in class
    def getTeacherID(self):
        return self.teacherID

    def getWorkHours(self):
        return self.workhours

    def getWork_rate(self):
        return self.work_rate

    def getYearsOfService(self):
        return self.years_of_service

    def getInfo(self):
        print("=====Teacher Address Info=====")
        print(f"Address: {self.street}")
        print(f"city: {self.city}")
        print(f"Zip Code:{self.zipcode}")
        print(f"State: {self.state}")
        print(f"County: {self.county}")
        print("======Teacher Info======")
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phoneNumber}")
        print(f"email address: {self.emailAddress}")
        print(f"Teacher ID: {self.teacherID}")
        print(f"Work Hours: {self.workhours}")
        print(f"work Rate: {self.work_rate}")
        print(f"years of service: {self.years_of_service}")

home = Address("joseph path","mankato","mcleod","56001","MN")
home.getInfo()

Adam = Person("joseph path","mankato","mcleod","56001","MN","Adam","612-961-4524","buck@gmail.com")
Adam.getInfo()

student = Student("joseph path","mankato","mcleod","56001","MN","Adam","612-961-4524","buck@gmail.com","806055","3.2")
student.getInfo()

teacher = Teacher("Troy lane","kato","carver","56424","MN","kendrick","78273819","ajshjh@gmail.com","837289","45","40","12")
teacher.getInfo()

    

    




    

