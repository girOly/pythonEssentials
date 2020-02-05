def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1,2,3,5,6))

nums = [1,2,3,5,6,7]

print(multiply(*nums))

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1,2,3,4,5,6,7,operator="+"))

print(apply(1,2,3,4,5,6,7,operator="*"))