def user_age_in_seconds():
    user_age = int(input("Enter your age:"))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age ins econds is {age_seconds}.")


friends = ["Oly", "Jimmy"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    new_friends = friends + [friend_name]
    return new_friends


def add(x,y):
    result = x + y
    return result

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You can't divide by zero!")

def default_value_add(x=1,y=5):
    result = x + y
    return result

