'''4. Given three integers, print the smallest one. (Three integers should be user input)'''

integer1=int(input('enter first number:'))
integer2=int(input('enter second number:'))
integer3=int(input('enter third number:'))

if integer1<integer3 and integer1<integer2:
    print(f'smallest number is {integer1}')
elif integer2<integer3 and integer2<integer1:
    print(f'smallest number is {integer2}')
else:
    print(f'smallest number is {integer3}')