# accumulator: to keep us with running values
#average number are good example

total_sum = 0
average = 0 
how_many_numbers = int(input("How many num do you wish to average"))
for i in range (0,how_many_numbers,1):
    value = float(input("Give the value"))
    total_sum = total_sum + value

print("Your total sum is", total_sum)
average = total_sum / how_many_numbers
print("Your average is", average)