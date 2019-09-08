#print hello world
'''
name = 'world'
print('Hello')
print (name)
print('Hello'+' '+name)
'''
#conditinals

'''
n = 10
a = 60
if n > 24:
 print('loser')
else:
 print ('not a loser')
 '''
 #Calculations and ocnditinals
'''
n = 6
T = 5
F = 2

if n >= 10:
 print(T - F)
else:
 print(T / n) 
 '''
#Practice conditionals 
#Task 
#Given an integer, n, perform the following conditional actions:
#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird

'''
n = 50

if n % 2 > 0:
    print('weird')
if n % 2 == 0 and n >= 2 and n <=5:
    print('not weird')
if n % 2 == 0 and n >= 6 and n <=20:
    print('not weird')
if n % 2 == 0 and n > 20:
    print('not weird')
'''

#shorter code:
'''
if n % 2 > 0 or (n % 2 == 0 and n >= 2 and n <=5):
    print('weird')
'''

#Arithmetic
#Read two integers from STDIN and print three lines where:

#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.
'''
a = 10
b = 100

print(a+b)
print(a-b)
print(a*b)
print(a/b)
'''
# Integrer and Floating divisions
'''
a = 4
b = 3

print(a//b)
print(a/b)
'''
#List
'''
digits = ['4.5','5.6','8.9','10.9','100']
print(digits)
print(len(digits))
print(digits[0])
'''
#functions

'''
digits = ['4.5','5.6','8.9','10.9','100']
def hello():
    print(digits)
hello()
hello()
hello()
hello()
'''
#loops
'''
nums = [1,2,3,4,5,6,7,8,4,5,6,7,8,4,4,7]
for num in nums:
    if num == 4:
       print('Yai!')
    elif num == 6:
        print('No way')
    else:
        print('ok')
'''
# Pig Game

#Variables
'''
turn = 1
player_one_score_total = 0
player_two_score_total = 0
max_score = 20
import random
score = 0

#code

while True:
    choice = input('enter choice: ')
    if choice == 'r':
        score = random.randint(1,6)
    if score != 1:
        if turn == 1:
            player_one_score_total += score
        else:
            player_two_score_total += score
    else:
        if turn == 1:
            player_one_score_total = 0
            turn = 2
            print('Turn 2')
        else:
            player_two_score_total = 0
            turn = 1
            print('Turn 1')
    if player_one_score_total >= max_score or player_two_score_total >= max_score:
        if player_one_score_total > max_score:
            print(f'Player 1 is the winner!!  Score = {player_one_score_total}')
        else:
            print(f'Player 2 is the winner!!  Score = {player_two_score_total}')
        break
    '''
montreal = {'lattitude':'45.50884','longitude':'73.58781','size':'590.76','population':'3,519,595'}
toronto = {'lattitude':'43.70011','longitude':'-79.4163','size':'630.21','population':'5,429,524'}
vancouver = {'lattitude':'49.24966','longitude':'-123.11934','size':'625.66','population':'2,264,823'}
ottawa = {'lattitude':'45.41117','longitude':'75.69812','size':'2,778','population':'989,657'}
calgary = {'lattitude':'51.05011','longitude':'-114.08529','size':'825.29','population':'1,237,656'}

#printing dictionaries
'''
city = 0
city2 = 0

city = input("Please add your city:" )
if city == 'montreal':
    print('The lattitude for montreal is :', montreal['lattitude'])
    city2 = input('Please add your second city: ')
    if city2 == 'toronto':
        print('The lattitude for montreal is :', toronto['lattitude'])
'''
# If statements with even and odd numbers
'''n = 24
if n % 2 > 0:
    print('Weird')
if n % 2 == 0 and n >= 2 and n <= 5:
    print('Not Weird')
if n % 2 == 0 and n >= 6 and n <= 20:
    print('Weird')
if n % 2 == 0 and n > 20:
    print('Not Weird')
'''
# If Statements with Even Odd and Multiples

'''Ask the user for a number. Depending on whether the number 
is even or odd, print out an appropriate message to the user
If the number is a multiple of 4, print out a different message..'''

'''
num = input('Add your number here: ') 
if int(num) % 2 == 0:
    print('number is odd')
else:
    print('number is even')
if int(num) % 4 == 0:
    print('this number is multiple of 4')

Ask the user for two numbers: one 
number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.
'''

'''
num = 0
check = 0
while True:
    num = input('add number: ')
    check = input ('add second number: ')
    if int(num) % int(check) != 0:
        print('this numbers are not divisible')
    else:
        print('This numbers are divisible')
        break
    '''
# List less than ten

'''Take a list, say for example this one

total_a = 0
aa = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements 
of the list that are less than 5.

for a in aa:
    if a < 5:
        print(a)
'''
'''
for a in aa:
    if a < 5:
        total_a += a
        print(total_a)
'''
'''
for a in aa:
    total_a += a
    print(total_a)
'''

#Append in list
'''
aa.append(90)
aa.append(40)
aa.append(70)
aa.append(90)
aa.append(60)
print(aa)
aa.remove(2)
print(aa)
aa.pop()
aa.insert(2,288)
print(aa)
'''
# List less than tens
'''Ask the user for a number and return a list that contains only 
elements from the original list a that are smaller than that 
number given by the user'''

'''aa = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
input_a = 0

input_a = input('submit your number:')
for a in aa:
    if a < int(input_a):
        print(a)
'''
# Character input

'''Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that 
they will turn 100 years old.'''

'''
name = 0
age = 0
year = 0
name = input('What is your name?: ')
age = input('what is your age: ')
year = (100 - int(age)) + 2019
print(year)
'''
#Divisors
'''Create a program that asks the user 
for a number and then prints out a list of all the 
divisors of that number. (If you don’t know what a divisor is, 
it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

#sudocode

'''input variable number
if x % variable == 0:
    insert x in the list.
use variable number to print list'''

'''
num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)

'''
#listOverlap

'''
alist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
blist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = []

write a program that returns a list that contains only the 
elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

#sudocode

read two lists
return values that are common in the two list just once

for a in alist:
    if a in blist:
        if a not in x:
            x.append(a)

print(x)

'''











