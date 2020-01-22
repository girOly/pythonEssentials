email = '''

Hi John,

Here's our first email to you.

Thank you,
Support Team
 '''
print(email)


course = 'Python for Beginners'
#         0123456
another = course[:]


print(course[-2])

# print(course[0:6])
# print(course[2:8])

print(another)


name = 'Yennifer'
print(name[1:-1])

first_name = 'John'
last_name = 'Smith'

message = first_name + ' [' + last_name + '] is a Coder'

print(message)

# f' is the equivalent of `${var}`
formatted_message = f'{first_name} [{last_name}] is a Super Coder'

print(formatted_message)
