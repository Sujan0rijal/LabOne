'5. A school decided to replace the desks in three classrooms. Each desk sits two students.'
' Given the number of students in each class, print the smallest possible number of desks that can be purchased.'
'The program should read three integers: the number of students in each of the three classes, a, b and c respectively.'
'In the first test there are three groups. The first group has 20 students and thus needs 10 desks.'
'The second group has 21 students, so they can get by with no fewer than 11 desks.'
'11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.'

no_students_class1= int(input('enter the number of students in class 1:'))
no_students_class2= int(input('enter the number of students in class 2:'))
no_students_class3= int(input('enter the number of students in class 3:'))

desk_class1= no_students_class1 / 2
print(f'the required number of desk for class1 is {desk_class1}')
desk_class2= no_students_class2 / 2
print(f'the required number of desk for class2 is {desk_class2}')
desk_class3= no_students_class3 / 2
print(f'the required number of desk for class3 is {desk_class3}')

remain_class1=no_students_class1 % 2
print(f'the remainning desk for first class is {remain_class1}')
remain_class2=no_students_class2 % 2
print(f'the remainning desk for second class is {remain_class2}')
remain_class3=no_students_class3 % 2
print(f'the remainning desk for third class is {remain_class3}')

total_desk=desk_class1+desk_class2+desk_class3+remain_class1+remain_class2+remain_class3
print(f'the total no of desk required for students is {total_desk}')