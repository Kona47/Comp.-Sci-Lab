########################################################################
##
## CS 101 Lab
## Program #5
## Name: Kona Hudson
## Email: kdhfcx@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


# import statements

# functions
def get_school(card):
    if card[5] == '1':
        return "School of Computing and Engineering SCE"
    elif card[5] == '2':
        return "School of Law"
    elif card[5] == '3':
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'
def get_grade(card):
    if card[6] == '1':
        return "Freshman"
    elif card[6] == '2':
        return "Sophomore"
    elif card[6] == '3':
        return 'Junior'
    elif card[6] == '4':
        return 'Senior'
    else:
        return 'Invalid Grade'
def character_value(char):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alph.find(char)
def get_check_digit(card):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0
    index = 0
    for i in card[0:10]:
        if i in alph:
            total += character_value(i)* (index + 1) 
        elif i == '0':
            total += 0 * (index + 1)
        elif i == '1':
            total += 1 * (index + 1)
        elif i == '2':
            total += 2 * (index + 1)
        elif i == '3':
            total += 3 * (index + 1)
        elif i == '4':
            total += 4 * (index + 1)
        elif i == '5':
            total += 5 * (index + 1)
        elif i == '6':
            total += 6 * (index + 1)
        elif i == '7':
            total += 7 * (index + 1)
        elif i == '8':
            total += 8 * (index + 1)
        elif i == '9':
            total += 9 * (index + 1)
        index += 1
    digit = total % 10
    return digit
def verify_check_digit(card):
    if len(card) != 10:
        return (False, "The length of the number given must be 10")
    if card[0:5].isalpha() == False:
        nam = 0
        for i in card[0:5]:
            if i.isalpha() == False: 
                e1 = i
                break
            nam+=1
        a = f"The first 5 characters must be A-Z, the invalid character is at {nam} is {e1}"  
        return (False, a)
    if card[7:10].isdigit() == False:
        gam = 7
        for i in card[7:10]:
            if i.isdigit() == False: 
                e2 = i
                break
            gam+=1
        b = f"The last 3 characters must be 0-9, the invalid character is at {gam} is {e2}"  
        return (False, b)
    if int(card[5]) != 1 and int(card[5]) != 2 and int(card[5]) != 3:
        return (False, "The sixth character must be 1 2 or 3")
    if int(card[6]) != 1 and int(card[6]) != 2 and int(card[6]) != 3 and int(card[6]) != 4:
        return (False, "The seventh character must be 1 2 3 or 4")
    if int(card[9]) != get_check_digit(card):
        c = f"Check Digit {card[9]} does not match calculated value {get_check_digit(card)}"
        return (False, c)
    if len(card) == 10 and card[0:5].isalpha() == True and card[7:10].isdigit() == True and int(card[5]) in range(1,4) and int(card[6]) in range(1,5) and int(card[9]) == get_check_digit(card):
        g = f'Library card is valid\nThe card belongs to a student in {get_school(card)}\nThe card belongs to a {get_grade(card)}'
        return g

    
    
    
    
if __name__ == "__main__":

    # main program
    print("Main Program")
    card = input('Enter Library Card. Hit Enter to Exit ==> ')
    while card != '':
        print(verify_check_digit(card))
        card = input('Enter Library Card. Hit Enter to Exit ==> ')
