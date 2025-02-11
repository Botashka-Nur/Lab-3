#First task
class StringManipulator:
    def __init__(self):
        self.text=""
    
    def getString(self):
        self.text=input()

    def printString(self):
        print(self.text.upper())

obj=StringManipulator()

obj.getString()
obj.printString()




#Second Task
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length=length

    def area(self):
        return self.length*self.length

shape=Shape()
square=Square(5)


print("Shape area:", shape.area()) 
print("Square area:", square.area())



#Third task
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self , length , width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width
    
shape=Shape()
print( shape.area())

rectangle = Rectangle(5, 3)
print(rectangle.area())




#4th task
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y
        print(f"Moved to new coordinates: ({self.x}, {self.y})")

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

point1 = Point(x1, y1)
point2 = Point(x2, y2)

point1.show()
point2.show()

distance = point1.dist(point2)
print(f"Distance between point1 and point2: {distance}")

x_new = float(input())
y_new = float(input())
point1.move(x_new, y_new)
point1.show()




#5th task 
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(self.balance)
        else:
            print(f"Insufficient funds. Current balance: {self.balance}")

owner = input()
balance = float(input())
account = Account(owner, balance)

while True:
    action = input().lower()
    if action == "deposit":
        amount = float(input())
        account.deposit(amount)
    elif action == "withdraw":
        amount = float(input())
        account.withdraw(amount)
    elif action == "exit":
        break



#6th task
numbers = list(map(int, input().split()))

prime_numbers = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) if x > 1 else False, numbers))

print(prime_numbers)