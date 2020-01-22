# Name : John Smith
# Email: john@gmail.com
# Phone: 123:1454

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

customer["name"] = "Jack Smith"
print(customer.get('birthday', "Jan 1 1980"))
print(customer["name"])

customer["birthday"] = 'January 1st'

phone = input("Phone: ")

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eigth",
    "9": "Nine"
}
output = ""
for char in phone:
    output += digits_mapping.get(char, "!") + " "

print(output)
