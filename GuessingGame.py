import random
chances = 5
number = random.randint(1, 10)

print("Number guessing game")
print("Guess a number between 1 and 10")
print("You will get 5 tries")

while chances > 0:
    guess = int(input("Enter your guess:  "))
    if(guess > number and guess < 10 and guess > 0):
        print("Your guess was too high. Try a number lower than", guess)
        chances = chances - 1
    elif(guess < number and guess < 10 and guess > 0):
        print("Your number was too low. Try a number higher than", guess)
        chances = chances - 1
    elif(guess == number and guess < 10 and guess > 0):
        print("You win!! Congratulations!")
        break
    elif(guess > 9):
        print("Type a number between 1 and 10.", guess, "is greater than 10")
    elif(guess < 1):
        print("Type a number between 1 and 10.", guess, "is smaller than 1")

if(chances == 0):
    print("You lose!! Better luck next time! The number was", number)
