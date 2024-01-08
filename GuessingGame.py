which_one = input('Guess Number From 1 to 50?: Press Enter')
secret_number = 9
guess_count = 0
guess_limt = 3
while guess_count < guess_limt:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry you lost! The right guess was 45.')
