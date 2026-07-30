# name = str(input("Enter your name: "))
# age = int(input("Enter your age: "))
# age = age + 10
# print(f"Hi {name}, in ten years you will be {age}!")

# roller coaster
# height = int(input("Enter your height in centimeters: "))

# if height >= 140:
#     print("You are tall enough to ride!")

# else:
#     print("Sorry, you need to grow a bit more first")

# movie tickets
# age = int(input("Enter your age: "))

# if age < 12:
#     print("Your ticket is $5.")

# elif age >= 65:
#     print("Your ticket is $8.")

# else:
#     print("Your ticket is $12.")

# secret password
# secret = "penguin"
# guess = ""

# while guess != secret:
#     guess = str(input("Enter the password: "))

# print("Access granted!")

# guessing game
# import random 

# secret_number = random.randint(1, 100)
# guess = 0

# while guess != secret_number:
#     guess = int(input("Enter an number between 1 and 100: "))
#     if guess > secret_number:
#         print("Too high!")

#     elif guess < secret_number:
#         print("Too low!")

# print("You got it!")

# rock, paper, scissors
# import random
# options = ["rock", "paper", "sissors"]

# while True:
#     user_choice = input("Choose rock, paper, sissors, or quit: ")
#     if user_choice == "quit":
#         break

#     computer_choice = random.choice(options)
#     print("Computer chose", computer_choice)

#     if user_choice == "rock" and computer_choice == "sissors":
#         print("You win 🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧")

#     elif user_choice == "paper" and computer_choice == "sissors":
#         print("computer won!")

#     elif user_choice == "sissors" and computer_choice == "paper":
#         print("You won!🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧")
        
#     elif user_choice == "sissors" and computer_choice == "rock":
#         print("computer won!")

#     elif user_choice == "sissors" and computer_choice == "sissors":
#         print("its a tie!")

#     elif user_choice == "paper" and computer_choice == "rock":
#           print("You won!🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧")

#     elif user_choice == "paper" and computer_choice == "sissors":
#             print("computer won!")
    
#     elif user_choice == "sissors" and computer_choice == "paper":
#             print("You won!🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧")
            
#     elif user_choice == "rock" and computer_choice == "paper":
#             print("computer won!")
    
#     elif user_choice == "paper" and computer_choice == "paper":
#             print("its a tie!")

#     elif user_choice == "paper" and computer_choice == "rock":
#           print("You won!🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧")

#     elif user_choice == "sissors" and computer_choice == "rock":
#             print("computer won!")
    
#     elif user_choice == "rock" and computer_choice == "sissors":
#             print("You won!🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧")
            
#     elif user_choice == "rock" and computer_choice == "paper":
#             print("computer won!")
    
#     elif user_choice == "rock" and computer_choice == "rock":
#             print("its a tie!")

#pet sim
# hunger = 50
# happiness = 50
# energy = 50
# pet = input("What animal is your pet?: ")
# print(f"Wow  you have a {pet} as a pet!")

# while True:
#     print("Hunger:", hunger, "| Happiness:", happiness)
#     choice = input("1. Feed pet\n2. Play with pet\n3. Quit\n4. rest\nChoose an option: ")

#     if choice == "3":
#         break

#     elif choice == "1":
#         hunger -= 10
#         happiness += 5
#         print(f"Your {pet} is full!")

#     elif choice == "2":
#         happiness += 10
#         hunger -= 5
#         print(f"Your {pet} is happy")

#     elif choice == "4":
#         energy += 10
#         happiness += 5
#         print(f"Your {pet} is rested")

# turtle
# import turtle
# t = turtle.Turtle()
# t.color("blue")
# t.shape("turtle")

# for i in range(4):
#     t.fd(100)
#     t.rt(90)

# for i in range(360):
#     t.speed(0)
#     t.forward(1)
#     t.color("red")
#     t.right(1)

# t.color("green")
# t.right(45)
# t.forward(75)
# t.right(92)
# t.forward(70)
# t.penup()
# t.right(135)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.pendown()
# t.right(135)
# t.forward(72)
# t.left(90)
# t.forward(70)
# colors = ["blue", "orange", "yellow"]
# for i in range(360):
#     t.speed(0)
#     t.color(colors)
#     t.circle(50)
#     t.right(10)

# turtle.done()
# import turtle
# import math

# # 1. Set up the screen and turtle
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.colormode(255)

# t = turtle.Turtle()
# t.speed(0)
# t.penup()

# # 2. Draw the colorful helix
# for i in range(360):
#     # Calculate math coordinates for a spiraling helix pattern
#     x = math.cos(i * 0.1) * 100
#     y = i - 180  # Centers the helix vertically
    
#     # Move the turtle to the calculated position
#     t.setposition(x, y)
#     t.pendown()
    
#     # Cycle the pen color based on the loop counter
#     t.pencolor(i % 255, (i * 2) % 255, (i * 3) % 255)
    
#     # Draw a tiny dot or step at each point to form the smooth line
#     t.dot(5)

# # 3. Clean up and finish
# t.hideturtle()
# turtle.done()

# adventure
inventory = []
current_room = "dungeon"

while True:
    if current_room == "dungeon":
        print("You are in a dark, cold dungeon. There is a hevy wooden door to your NORTH and a shiny key on the floor.\n1. pick up the key and open the door\n2. break the door\n3. quit")
        choice = input("What do you want to do?: ")

        if choice == "1":
            inventory.append("key")
            print("You open the door and find a dragon sleeping in a pile of treasure")
            current_room = "treasure room"

        if choice == "2":
            print("While trying to break the door you slipped over a banana peel and broke your shoulder")

        if choice == "3":
            break

    elif current_room == 'treasure room':
        print("When you opened the door you find a giant room full of treasures it feels like heaven but in the middle of the room lays an enourmous res fire-breathing dragon")








    





