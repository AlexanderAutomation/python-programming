classmates = ['connor','efe','alexander','bianca','edwin','greg']
'''
#print a list
print(classmates)

#number of items in a list - use the function len
print(len(classmates))

# get a spesific item - the first
print(classmates[0])

#print last element
print(classmates[len(classmates)-1])
'''
'''
#shortcut for last element
print(classmates[-1])

#slicing - takin sections of the list
print(classmates[0:3])
'''
'''
#adding an element to the end of a list
classmates.append('princeton')

print(classmates)

#remove from end of the list
classmates.pop()

print(clasmmates)
'''
'''
#insert at a spesifict position
classmates.insert(0,'princeton')
print(classmates)

#remove an element
classmates.remove('princeton')
print(classmates)
'''
'''
#calculating the sum of a list of numbers
ages = [15,25,30,27,29,41,23,20,31,19]

#use a for loop
total_ages = 0
for age in ages:
    total_ages += age

print(total_ages)

#another for lopp - use range and indexes
for idx in range(len(ages)):
   total-ages += ages [idx]

print(total_ages)
'''
#calculating the sum of all odd number ages in the list
for age in ages:
    if age % 2 == 1:
        total_ages += age

print(total_ages)


