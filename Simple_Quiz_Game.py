print("Hello World")
print("Welcome to the simple quiz game!!")

# getting input from user to see if they want to play or exit the game.
playing = input("Do you want to play? ")
if playing != "yes":
    print("Goodbye..come around again")
    quit()


print("Okay! ------Lets Play------")

# declearing a variable to keep tab of the scores
score = 0

# getting user input (answer)
userInputAnswer = input("What are functions defined with ").lower()
if userInputAnswer == "def":
    print("Correct")
    score += 1
else:
    print("Wrong Answer")
#def
userInputAnswer = input("Python can run on ... ").lower()
if userInputAnswer == "client and server":
    print("Correct")
    score += 1
else:
    print("Wrong Answer")
#client and server

userInputAnswer = input("You can use this module in python to create GUI programs? ").lower()
if userInputAnswer == "tkinter":
    print("Correct")
    score += 1
else:
    print("Wrong Answer")
#Tkinter.....GUI

userInputAnswer = input("Is Python case sensitive? ").lower()
if userInputAnswer == "yes":
    print("Correct")
    score += 1
else:
    print("Wrong Answer")
#yes

userInputAnswer = input("Tuple in python are immutable? ...True or False: ").lower()
if userInputAnswer == "true":
    print("Correct")
    score += 1
else:
    print("Wrong Answer")

userInputAnswer = input("/* is a character used for writing comments in Python ..True or  False: ").lower()
if userInputAnswer == "false":
    print("Correct")
    score += 1
else:
    print("Wrong Answer")
#false

userInputAnswer = input("What does RAM stand for? ").lower()
if userInputAnswer == "random access memory":
    print("Correct")
    score += 1
else:
    print("Wrong Answer")

userInputAnswer = input("Python a complier or interpreter? ").lower()
if userInputAnswer == "interpreter":
    print("Correct")
    score += 1
else:
    print("Wrong Answer")


# printing out the scores for the user input
print(f"You got {score} questions correct")
print(f"You total for this quiz is {(score/8)* 100 }% percent")




