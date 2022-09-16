#this section introduces the game and asks the user for their number
print('Welcome to the Flarsheim Guesser!\n')
print('Please think of a number between and including 1 and 100.\n')
#below, the user inputs the value when their number is divided by 3
# this number is then tested in the if statement to make sure it is a valid input, if it isn't, it asks for a new input.
rem3 = int(input('What is the remainder when your number is divided by 3? '))
while rem3 < 0 or rem3 > 2:
    if rem3 > 2:
        print('The value must be less than 3')
        rem3 = int(input('What is the remainder when your number is divided by 3? '))
    elif rem3 < 0:
        print('The value entered must be 0 or greater')
        rem3 = int(input('What is the remainder when your number is divided by 3? '))
print()
#Now it asks for the inputs when their number is divided by 5 and divided by 7 nd makes sure the values are valid.
rem5 = int(input('What is the remainder when your number is divided by 5? '))
while rem5 < 0 or rem5 > 4:
    if rem5 > 4:
        print('The value must be less than 5')
        rem5 = int(input('What is the remainder when your number is divided by 5? '))
    elif rem5 < 0:
        print('The value entered must be 0 or greater')
        rem5 = int(input('What is the remainder when your number is divided by 5? '))
print()
rem7 = int(input('What is the remainder when your number is divided by 7? '))
while rem7 < 0 or rem7 > 6:
    if rem7 > 6:
        print('The value must be less than 7')
        rem7 = int(input('What is the remainder when your number is divided by 7? '))
    elif rem7 < 0:
        print('The value entered must be 0 or greater')
        rem7 = int(input('What is the remainder when your number is divided by 7? '))
'''this for statement goes through all the values between 1 and 100
it then finds the remainder when i is divided by 3, 5, and 7, and
checks if these values are equal to the ones the user inputed. If so,
it inputs that value, which is the value the user was thinking of
'''
for i in range(1, 101):
    if (i % 3) == rem3 and (i % 5) == rem5 and (i % 7) == rem7:
        print(f'Your number was {i}\n')
        print('How amazing is that?\n')
        break
'''Now the game asks if they would like to play again, and if y or Y is inserted,
the game replays in the while loop below. The first while statement is to make sure
the users input is valid, and asks the user if they want to play again if a weird character is inserted'''

play = input('Do you want to play again? Y to continue, N to quit ==> ')
while play != 'N' and play != 'n' and play != 'y' and play != 'Y':
   play = input('Do you want to play again? Y to continue, N to quit ==> ') 
while play == 'Y' or play == 'y':
    print('\nPlease think of a number between and including 1 and 100.\n')
    rem3 = int(input('What is the remainder when your number is divided by 3? '))
    while rem3 < 0 or rem3 > 2:
        if rem3 > 2:
            print('The value must be less than 3')
            rem3 = int(input('What is the remainder when your number is divided by 3? '))
        elif rem3 < 0:
            print('The value entered must be 0 or greater')
            rem3 = int(input('What is the remainder when your number is divided by 3? '))
    print()
    rem5 = int(input('What is the remainder when your number is divided by 5? '))
    while rem5 < 0 or rem5 > 4:
        if rem5 > 4:
            print('The value must be less than 5')
            rem5 = int(input('What is the remainder when your number is divided by 5? '))
        elif rem5 < 0:
            print('The value entered must be 0 or greater')
            rem5 = int(input('What is the remainder when your number is divided by 5? '))
    print()
    rem7 = int(input('What is the remainder when your number is divided by 7? '))
    while rem7 < 0 or rem7 > 6:
        if rem7 > 6:
            print('The value must be less than 7')
            rem7 = int(input('What is the remainder when your number is divided by 7? '))
        elif rem7 < 0:
            print('The value entered must be 0 or greater')
            rem7 = int(input('What is the remainder when your number is divided by 7? '))
    for i in range(1, 101):
        if (i % 3) == rem3 and (i % 5) == rem5 and (i % 7) == rem7:
            print(f'Your number was {i}\n')
            print('How amazing is that?\n')
            break
    #Once 'n' or 'N' is submitted, the game ends, but if 'y' or 'Y' is submitted again, the game replays.
    play = input('Do you want to play again? Y to continue, N to quit ==> ')
    while play != 'N' and play != 'n' and play != 'y' and play != 'Y':
        play = input('Do you want to play again? Y to continue, N to quit ==> ')
    



    
