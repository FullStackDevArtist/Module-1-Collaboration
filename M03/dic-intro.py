#dictionaries create key value pairs that associate name(key) wiith a value
#python treats dic like maps or objects
#objects are containers that have properties that describe a object or item apart of item
#Person- name, age
#car- make, model, year
#syhntax for dictionary dictname = {"key_name":value,}
#bank customers and there balances
bank_customers = {
    #keys ar always going to be a string
    "Alice" : 100.00,
    "Tim": 500.00,
    "Sam": 850.00
}

for key in bank_customers:
    print(key, bank_customers[key])
#to display things in dic we access them by their keys

#dict are mutable
#add new key with new value
bank_customers["Zach"] = 400.00
print(bank_customers)

#to grab a single value for dict use .get()function
alice_balance = bank_customers.get("Alice")
print(alice_balance)

#to delete is del and key name
del bank_customers["Alice"]
print(bank_customers)

#to search we use the in keyword
key = "Tim"
if key in bank_customers:
    print(key,"is int the dict")
else:
    print(key," is not in dict")

#detailed search key name value match seatch terms
find_name = "Tim"
value = 500.00
#.item() function allows to search things in keys AND values
for name, balance in bank_customers.items():
    if name == find_name and balance == value:
        print("Found Tim and his balance match")
        

