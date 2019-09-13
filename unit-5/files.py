#reading a File
my_file = open('unit-5/data/hello.txt')
print(my_file.read())
my_file.close()
#writting to a file
my_file = open('unit-5/data/hello.txt','w')
my_file('add this')
my_file.close()
#appending 
my_file = open('unit-5/data/hello.txt','a')
my_file('hello from the land')
my_file.close()
#reading a csv file

print('hello')
