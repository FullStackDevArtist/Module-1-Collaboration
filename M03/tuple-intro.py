#tuples are similar to list but thet are immuteable
#list are constant
#tuples are faster than list
#values that should not changed or modify
#good for saftey features because they shouldnt change
# to change tuple you have to make a new tuple with added new info
#Immutability = cannot be changed
#string are immutable you cannot change the individual letter but you can change the entire string
name = "tim"
name - "zach"
name[0] = " j" #cannot replace the letter must change the string
print(name)

#Create another tuple from two other tuples
states = ("IL", "IN","KY")
states2 =("FL", "NY", "NJ")
states3 = states + states2
print(states3)
#use a tuple if you know that the data structure will not be changed