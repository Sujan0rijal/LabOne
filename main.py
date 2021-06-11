' 4. Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock? '

N = int(input('enter the minutes passed since midnight:'))
hours = (N/60)
minutes = (N%60)

print(f'the hours is {hours}')
print(f'the minutes is {minutes}')
print(f'its {hours}:{minutes} now')