# for item in range(0, 19, 2):
#     print(item)
#
# prices = [10, 20, 30]
# total_cost = 0
# for item in prices:
#     total_cost += int(item)
#
# print("Total: " + str(total_cost))
#
# for x in range(4):
#     for y in range(3):
#         print(str(x) + ' ' + ' ' + str(y))

numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print("x" * number)

for number2 in numbers:
    output = ''
    for count in range(number2):
        output += 'x'
    print(output)

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']

print(names[0:4])

numbers = [3, 6, 8, 2, 10]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)
