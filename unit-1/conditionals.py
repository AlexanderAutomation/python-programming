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

name = 'fizzbuzz'

if name.length > 4:
    print('longer than 4')

if name.length > 6:
    print('longer than 6')



