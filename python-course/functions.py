#Defination
def greet():
 '''Display a simple greeting'''
 print('Hello Word from Function')
'''Call the function'''
greet()

#Passing Information to a function
def all_song(song):
    song = input('My favorite song is: ')
    print(f'By BTS: {song}')
all_song('Fake Love')

#Positional Arguments
def cover(artist, album):
    print('\nMy favorite artist is: ' + artist.title())
    print('My favorite album ' + album + ' is by ' + artist)
cover('BTS', 'MOTS')

#Returing a Simple Value
def get_artist(name, group):
    member = name + ' ' + group
    return(member.title())
musician = get_artist('V', 'BTS')
print(musician) 
 
 