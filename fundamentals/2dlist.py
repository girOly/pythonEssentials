# [
#
#     123
#     456
#     789
# ]
# 3x3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item)


numbers = [5, 2, 1, 7, 4]

numbers.insert(0, 10)

print(numbers)
print(numbers.index(7))

numbers1 = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers1:
    if number not in uniques:
        uniques.append(number)
print(uniques)
