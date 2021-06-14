'10. Write a Python program to convert seconds to day, hour, minutes and seconds.'

second = float(input('enter the secconds:'))
print(f'the total seconds is {second}')

minutes = second/60
print(f'the total minutes is {minutes}')

hours = minutes/60
print(f'the total hours is {hours}')

day = hours/24
print(f'the total day is {day}')