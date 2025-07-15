#alot of functions that are related need to group them together to know what they are apart of
# we can use decorators and static methods
#decorator is a function that another function and change it
#decorator is a wrapper for a function that add code to a function

def my_decorator(func):
    def wrapper():
        print("Something added before the function")
        func()
        print("Something after thr function")
    return wrapper
#now static method
#makes class that just consist of functions
class MyMathUtils:
    @staticmethod
    def add (x,y):
        return x+y
    @staticmethod
    def multiply(x,y):
        return x,y
print(MyMathUtils.add(7,5))
print(MyMathUtils.multiply(7,5))
