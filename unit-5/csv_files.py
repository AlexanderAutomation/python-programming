#import csv
import json

#read a csv file

'''with open('data/deniro.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        print(row)'''

#read a json file
with open('data/sample.json') as json_file:
    data = json.load(json_file)
    for student in data['students']:
        print(student['name'],student['age'])

    #print(json.dumps(data, indent=4))



