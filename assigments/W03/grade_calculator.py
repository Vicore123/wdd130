####### Core Requirements ########

grade_percentage = int(input('Please type your grade percentage '))

if grade_percentage >= 90:
    letter = 'A'
elif grade_percentage >= 80:
    letter = 'B'
elif grade_percentage >= 70:
    letter = 'C'
elif grade_percentage >= 60:
    letter = 'D'
else:
    letter = 'F'


######## Stretch Assignment #########

sign = ''
last_digit = grade_percentage % 10

if grade_percentage < 97 and grade_percentage > 60:
    if last_digit >= 7:
        sign = '+'
    elif last_digit < 3:
        sign = '-'
    else:
        sign = ''
else: 
    sign = ''

print(f'\nYour grade is: {letter}{sign}')
if grade_percentage >= 70:
    print('congratulations! You passed the course\n')
else:
    print('I am sorry, you did not pass the course, try again next time\n')