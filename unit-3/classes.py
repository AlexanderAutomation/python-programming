'''class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def say_hello(self):
        print('hello, my name is {}, and I am {} years old'.format(self.name, self.age))

p1 = Person('Alexander',41)'''

#create a rectangle class
#write a methods to calculate the perimeter area for your rectangles

'''
class Rectangle:
    def __init__(self, L, W):
        self.wight = L
        self.lenght = W

    def calculate_perimeter(self):
        return 2 * (self.wight + self.lenght)

    def calculate_area(self):
        return self.wight * self.lenght

r1 = Rectangle(10,2)

print(r1.calculate_area())

'''

#create and instagram account class
#class should have username, Email a list of pictures,
#and list of followers

#an instagramaccount can follow another Instagram Account

class InstagramAccount:
    def __init__(self,username, email):
        self.username = username
        self.email = email
        self.pictures = []
        self.followers = []

    def add_photo(self,photo_url):
        self.pictures.append(photo_url)

    '''def follow(self,account):
        try:
            account.followers.append(self)
        except:
            print('{account} is not a valid Instagramaccount'.format(account))'''
 
    def follow(self,account):
        if isinstance(account, InstagramAccount):
            account.followers.append(account)
        else:
            print('{account} is not a valid Instagramaccount'.format(account))


    def get_followers(self):
        return self.followers

    def __repr__(self):
        return "username: {}\nemail: {}\nfollowers: {}\n"f'username:{self.username},email:{self.email},followers:{self.followers}'
    


ac1 = InstagramAccount('alex33', 'Alex@gmail.com')

ac2 = InstagramAccount('pedro','pedro@gmail.com')

ac1.follow(ac2)

#print(ac1.get_followers())

print(ac2)

ac2.follow('johnsmith')





