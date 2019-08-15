'''
def list_intersection(list_one,list_two)
#create a new list only items in both firts and second list
result = []
for item_one in list_one:
    for item_two in list_two:
        if item_one == item_two:
            result.append(item_onw)

return result

print(list_intersection([1,3, 5, 7, 9], [3, 4, 5, 6, 11]))

def list_intersection_2(list_one, list_two)
    result = []
    for item in list_one:
        if item in list_two:
            result.append(item)
    return result

def reverse_list(mylist):
    
    returns a new list that is the reverse of the one passed in
    
    result = []
    for idk range(len(my_list -1, -1, -1):
        result.append(my_list[idx])
    return result

#print(reverse_list(['apple','peach','strawberry','banana']))

#short cut
def reverse_list_2(my_list):
    return my_list[::-1]

#print(reverse_list_2([2, 4, 6, 8, 10]))

def reverse_str(my_string):
    reversed_string = ''
    for idx in range(len(my_string -1, -1, -1):
        reversed_string += my_string[idx]
    return reversed_string

def is_palindrome(my_string):
    
    check if my_string is a palindrome
    return True if it is, False otherwise
    
    backwards = reverse-str(my_string)
    if backward == my_string:
        return True
    return False

    print(is_palindrome('level'))
'''
'''
def reverse_str(my_string):
    reversed_string = ''
    for idx in range(len(my_string) - 1, -1, -1):
        reversed_string += my_string[idx]
    return reversed_string 

'''
def is_palindrome(my_string):
    '''
    check if my_string is a palindrome
    return True if it is, False otherwise
    '''
    backwards = reverse_str(my_string)
    if backwards == my_string:
        return True
    return False


print(is_palindrome('level'))
print(is_palindrome('racecar'))
print(is_palindrome('aaa'))
print(is_palindrome('aaadba'))
print(is_palindrome('amanaplanacanalpanama'))





   
   









