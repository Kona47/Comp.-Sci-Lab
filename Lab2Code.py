#This code is used as a grade calculator for students in the Computer Science Lab class.
#This first section of code greets the user and asks for their name.
print('**** Welcome to the LAB grade calculator! ****\n')
name = input('Who are we calculating grades for? ==> ')
#This section of code asks the users for 3 inputs. Their grade in the labs, exams, and attendance categories.
#The if statements here ensure they are entering valid grade values, and changes them if they are invalid.
labs_grade = int(input('\nEnter the Labs grade? ==> '))
if labs_grade > 100:
    print('The lab value should have been 100 or less. It has been changed to 100.')
    labs_grade = 100
if labs_grade < 0:
    print('The lab value should have been zero or greater. It has been changed to 0.')
    labs_grade = 0
exams_grade = int(input('\nEnter the EXAMS grade? ==> '))
if exams_grade > 100:
    print('The exam value should have been 100 or less. It has been changed to 100.')
    exams_grade = 100
if exams_grade < 0:
    print('The exam value should have been zero or greater. It has been changed to 0.')
    exams_grade = 0
attendance_grade = int(input('\nEnter the Attendance grade? ==> '))
if attendance_grade > 100:
    print('The attendance value should have been 100 or less. It has been changed to 100.')
    attendance_grade = 100
if attendance_grade < 0:
    print('The attendance value should have been zero or greater. It has been changed to 0.')
    attendance_grade = 0
#This next section of code calculates their final grade by adding the 3 values multiplied by their weight
#the labs is 70% of the final grade, the exams are 20%, and attendance is 10%
finalGrade = (labs_grade * .7) + (exams_grade * .2) + (attendance_grade * .1)
print(f'\nThe weighted grade for {name} is {finalGrade}')
#This section of if statements is setting the value of the letter grade based on the score of the usersd final grade.

if 90 <= finalGrade <= 100:
    letterGrade = 'A'
elif 80 <= finalGrade < 90:
    letterGrade = 'B'
elif 70 <= finalGrade < 80:
    letterGrade = 'C'
elif 60 <= finalGrade < 70:
    letterGrade = 'D'
else:
    letterGrade = 'F'
#After the value of the letter grade is set, the next statement prints it to the user.
print(f'{name} has a letter grade of {letterGrade}')
print('\n**** Thanks for using the Lab grade calculator ****')

    
