#input validation
#Create a loop for input validation
while True:
    accept = input("Do you accept the terms")
    if accept != "y":
        print("not accepted")
    else:
        print("Thanks for accepting our terms")
        break