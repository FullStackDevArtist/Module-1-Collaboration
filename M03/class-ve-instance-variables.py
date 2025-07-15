#blank value until we create the value use instance
#instance variables can be set upon
#class represent real world objects but data is ususally different inside
class Dog:
    #class variable
    animal= "Dog"
instance1 = Dog("fido", 2)
print(instance1.name)
print(instance1.age)
print(instance1.animal)

#create 2nd instance with different data
instance2 = Dog ("Braxton", 9)
print(instance2.name)
print(instance2.age)
print(instance2.animal)
#change data inside
instance2.age=10
print(instance2.age)

#usefull for user input effect name and age
dog_name = input("Whats your dogs name")
dog_age = int(input("What is your dogs age"))