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


#Arbitrary Keyword Arguments, **kwargs
def my_function(**sb):
  print("My first subject " + sb["lname"])

my_function(fname = "Calculus 1", lname = "PP1")


#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("KZ")
my_function()
my_function("Argentina")


#Passing a List as an Argument
def my_function(celebration):
  for x in celebration:
    print(x)

celebration = ["birthday", "Nauryz", "New year"]

my_function(celebration)


#Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


#Positional-Only Arguments
def my_function(x, /):
  print(x)

my_function(3)


#Keyword-Only Arguments
def my_function(*, x):
  print(x)

my_function(x = 3)


#Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)