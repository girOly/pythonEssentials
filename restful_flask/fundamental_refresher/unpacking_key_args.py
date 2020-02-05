def key_arg(**kwargs):
    print(kwargs)

key_arg(name="Bob", age=25)

details ={"name": "Bob", "age": 25}

key_arg(**details)

def named(name, age):
    print(name, age)

named(**details)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")



print_nicely(name="Bob", age=25)

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,3,5, name="Bob", age=25)