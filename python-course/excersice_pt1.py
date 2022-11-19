#if statements

usernames = ['admin', 'thv', 'rkive', 'j.m', 'jin', 'suga', 'jungkook.97', 'uarmyhope']
user = 'admin'
for username in usernames:
    print(f'Welcome to this website @{username}')
if user in usernames:
    print('Hello admin. Would you to see the last report')

if usernames == []:
  print('We needed to find the users')

#input()
question = input('What kinda of cars you look for?')
print(question)
if question == 'Ferrari':
  print('We dont adquired this type of cars')
else:
  pay = input('How much you have to pay')
  pay = int(pay)
  print(f'You have: {pay}')
  if pay < 20:
    print('You cant purchase the car')
  else:
    print('Thanks for your buy')
  
   
  
 