guess = 0
tries = 0
while guess != 6 and tries < 5:
    guess = int(input('Guess The Number: '))
    tries += 1

if guess != 6 and tries == 5:
    print('You ran out of tries!')
else:
    print('You got it after ' + str(tries) + ' times!')