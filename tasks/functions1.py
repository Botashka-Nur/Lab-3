#task 1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = float(input())
ounces = grams_to_ounces(grams)

print(f"{grams} grams is equal to {ounces} ounces.")


#task 2 
fahrenheit = float(input())
centigrade = (5 / 9) * (fahrenheit - 32)
print(centigrade)


#task 3
def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y
    return x, y


#task 4 
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]


#task 5 
import itertools

def print_permutations():
    user_input = input()
    permutations = itertools.permutations(user_input)
    for perm in permutations:
        print(''.join(perm))


#task 6
def reverse_words():
    user_input = input()
    words = user_input.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence


#task 7 
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


#task 8 
def spy_game(nums):
    sequence = [0, 0, 7]
    index = 0
    for num in nums:
        if num == sequence[index]:
            index += 1
        if index == len(sequence):
            return True
    return False


#task 9 
import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3


#task 10 
def unique_elements(nums):
    unique_list = []
    for num in nums:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


#task 11
def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]


#task 12 
def histogram(lst):
    for num in lst:
        print('*' * num)


#task 13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20)
    guess_count = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())
        guess_count += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guess_count} guesses!")
            break

guess_the_number()


#task 14
import random
import math

def unique_elements(nums):
    unique_list = []
    for num in nums:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20)
    guess_count = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())
        guess_count += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guess_count} guesses!")
            break

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def histogram(lst):
    for num in lst:
        print('*' * num)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(nums):
    return [num for num in nums if is_prime(num)]