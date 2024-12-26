Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Person:
...   def __init__(self, fname, lname):
...     self.firstname = fname
...     self.lastname = lname
... 
...   def printname(self):
...     print(self.firstname, self.lastname)
... 
... class Student(Person):
...   def __init__(self, fname, lname, year):
...     super().__init__(fname, lname)
...     self.graduationyear = year
... 
...   def welcome(self):
...     print("go", self.firstname, self.lastname, "to the class of", self.graduationyear)
... 
... x = Student("Mike", "Olsen", 2024)
... x.welcome()
