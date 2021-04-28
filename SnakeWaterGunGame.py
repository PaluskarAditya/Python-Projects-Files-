import random

# if user chooses snake and computer chooses water as snake drinks his water and user wins

# if user chooses water and computer chooses gun as gun is damaged in water so user wins

# if user chooses gun and compter chooses snake as gun kills snake so user wins
print("Welcome to the Snake, Water and Gun game. Kindly enter your name.")
user_name = input("")

o = 0
i = 0
g = 0


while o != 10:
    
    lst = ["s", "g", "w"]
    ran = random.choice(lst)
    print(ran)
    
    print("Select S for Snake, G for Gun and W for Water")
    answer = input("").lower()
    o += 1
    if answer == "s" and ran == "s":
        print("You chose Snake and Computer chose Snake so its a Tie.")
        print(f"{user_name} has {i} points and Computer has {g} points")
    elif answer == "s" and ran == "w":
        print("User wins as his Snake drinks all the Water of Computer.")
        print("You chose Snake and COmputer chose Water")
        i += 1
        print(f"{user_name} has {i} points and Computer has {g} points")
    elif answer == "s" and ran == "g":
        print("Computer wins as his Gun kills User's Snake.")
        print("You chose Snake and Computer chose Gun.")
        g += 1
        print(f"{user_name} has {i} points and Computer has {g} points")
    elif answer == "w" and ran == "w":
        print("You chose Water and Computer chose Water so its a Tie.")
        print(f"{user_name} has {i} points and Computer has {g} points")
    elif answer == "w" and ran == "s":
        print("Computer wins as his Snake drinks all the Water of User.")
        print("You chose Water and Computer chose Snake.")
        g += 1
        print(f"{user_name} has {i} points and Computer has {g} points")
    elif answer == "w" and ran == "g":
        print("User wins as his Water damages Computer's Gun.")
        print("You chose Water and Computer chose Gun.")
        i += 1
        print(f"{user_name} has {i} points and Computer has {g} points")
    elif answer == "g" and ran == "g":
        print("You chose Gun and Computer chose Gun so its a Tie.")
        print(f"{user_name} has {i} points and Computer has {g} points")
    elif answer == "g" and ran == "w":
        print("Computer wins as his Water damages User's Gun.")
        print("You chose Gun and Computer chose Water.")
        g += 1
        print(f"{user_name} has {i} points and Computer has {g} points")
    elif answer == "g" and ran == "s":
        print("User wins as his Gun kills Computer's Snake.")
        print("You hcose gun and Computer chose Snake.")
        i += 1
        print(f"{user_name} has {i} points and Computer has {g} points")
      
if i>g:
    print(f"{user_name} wins against Computer by {i} Wins.")
elif i==g:
    print(f"Its a Tie as {user_name} has {i} wins and Computer has {g} Wins.")
else:
    print(f"Computer wins against {user_name} by {g} Wins.")
