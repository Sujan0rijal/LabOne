'''2. WAP which accepts marks of four subjects and display total marks, percentage and grade.
 Hint: more than 70% –> distinction,
 more than 60% –> first, more than 40% –> pass, less than 40% –> fail'''

subject1=float(input('enter the marks of subject1:'))
subject2=float(input('enter the marks of subject2:'))
subject3=float(input('enter the marks of subject3:'))
subject4=float(input('enter the marks of subject4:'))

total_marks= subject1+subject2+subject3+subject4
percentage=total_marks/4
print(f'you have got {percentage}%')

if percentage>=70:
    print('you have got distinction')
elif 70>percentage>=60:
    print('you have got first division')
elif 60>percentage>=40:
    print('you have got pass')
else:
    print('you have got fail')