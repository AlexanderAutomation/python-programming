# Guessing game
'''
-get a random number between 1 and 10
-prompt the user for to guess the number
-loop while the user guess is not equal to your number
 if the users guess is less than the numbers print "too small"
 if the users guess is greater than the number print "too big"

 - print " you are cotrect when the user gets the number right"
'''
#sudo code
'''
Open Loop
get random number >= 1 and random number <=10
input guess
if guess < number:
    print ('too small')
else:
    print ('too big')
elif guess = number:
        print('you are cotrect when the user gets the number right')
close loop

'''

#variables
guess_number = 0
number = 0
import random



#code
while True:
    #number = random.randint(1,10)
    guess_number = int(input('guess number: '))
    if (guess_number) < number:
        print ('too small')
    elif:
        print ('too big')
    else guess_number == number:
            print('you are cotrect')
            break












