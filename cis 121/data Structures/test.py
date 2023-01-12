# Adam chase
arrayOfMultiples = []
def Number(aNumber,aLength):
    aNumber = int(input("please enter a number:"))
    aLength = int(input("please enter a length:"))
    Number = ((aNumber + aNumber)**aLength)
    arrayOfMultiples.append(Number)
    return Number
print(arrayOfMultiples)