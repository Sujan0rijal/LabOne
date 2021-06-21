'''If tempereture  is greater than 30,it`s hot day otherwise.If it`s less than 10 then it`s cold
day otherwise it`s neither cold nor hot'''

temperature= int(input('enter the temperature:'))

if temperature>30:
    print(f'it`s hot day')
elif temperature<10:
        print(f'it`s cold day')
else:
    print(f'it`s neither hot nor cold')