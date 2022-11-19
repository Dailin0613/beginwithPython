#Classes
class Restaurant:
    '''Contain the whereabout of the restaurant'''
    def __init__(self, restaurant_name, cuisine_type):
      self.restaurant_name = restaurant_name
      self.cuisine_type = cuisine_type
    def describe_restaurant(self, location, services):
      self.location = input('Have the following location: ')
      print(self.location)
      self.services = input('Offerd this type of services: ')
      print(self.services)
    def open_restaurant(self):
      unclose = input('Restaurant is open?')
      print(unclose)
      if unclose == 'Yes':
        print('The restaurant is already open')
      else:
        print('Wait for the open time')
my_restaurant = Restaurant('Le pizza', 'Italian food')
print('I open  new restaurant named ' + my_restaurant.restaurant_name + ' the main cuisine is ' + my_restaurant.cuisine_type)
my_restaurant.describe_restaurant('Center on London', 'Italian Food')
my_restaurant.open_restaurant()
      

