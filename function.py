#Example
def my_function():
  print("Hi KBTU!")

#Calling a Function
def my_function():
  print("Hi KBTU!")

my_function()


#Arguments (examples)
def my_function(fname):
  print(fname + "information")

my_function("support")
my_function("method")
my_function("email")


#Number of Arguments
#This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("akbota", "nurkasymova")


#Arbitrary Arguments, *args
def my_function(*cars):
  print("My first car " + cars[0])

my_function("Mers", "Bmw", "Passat")


#Keyword Arguments
def my_function(fruit3, fruit2, fruit1):
  print("The expensive fruit is  " + fruit3)

my_function(fruit1 = "Yubari King Melon", fruit2 = "Densuke Watermelon", fruit3 = "Taiyo no Tamago Mango")





