#we can also use fuction to manipulate data structures like list tuples
groceries = ["bananas", "apples", "milk"]
numbers = [6,22,12]
#create a shortcut to print list 
def print_list (alist):
    for item in alist:
        print(item)

print_list(groceries)

# use function to grab list and mod values from list
#good when we need a function that we dont know the data exactly
#but we know what we want to do with it
def subtract_list(alist, value):
    for item in alist:
        item = item - value
        print(item)

subtract_list (numbers,4)