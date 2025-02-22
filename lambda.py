#Syntax
#lambda arguments : expression

#Example

#1
x = lambda a : a + 10
print(x(5))

#2
x = lambda a, b : a * b
print(x(5, 6))

#3
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#4
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(12))


#5
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(12))


#6
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(12))
print(mytripler(12))

