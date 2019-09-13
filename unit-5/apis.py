import requests
import json

'''response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')

response_data = response.json()

response_data

nhl_teams = response_data['teams']

print(json.dumps(nhl_teams[0], indent = 2))


response = requests.get('http://api.open-notify.org/astros.json')

response_data = response.json()

print(json.dumps(response_data, indent=2))

#print the names of the people onboard the ISS

for people in response_data['people']:
    print (people['name'])
'''

#print the names of the venues of all teams

'''response = requests.get('https://statsapi.web.nhl.com/api/v1/teams').json()
data = response['teams']
print(type(data))
#i = 0
for team in data:
   print(data[team]['venue']['name'])
   team += 1'''

# find out how many teams ate in eastern conference

#i = 0
'''team_count = 0
for team in data:
   if data[team]['conference']['name'] == 'Eastern':
       #print(data[i]['name'])
       team_count += 1
       #i += 1
print('Total No. of Eastern Conference Teams: ' + str(team_count))'''

# find out which  team is the oldest (earliest firts year of play)

result = []
for team in data:
   result.append(
       {'name': team['name'], 'firstYearOfPlay': team['firstYearOfPlay']})
   #i += 1
# From newest to oldest
# newlist = sorted(result, key=lambda k: k['firstYearOfPlay'], reverse=True)
#newlist = sorted(result, key=lambda k: k['first Season'], reverse=False)
print(newlist[0])