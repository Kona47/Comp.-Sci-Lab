########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
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
import math
import random
def play_again() -> bool:
    play = input('Do you want to play again? ==> ')
    while play != 'Y' or 'YES' or 'N' or 'NO' or 'nO' or 'y' or 'n' or 'Yes' or 'yES' or 'YEs' or 'YeS':
        return '\nYou must enter Y/YES/N/NO to continue. Please try again'
        play = input('Do you want to play again? ==> ')
    if play == 'N' or 'NO' or 'No' or 'nO' or 'n':
        return False
    elif play == 'Y' or 'YES' or 'YeS' or 'yes' or 'Yes' or 'yES' or 'yeS' or 'y' or 'YEs':
        return True
    '''Asks the user if they wish to play again'''
   
def get_wager(bank : int) -> int:
    wager = int(input('How many chips do you want to wager? ==> '))
    while wager <= 0 or wager > bank:
        if wager <= 0:
            print('The wager amount must be greater than 0. Please enter again.')
            wager = int(input('How many chips do you want to wager? ==> '))
        elif wager > bank:
            print(f'The wager amount cannot be greater than how much you have. {bank}')
            wager = int(input('How many chips do you want to wager? ==> '))
    if 0 < wager <= bank:       
        return wager
    bank = bank - wager
    '''Asks the user howe much they wish to wager and checks to make sure
    the value is above zero, but smaller than their aamount of chips'''
def get_slot_results() -> tuple:
    reela = random.randint(1,10)
    reelb = random.randint(1,10)
    reelc = random.randint(1,10)
    slot = (reela, reelb, reelc)
    return reela, reelb, reelc
''' Returns the result of the slot pull '''
def get_matches(reela, reelb, reelc) -> int:
    if reela == reelb and reelb == reelc:
        matches = 3
        return 3
    elif reela != reelb and reela != reelc and reelb != reelc:
        matches = 0
        return 0
    else:
        matches = 2
        return 2
    '''determines the amount of matches the spin had'''
def get_bank() -> int:
    bank = int(input('How many chips do you want to start with? ==> '))
    while bank <= 0 or bank > 100:
        if bank <= 0:
            print('Too low a value, you can only choose 1 - 100 chips')    
        elif bank > 100:
            print('Too high a value, you can only choose 1 - 100 chips')
        bank = int(input('How many chips do you want to start with? ==> '))
    if 0 < bank <= 100:
        return bank
''' Returns how many chips the user wants to play with.  Loops until a value 
greater than 0 and less than 101 '''
def get_payout(wager, matches):
    if matches == 3:
        return wager * 10 - wager
    elif matches == 2:
        return wager * 3 - wager
    elif matches == 0:
        return wager * -1
''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times 
the wager if 2 match, and negative wager if 0 match '''
if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while True:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
