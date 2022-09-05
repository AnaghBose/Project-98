import random
print("Number guessing game")
number = random.randint(1, 9)
chances = 0
print("Guess a number(From 1 to 9):")
while chances < 5:
    guess = int(input("Enter Your Guess:"))
if guess == number:
    print("Congratulation ! Your guess was correct !!")
elif guess < number:
    print("OOPS ! Your guess was lower than than the number: Guess a number higher than", guess)
else:
     print("Your guess was higher than the number: Guess a number higher than", guess)
chances += 1
if not chances < 5:
    print("You lost ! The number was", number)
