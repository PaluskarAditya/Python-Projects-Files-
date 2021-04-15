import random  #I have used random module in this game for using random itegers

tries = 0

print("Hey! Welcome to the guess Guessing Game.")
print()

answer = random.randint(1,10)
print(answer)   #If you want to win the game without cheating, Kindly remove the print("answer") statement. :)

print("Enter a guess between 1 to 10")
print()
print("You have 5 chances.")
print()

for i in range(5):
    tries += 1
    guess = int(input("Enter your guess : "))
    if guess > answer:
        print("Your guess is too High.")
    elif guess < answer:
        print("Your guess is too Low.")
    elif guess == answer:
        print("Hey! Your Answer is right :)")
        break
    
print("Thank You")
    



