#Name: MaKayla Harrison
#Date: 6/23/25
#File Name: M02Lab
#Ass: App that lets students know if they have made the Dean list or Honor Roll via GPA

#ask for and accept a student's last name.
#quit processing student records if the last name entered is 'ZZZ'.
#ask for and accept a student's first name.
#ask for and accept the student's GPA as a float.
#test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
#test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.


#Variables
lastname = ""
firstname = ""
GPA = 0.0 

#inputs for names and GPA
while True:
    lastname = input("Enter your Lastname")
    if lastname == "ZZZ":
            break
    firstname = input("Enter first name")
    GPA = float(input("Enter your GPA"))

    #Check GPA
    if GPA >= 3.5:
        print (firstname , lastname, "Congrats you have made the Dean List")
    elif GPA >= 3.25:
        print(firstname, lastname, "Congrats you have made the Honor Roll")
    else: print(firstname, lastname,"Unfortunatly you have not made Honor Roll")
