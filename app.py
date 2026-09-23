# import math

# price = 10
# rating = 4.9
# name = "Bello"
# is_published = True
# print(price)

# name = "John Smith"
# age = 20
# is_new = True
# print()

# name = input("What is your name? ")
# print("Hi " + name)

# birth_year = input("Birth year: ")
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(type(age))
# print(age)

# string
# course = 'Python for beginners'
# another = course[:]
# print(another)

# first = "John"
# last = "smith"
# message = first + " [" + last + "] is a coder"
# ms = f'{first} [{last}] is a coder'
# print(ms)

# course = "Python for beginners"
# print(len(course))
# print(course.lower())
# print(course.upper())
# print(course.find("P"))
# print(course.replace("beginners", "Asolute beginners"))
# print("Python" in course)

# arithmetics
# print(10 + 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10**3)

# math functions
# print(round(2.9))
# print(abs(2.9))
# print(math.ceil(2.9))
# print(math.floor(2.9))

# if statements
# is_hot = False
# is_cold = True

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm")
# else:
#     print("Enjoy your day")
# temp = 20
# if temp > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

# weight = float(input("Weight: "))
# unit = input("(L)bs or (K)g: ")


# if unit.upper() == "L":
#     calc_weight = weight * 0.453592
#     calc_unit = "kg"
# else:
#     calc_weight = weight * 2.20462
#     calc_unit = "pounds"

# print(f"You are {round(calc_weight)} {(calc_unit)}")

# while loop
# i = 1

# while i <= 5:
#     print("*" * i)
#     i += 1
# print("Done")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You win!")
#         break
# else:
#     print("You lost")

# command = ""
# started = False


# while True:
#     command = input(">").lower()
#     if command == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not Started:
#             print("Car is already stopped")
#         else:
#             Started = False
#             print("Car stopped.")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry i dont understand this")


# for item in ["Rsd", "refsdws", "rdfvcwed"]:
#     print(item)

# for num in range(5, 10):
#     print(num)

# prices = [10, 20, 30]

# i = 0
# for item in prices:
#     i += item
# print(i)

# nested loops
# for x in range(4):
#     for y in range(3):
#         print(f"{x}, {y}")

# numbers = [5, 2, 5, 2, 2]

# for num in numbers:
#     print("x" * num)

# # lists
# names = ["fdc", "ssx", "ewdscx", "wsx"]
# print(names[0])  # index
# print(names[-1])  # index

# largest number in a list
# numbers = [3, 4, 6, 8, 8, 3, 1]
# max = numbers[0]
# for num in numbers:
#     if num > max:
#         max = num
# print(max)

# 2d lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
