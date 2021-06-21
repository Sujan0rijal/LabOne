'''if name is less than 3 character long- name must be at least 3 characters
otherwise if it`s more than 50 characters- name must be maximun of 50 characters
otherwise- name looks good !'''

name_characters= int(input('enter the characters :'))
if name_characters<3:
    print(f'name must be at least 3 characyers')
elif name_characters>50:
    print(f'name must be maximum of 50 characters')
else:
    print(f'name looks good')