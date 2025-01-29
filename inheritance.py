#Create a Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("Aygerim", "Don")
x.printname()

#Create a Child Class
class Student(Person):
  pass
x = Student("Lyazzat", "Guldana")
x.printname()


#Add the __init__() Function
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2024 


#Example
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Akbota", "Nurkasymova", 2028)

#Add Methods
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to university KBTU", self.graduationyear)