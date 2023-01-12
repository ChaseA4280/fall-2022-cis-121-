# hw 9.1

# class Student(object):
#     """Represents a student."""

#     def __init__(self, name, number):
#         """All scores are initially 0."""
#         self.name = name
#         self.scores = []
#         for count in range(number):
#             self.scores.append(0)

#     def getName(self):
#         """Returns the student's name."""
#         return self.name
  
#     def setScore(self, i, score):
#         return self.scores[i-1]

#     def getAverage(self):
#         return sum(self.scores) / len(self.scores)
   
#     def getHighScore(self):
#         """Returns the highest score."""
#         return max(self.scores)
 
    
    
        
#     # Write method definitions here
#     def __ge__(self, other):
#         return self.name >= other.name

#     def __eq__(self, other):
#         if self is other:
#             return True
#         elif type(self) != type(other):
#             return False
#         else:
#             return self.name == self.name
    
#     def __lt__(self, other):
#         return self.name < other.name

#     def __str__(self):
#         """Returns the string representation of the student."""
#         return "Name: " + self.name  + "\nScores: " + \
#                " ".join(map(str, self.scores))

# def main():
#     s1 = Student("adam", 10)
#     s2 = Student("paul", 10)
#     s3 = Student("james", 10)
#     print("False:", s1 == s2)
#     print("True:", s1 == s3)
#     print("True:", s1 == s1)
#     print("False:", s1 is s3)
#     print("True:", s1 < s2)
#     print("True:", s2 > s1)
#     print("True:", s2 >= s1)
#     print("True:", s1 >= s3) 
#     print("True:", s1 <= s2)
#     print("True:", s1 <= s3)

# if __name__ == "__main__":
#     main()

# hw 9.2

# import random


# class Student(object):
#     """Represents a student."""

#     def __init__(self, name, number):
#         """All scores are initially 0."""
#         self.name = name
#         self.scores = []
#         for count in range(number):
#             self.scores.append(0)

#     def getName(self):
#         """Returns the student's name."""
#         return self.name

#     def setScore(self, i, score):
#         """Resets the ith score, counting from 1."""
#         self.scores[i - 1] = score

#     def getScore(self, i):
#         """Returns the ith score, counting from 1."""
#         return self.scores[i - 1]

#     def getAverage(self):
#         """Returns the average score."""
#         return sum(self.scores) / len(self._scores)
    
#     def getHighScore(self):
#         """Returns the highest score."""
#         return max(self.scores)

#     def __str__(self):
#         """Returns the string representation of the student."""
#         return "Name: " + self.name  + "\nScores: " + \
#                " ".join(map(str, self.scores))

#     def __lt__(self, other):
#         """Returns self < other, with respect
#         to names."""
#         return self.name < other.name

#     def __ge__(self, other):
#         """Returns self >= other, with respect
#         to names."""
#         return self.name >= other.name

#     def __eq__(self, other):
#         """Tests for equality."""
#         if self is other: 
#             return True
#         elif type(self) != type(other):
#             return False
#         else:
#             return self.name == other.name

# def main():
#     """Tests sorting."""
#     # Create the list and put 5 students into it
#     list = []
#     for count in reversed(range(5)):
#         s = Student("Name" + str(count + 1), 10)
#         list.append(s)

#     print("sorted list of students:")
#     random.shuffle(list)
        
#     # Complete the definition of the main function
#     list.sort()

#     for obj in list:
#         print(obj.__str__())

# if __name__ == "__main__":
#     main()



