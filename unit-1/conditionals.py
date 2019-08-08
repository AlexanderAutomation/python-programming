'''
num = 7

if num > 5:
    print('too high')
elif num < 3:
    print ('too low')
else:
    print('just right')
'''

#print corrresponting letters for grades
# 80 - 100, print 'A'
# 79 - 60, print 'B'
# 50 - 50, print 'C'
# 0 - 49, print 'F'
'''
grade = 55

if grade  < 80:
  print ('A')
elif grade >= 60:
  print ('B')
elif grade >= 50:
  print('C')
else:
  print ('F')
'''
#fizzbuzz

#for the firts 50 integers
#if its a multiple of 3, print 'fizz'
#if its a multiple of 5, print 'buzz'
#if its a multiple of 15, print 'fizzbuz'
#otherwise, just print the number
'''
for num in range (1,51):

 if num % 15 == 0:
    print('fizzbuzz')
 elif num % 5 == 0:
    print('fizz')
 elif num % 3 == 0:
    print('buzz')

 else:
    print (num)
'''
'''
name = 'fizzbuzz'

if name.length > 4:
    print('longer than 4')

if name.length > 6:
    print('longer than 6')
'''
'''
#usign 'and' and 'or' in conditionals
num = 15

#display a message if number is odd and also less than 20
if num % 2 == 1 and num < 20:
    print('odd number less than 20')
else:
    print('something else')

  '''
'''
num = 10

print(num)
'''
#group print statements together
num = 24
if num % 2 == 1 or (num % 2 == 0 and num >= 6 and num <= 20):
  print('weird')
if num % 2 == 0 and (num >= 2 and num <= 5) or (num % 2 == 0 and num > 20):
  print('not weird')

#nested if
city = 'toronto'
name = 'alexander'
if city == 'toronto':
  if name == 'alexander':
    print('welcome, newcomer!!')
  elif name == 'connor':
    print('Wassup')
  else:
    print('hello{}'.format(name))
else:
    print('Im not familiar with your city')

   