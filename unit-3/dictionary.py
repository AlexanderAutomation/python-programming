#creating a dictionary
car_details = {"make":"chevy","model":"convertte","year":"1963","seats":2,"color":"black"}
person = {"heigh":1.90,"weight":180,"eye_color":"brown","hair":"black"}
eng_to_pl = {"yes":"tak","no":"nie"}
office_supplies_brands = {"stapler":"staples","calculator":"casio"}
color_description = {"orange":"brigth","blue":"dark","red":"deep"}
'''
#get data from dictionaries

print(car_details)

#get details from a dictionary

print(car_details["make"])

#iterate over a dictionary
for key in car_details:
    print(key)
'''

#iterate over a disctionary
'''
for key in car_details:
    print(car_details[key])
'''
#print key and value
for key in car_details:
    print(key,car_details[key])

#check for value in a dictionary
if('year') in car_details:
    print(car_details['year'])

#if a key is not in the dictionary
print(eng_to_pl['mom'])

'''
#Homework
#Build a list of dictionary of all the major cities in Canada
each dictionary will store the city:
-name
-lattitude
-longitude
-size
-population
'''

