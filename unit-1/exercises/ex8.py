'''
Create a list of destinations Go through  the list, 
add a rank to each destination.

'''
import random
destinations = ['colombia','uk','croatia','mexico','syria','thailand','jamaica','usa','ecuador','peru','spain']

for idx in range(len(destinations)):
    rank = random.randint(1,10)
    destinations[idx] += '-' + str(rank)
print(destinations)