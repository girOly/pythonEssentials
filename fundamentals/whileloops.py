# while condition:
# ... Repeat execution
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
# print("Done")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess the Secret Number: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('You lose!')
