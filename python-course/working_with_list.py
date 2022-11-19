#looping trough an entire list
songs = ['Magic Shop', 'Boy With Luv', 'Butterfly', 'Dynamite', 'Fly To My Room']
for song in songs:
    print(song)
#doing something after the looping 'for'
print('All this songs are by BTS')

#making numerical list
#->using the range() function
for value in range(0,5):
    print(value)

#working wih part of a list
#->slicing a list
print(songs[1:3])
#->looping through a slice
cities = ['London', 'Manchester', 'Liverpool', 'Madrid', 'Barcelona', 'Sevilla']
print(f'I will move to one of this city {cities}')
for city in cities[:3]:
    print('This cities are from England')
#->copying list
type_of_house = ['flat', 'condomine', 'mansion']
my_fav_house = type_of_house[:]
print(my_fav_house)

#defination of tuples
lucky_numbers = (23, 24, 25)
print(lucky_numbers[0])
print(lucky_numbers[1])
print(lucky_numbers[2])

 
