#Creating and Using a class
#Creating a class
class Country:
    '''Show contries with cities and language, and then say the fronteir'''
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.latitude = 0 #Default value, if the default value is a string is ''
    def get_latitude(self):
        print('This latitude star in ' + str(self.latitude))
    def have_frontier(self):
        fronteir = input('Have fronteir with: ')
        while True:
         country_f = input('The country ')
         print("(If is all fronteir with, ended with the 'x' letter)")
         if country_f == 'x':
            break
the_country = Country('England', 'Great London')
print('The country select is ' + the_country.name + ' and the main city is ' + the_country.city)
the_country.have_frontier()
the_country.get_latitude()

#Inheritance
class City(Country):
    def __init__(self, name, city):
        super().__init__(name, city)
        self.borough = 32
    def has_borough(self):
        print('This city have a ' + str(self.borough) + ' as a borough')
the_city = City('Greater London', 'City of London')
the_city.has_borough()

