'''
Read a sentence
print each word and frequency
'''

#use a dictionary
'''
'This is a sentence that has many words it is a good sentence'

{
    'this':1,
    'is':1,
    'a':1,
    'sentence':1,
    'that':1,
    'has':1,
    'many':1
    'words':1,
    'it':1,
    'good':1
}
'''
#create dictionary
frequency = {}

# Read in a sentence
sentence = input('enter a sentence: ')

#break sentence into words (tokenize)
words = sentence.split(' ')

#loop over our words
for word in words:
    # if in dictionary 
    if word in frequency:
        frequency[word] += 1
    else: 
        frequency[word] = 1
print(frequency)

#do execises for frequency counter and for loops.