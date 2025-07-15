#06/18 Wedn Sess
#last time class was conditionals
#Today we are talking about loop
# they are control structure the repeat block of code when conditional is met. 
# a for loop is count-controlled loop a certain number of times

#flag
keep_going = "y"
#make a commission program to check sells and commission for an employee..
#while syntax
while(keep_going) =="y":
    sales = float (input("please give sales for the month"))
    com_rate = float(input(" What is your commission rate in decemial form"))
    total_earned = sales * com_rate
    print("you have earned", total_earned)