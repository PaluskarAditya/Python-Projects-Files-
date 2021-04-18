print("Welcome to Astrolger's Stars")

print("Enter a Number between 1 - 5")
number = int(input())

print("Enter 1 or 0")
boolean = bool(int(input()))

if number == 1 and boolean == True:
    print("*")
elif number == 2 and boolean == True:
    print("""*
**""")
elif number == 3 and boolean == True:
    print("""*
**
***""")
elif number == 4 and boolean == True:
    print("""*
**
***
****""")
elif number == 5 and boolean == True:
    print("""*
**
***
****
*****""")
elif number == 1 and boolean == False:
    print("*")
elif number == 2 and boolean == False:
    print("""**
*""")
elif number == 3 and boolean == False:
    print("""***
**
*""")
elif number == 4 and boolean == False:
    print('''****
***
**
*''')
elif number == 5 and boolean == False:
    print('''*****
****
***
**
*''')

print("Thank You")