class Document:
    def __init__(self,authors,date):
        self.authors = authors
        self.date = date 

    def getAuthors(self):
        return self.authors
    
    def addAuthors(self,name):

        if type(name) == str:

            self.authors.append(name)

        if name in self.authors:
            print(f"name:{name} added to the list of authors!")

        else:
            print("there was an error")

    def getDate(self):
        return self.date
    
    def getInfo(self):
        print("=======Document info=======")
        print(f"authors:{self.authors}")
        print(f"date:{self.date}")
        


class Book(Document):

    def __init__(self,authors,date,title):
        super().__init__(authors,date)
        self.title = title

    def getTitle(self):
        return self.title

    def getInfo(self):
        print("=======book info=======")
        print(f"authors:{self.authors}")
        print(f"date:{self.date}")
        print(f"title:{self.title}")
        

class Email(Document):

    def __init__(self,authors,date,subject,to):
        super().__init__(authors,date)
        self.subject = subject
        self.to = to 
    
    def getSubject(self):
        return self.subject

    def getTo(self):
        return self.to

    def getInfo(self):
        print("=======email info=======")
        print(f"authors:{self.authors}")
        print(f"date:{self.date}")
        print(f"subject:{self.subject}")
        print(f"to:{self.to}")

        

doc1 = Document(["adam chase"],"12/12/2002")
doc1.getInfo()
# print(doc1.getAuthors())
# print(doc1.getDate())
# doc1.addAuthors("jeff gorden")
# print(doc1.getAuthors())

# print("\n\n\n")

# #book class testing
# print("book class testing")
book = Book(["Adam Chase"], "12/12/2002","black belt")
book.getInfo()
# print(book.getTitle())
# print(book.getAuthors())
# print(book.getDate())

# print("\n\n\n")

# #email class testing

# print("email class testing")

# #create a method in each class to display all info 

email = Email(["Adam Chase"],"12/12/2002","book","jeff")
email.getInfo()

