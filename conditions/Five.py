'game finding a secret number within 3 attempts using while loop'

import random
random_num=random.randint(1,10)
guess=int(input('enter your guess:'))
i=1
while i<=3:
    if random_num ==guess:
        print('you have guess it')
        break
    else:
        guess = int(input('guess again'))
    i=i+1
else:
    print('limit is crosss')