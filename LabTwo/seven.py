'''7. Given a positive real number, print its fractional part.'''

def factorial(num):
    '''
    sujan rijal
    :param num: integer
    :return: integer
    '''
    fact=1
    for i in range(2,num+1):
        fact=fact*i
    return fact
print(factorial.__doc__)

print(factorial(5))