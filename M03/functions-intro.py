#we use functions like print() and input()
#to create your own you create a template for it
#called defined function in python
# void function in python there is no return value
# example of void function
def my_function():
    x= 5
    y= 6
    total = x+y
    print(total)
# we have just defined the function
#this will just run the fuction
#good because they are repeatable

#parameters are passed as data to a function
#variable are placeholders for incoming data
#parameters are just a arguments waiting to be used
#arguments is used when we are running a function 
#parameters are the placeholders when defining a function
#def my_fuction - name is a parameter
#print(name) name is argument
def display_number(number):
    print(number) 

#when calling the function the argument or variable name does not have to be the same 
my_number = 50
display_number(my_number)