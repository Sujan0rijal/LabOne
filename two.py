'6. Solve each of the following problems using Python Scripts. Make sure you use appropriate variable names and comments.'
'When there is a final answer have Python print it to the screen.'
'A person’s body mass index (BMI) is defined as:'
'BMI=mass in kg / (height in m)2.'

mass_man=float(input('enter the mass of man:'))
height_man=float(input('enter the height of man:'))

BMI= mass_man / ( height_man*height_man)
print(f'A person`s body mass index (BMI) is {BMI}')