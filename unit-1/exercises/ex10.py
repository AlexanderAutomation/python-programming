playlist = [{'title':'Oh baby baby','artist':'Britney','genre':'pop','length':3},
{'title':'Oh baby baby','artist':'Romeo','genre':'bachata','length':6},
{'title':'latina','artist':'Jlo','genre':'pop','length':7},
{'title':'nomore','artist':'Jlo','genre':'pop','length':8},
{'title':'survivor','artist':'Beyonce','genre':'jazz','length':9},
{'title':'will always','artist':'Witney','genre':'pop','length':7},
{'title':'Respect','artist':'Aretta','genre':'Soul','length':6.5},
{'title':'Material girl','artist':'Madonna','genre':'pop','length':1},
{'title':'dont cry','artist':'Bob','genre':'Regue','length':10},
{'title':'love you','artist':'Britney','genre':'pop','length':13}]

''' Read dictionaries and print the song with the longest length'''

def find_max(my_list):
    max = my_list[0]
    for idx in range(1,len(my_list)):
        if my_list[idx] > max:
            max_value = my_list[idx]
    return max_value

nums = [25, 18, 33, 45, 99, 8, 1, 16, 2, 56]

max_num = find_max(nums)

print(max_num)

def longest_song(my_playlist):
    '''
    returns the longest song on a playlist
    '''
    max_song = {'title' : my_playlist[0]['title'], 'length':my_playlist[0]['length']}
    for idx in range(1,len(my_playlist)):
        if my_playlist[idx]['length'] > max_song['length']:
            max_song['title'] = my_playlist[idx]['title']
            max_song['length'] = my_playlist[idx]['length']
        
        
    return max_song

print(longest_song(playlist))

def most_song_artiste(any_playlist):
    '''print the name of the artiste wih the most songs in the list'''
    '''artiste_counter = {}
    for song in any_playlist:
        #split artist name(s) along slash
        artiste_names = song['artist'].split('/')
        if len(artiste_names):
           if artiste_names[0] in artiste_counter or artiste_names[1] in artiste_counter:
              artiste_counter[song['artist']] += 1
        else:
            if song['artist'] in artiste_counter:
                artiste_counter[song['artist']] = 1
        else:
            artiste_counter[song['artist']] = 1
    return artiste_counter

print(most_song_artiste(playlist))'''

if any ([1,2,3,5,7]) in [1,3,5]:
    print('yes!!!!!!')

''' Explain project and what is the data set'''
''' find some kind of data'''
'''kaggle'''
'''find a data set'''





