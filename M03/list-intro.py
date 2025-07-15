#list are dynamic in size
#python simpest data straucture is a list
#list can contain multiple types of data ( dont mix data types)
#data structures contain more than one piece of data
#list can be changed (deleted, or added)

#create a list with some data values for test scores
test_scores = [100,99,77,55]
#index is the order or position of a item in the list
print(test_scores[0])
print(test_scores[1])
#display the data is a for loop
#for loop allows each item in the list to do the following thing to it
#syntax for iteratorname in listname

for item in test_score:
    print(item)


#modify a list
for test_score in test_scores:
    test_score = test_score + 5 
    print(test_scores)

    #add thing to a list
    test_scores.append(82)
    #append adds things to a list
    #when adding these changes they are not save to the orginal list
    #easiest way is to make a new list and save those changes in that list

    new_list = []
    for test_score in test_scores:
        test_score = test_score + 5
        new_list.append(test_score)
        print(new_list)
        
#combine list together 
#extended function combines one list to another
test_score2 = [95,44,76]
test_scores.extend(test_score2)
print(test_scores)

#remove instance
test_scores.remove(100)
print(test_scores)

#searching through a list
looking_for = 95
found = looking_for in test_scores
print(found)
