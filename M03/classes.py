#classes is a blueprint for an object contains data (attributes/field/properties) and function (methods)
#methods and functions are the same but the methods need a object
#object represent real world thing/object
#classes help group objects with the same or like behavior
# to use a class needs to be defines as a person
class Person:
    name="zach"
    age=39

#class are like the master copy that can be replicated
instance1 = Person() #create a instance
#to access the attributes we use .dot notation
print(instance1.name)
print(instance1.age)

#make multiple copies
instance2 = Person()
print(instance2.name)
#mod instances after created
instance2.name="Time"
instance2.age=43

print(instance2.name)
print(instance2.age)
