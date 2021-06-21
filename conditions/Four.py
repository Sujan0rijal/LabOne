''''Task----------condition-------weight converter
  Input the weight of a person is either kg or lbs. If the person provides his/her
  weight in kg then convert it into lbs 
  else convert it to kg'''

weight=int(input('enter the weight of a person:'))
unit = input('enter (L)bs OR (K):')

kg= int(weight*2.2)
lbs=int(weight*0.45)
if unit == 'L' or 'l':
    print(f'you are {lbs} kilogram')
elif unit == 'K' or 'k':
    print(f'you are {kg} pounds')
else:
    print(f'the converter is only for kg or lbs')