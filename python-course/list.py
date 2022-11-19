#defination
albums = ['Love yourself:Answer', 'MOTS:7', 'MOST:Persona', 'PROOF']

#access the one item of the list
print(f'My favorit bts album is {albums[1]}')

#access the last item in the list
print(f'The recient bts album is {albums[-1]}')

#using individual value from a list
print(f'My first listen bts was when their release {albums[2].title()}' + ' album') 

#modifing item in a list
albums[3] = 'Wings'
print(f'Change PROOF ' + f'for {albums[3]}')

#adding item to a list
albums.append('Dark&Wild')
print(albums)

#inserting item into a list
albums.insert(2, 'Face Yourself')
print(f'I insert my favorite albums japanse {albums[2]}')

#REMOVE
#removing an item using the 'del' statement
del albums[2]
print(albums)
#removing an item using the pop() method, this method remove the last item y saved y the new variable
last_album = albums.pop()
print(albums)
print(last_album)
#popping items for any position n a list
all_albums = albums.pop(0)
print(f'The most beutiful album by bts is {all_albums}')

#ORGANIZING
#Sorting list permanentily with sorth(), this method organizing a list alphabetically
albums.sort()
print(albums)
#if want reverse 
albums.sort(reverse = True)
print(albums)
