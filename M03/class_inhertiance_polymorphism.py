#inheritance based polymorphism
#inherit a class and override it methoda
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        #default behavior
    def move(self):
        print("Move")
    
    class Car(Vehicle):
        def move(self):
            print("VROOM")

    class Plane(Vehicle):
        def move(self):
            print("FLY")
    car1 = Car ("ford", )
    
