def getdate():
    import datetime
    return datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")

def user_input():
    a = []
    print("Enter 1 for Lock and 2 for Retrieve.")
    option = int(input(""))

    
    if option == 1:
        print("Enter 1 for Harry 2 for Hammad and 3 For Rohan.")
        option1 = int(input(""))

        
        if option1 == 1:
            print("Enter 1 for Exercise and 2 for Diet.")
            option2 = int(input(""))
            if option2 == 1:
                print("Type your Exercise.")
                user_ex = input("")
                with open ("harry-ex.txt", "a") as a:
                    a.write (getdate()+' :- '+str(user_ex))
                    a.write("\n")
                    print("Successfully Written.")
            if option2 == 2:
                print("Type your Diet.")
                user_diet = input("")
                with open ("harry-diet.txt", "a") as a:
                    a.write (getdate()+' :- '+str(user_diet))
                    a.write("\n")
                    print("Successfully Written.")


        if option1 == 2:
            print("Enter 1 for Exercise and 2 for Diet.")
            option2 = int(input(""))
            if option2 == 1:
                print("Type your Exercise.")
                user_ex = input("")
                with open ("hammad-ex.txt", "a") as a:
                    a.write (getdate()+' :- '+str(user_ex))
                    a.write("\n")
                    print("Successfully Written.")
            if option2 == 2:
                print("Type your Diet.")
                user_diet = input("")
                with open ("hammad-diet.txt", "a") as a:
                    a.write (getdate()+' :- '+str(user_diet))
                    a.write("\n")
                    print("Successfully Written.")


        if option1 == 3:
            print("Enter 1 for Exercise and 2 for Diet.")
            option2 = int(input(""))
            if option2 == 1:
                print("Type your Exercise.")
                user_ex = input("")
                with open ("rohan-ex.txt", "a") as a:
                    a.write (getdate()+' :- '+str(user_ex))
                    a.write("\n")
                    print("Successfully Written.")
            if option2 == 2:
                print("Type your Diet.")
                user_diet = input("")
                with open ("rohan-diet.txt", "a") as a:
                    a.write (getdate()+' :- '+str(user_diet))
                    a.write("\n")
                    print("Successfully Written.")
    
    
    if option == 2:
        print("Enter 1 for Harry 2 for Hammad and 3 For Rohan.")
        opt_name = int(input(""))
        

        if opt_name == 1:
            print("Enter 1 for Exercise and 2 for Diet.")
            user_ans = int(input(""))
            if user_ans == 1:
                f = open ("harry-ex.txt")
                content = f.read()
                print(content)
                f.close()
            if user_ans == 2:
                f = open ("harry-diet.txt")
                content = f.read()
                print(content)
                f.close()


        if opt_name == 2:
            print("Enter 1 for Exercise and 2 for Diet.")
            user_ans = int(input(""))
            if user_ans == 1:
                f = open ("hammad-ex.txt")
                content = f.read()
                print(content)
                f.close()
            if user_ans == 2:
                f = open ("hammad-diet.txt")
                content = f.read()
                print(content)
                f.close()

        
        if opt_name == 3:
            print("Enter 1 for Exercise and 2 for Diet.")
            user_ans = int(input(""))
            if user_ans == 1:
                f = open ("rohan-ex.txt")
                content = f.read()
                print(content)
                f.close()
            if user_ans == 2:
                f = open ("rohan-diet.txt")
                content = f.read()
                print(content)
                f.close()

    


user_input()