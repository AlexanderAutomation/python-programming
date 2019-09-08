'''class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def say_hello(self):
        print('hello, my name is {}, and I am {} years old'.format(self.name, self.age))

p1 = Person('Alexander',41)'''

#create a rectangle class
#write a methods to calculate the perimeter area for your rectangles

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

#create and instagram account class
#class should have username, Email a list of pictures,
#and list of followers

#an instagramaccount can follow another Instagram Account