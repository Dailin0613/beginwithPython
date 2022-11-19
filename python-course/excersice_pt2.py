#functions_basic
def make_shirt(size, message):
  size = str(size)
  print('The size of this shirt is: ' + size)
  message = input('You want to make this shirt? :')
  print(message)
make_shirt(24, 'Yes')
