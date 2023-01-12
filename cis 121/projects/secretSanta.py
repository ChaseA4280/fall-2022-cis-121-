from privacy import sender
import random
import smtplib
class secretsanta:
    def __init__(self):
        self.info = dict()
        self.selection = dict()
        self.participants = 0
        self.budget = 0

    def getInfo(self):
        self.participants = int(input("how many participants are there: "))
        self.budget = int(input("what is the budget: "))

        for i in range(1 ,self.participants+1):
            name = input("what is the persons name {}: ".format(i))
            email = input("what is there email: ")
            self.info[name] = [email]
    

    def assign(self):
        choices = [name for name in self.info]

        for person in self.info:
            secretPerson = random.choice(choices)
            while secretPerson == person or secretPerson in self.selection:
                if secretPerson in self.selection and self.selection[secretPerson] == person:
                    continue
                elif secretPerson == person:
                    continue
                break
            self.selection[person] = secretPerson
            ind = choices.index(secretPerson)
            choices.pop(ind)



    def sendEmail(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender)
        print("login successful")
        for person,sp in self.selection.items():
            receiver = self.onfo[sp][1]
            sp_address = self.info[sp][1]
            sp_request = self.info[sp][2]
            message = "subject: secret santa\n" \
                      "Hello {},\n\n" \
                      "SHHH, your secret santa person is: {}.\n\n" \
                      "The budget of the gift exchange is ${}.\n\n" \
                      "Here is {}'s wishlist: {}\n\n" \
                      "This is their address to send the gift: {}\n\n" \
                      "Enjoy!".format(person,sp,self.budget,sp,sp_request,sp_address)
            server.sendmail(sender, receiver, message)
            print("{} has been sent their secret person.".format(person))
        server.quit()

    def start(self):
        self.getInfo()
        self.assign()
        self.sendEmail()

if __name__ == '__main__':
    secret_santa = secretsanta()
    secret_santa.start()

