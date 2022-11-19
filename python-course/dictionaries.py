#simple dictionary
member = {
    'name' : 'Kim Taehyung',
    'city' : 'Daegu',
    'year' : 1995,
    'last_solo_song' : 'Christmas Tree'
}
print(member['name'])
print(member['city'])

#accessing values in dictionaries
year = member['year']
print('V aka ' + member['name'] + ' was born on ' + str(year))

#adding new key-value pairs
member['group'] = 'BTS'
member['position'] = 'Vocal line'
print(member)

#modifying values in dictionary
member['city'] = 'Seul'
print(member['name'] + ' now live in ' + member['city'])

#removing key-value pairs
del member['last_solo_song']
print(member)

#looping throug a dictionary
#looping through all key-value pairs
song = {
    'name' : 'Christmas Tree',
    'album' : 'OST Beloved Summer',
    'genre' : 'OST',
    'artist' : 'V'
}
for key, value in song.items():
    print('\n Key: ' + key)
    print('\n Value: ' + value)

#Nesting
#->A list of dictionaries
user = {
    'username' : 'web_js_0613',
    'email' : 'dailinc198@gmail.com',
    'account' : 'Instagram'
}
person = {
    'name' : 'Dailin',
    'lastname' : 'Chibas',
    'country' : 'England'
}
job = {
    'enterprise' : 'Google Inc',
    'position' : 'Software Engeener',
    'language' : 'Python'
}
citizens = [user, person, job]
for citizen in citizens:
    print(citizen)

#-> A list in a dictionary
country = {
    'name' : 'England',
    'language' : 'english',
    'main_cities' : ['London', 'Manchester', 'Cambridge']
}
print(country)
 
