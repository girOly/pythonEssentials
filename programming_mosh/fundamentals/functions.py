def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome aboard! \n')


print("Start")
greet_user('John', 'Smith')
greet_user(last_name='Leonard', first_name='Michel')
print("Finish")


def square(number):
    return number * number


print(square(3))
