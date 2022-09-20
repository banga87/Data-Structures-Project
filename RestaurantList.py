# Node based structure
import RestaurantData

class Restaurant:
    def __init__(self, restaurant:list, next_restaurant=None):
        self.restaurant = {}
        self.restaurant['Name'] = restaurant[1]
        self.restaurant['Type'] = restaurant[0]
        self.restaurant['Price'] = restaurant[2]
        self.restaurant['Rating'] = restaurant[3]
        self.restaurant['Address'] = restaurant[4]
        self.next_restaurant = next_restaurant

    def get_type(self):
        return self.restaurant["Type"]

    def get_name(self):
        return self.restaurant["Name"]
    
    def get_price(self):
        return self.restaurant["Price"]

    def get_rating(self):
        return self.restaurant["Rating"]

    def get_address(self):
        return self.restaurant["Address"]

    def get_next_restaurant(self):
        return self.next_restaurant

    def set_next_restaurant(self, next_restaurant):
        self.next_restaurant = next_restaurant

    def print_restaurant(self):
        print("--------------------")
        for key, value in self.restaurant.items():
            print("{} : {}".format(key, value))
        print("--------------------")

# LinkedList structure
class RestaurantList:
    def __init__(self, restaurant=None):
        self.head_restaurant = None
        if restaurant is not None:
            self.head_restaurant = Restaurant(restaurant)

    def get_head_restaurant(self):
        return self.head_restaurant

    def insert_restaurant(self, restaurant:list):
        new_restaurant = Restaurant(restaurant)
        new_restaurant.set_next_restaurant(self.head_restaurant)
        self.head_restaurant = new_restaurant

    def populate_list(self, list):
        for restaurant in list:
            self.insert_restaurant(restaurant)

    def get_restaurant_names(self):
        location = self.get_head_restaurant()
        names = []
        while location:
            names.append(location.get_name())
            location = location.get_next_restaurant()
        return names

    def get_types(self):
        location = self.get_head_restaurant()
        types = []
        while location:
            if location.get_type() not in types:
                types.append(location.get_type())
            location = location.get_next_restaurant()
        return types

    def type_search(self, type):
        location = self.get_head_restaurant()
        type_list = []
        while location:
            if location.get_type() == type:
                type_list.append(location)
            location = location.get_next_restaurant()
        return type_list

    def name_starts_with(self, char):
        location = self.get_head_restaurant()
        starts_with = []
        while location:
            if location.get_name()[0].lower() == char.lower():
                starts_with.append(location)
            location = location.get_next_restaurant()
        return starts_with

restaurant_data = RestaurantData.restaurant_data
list = RestaurantList()
list.populate_list(restaurant_data)

print("Welcome to Banga's Restarant thingy!!\nFollow the instructions to find a restaurant.\n")
print("To start, please select one of the following cuisines::::")

cuisines = list.get_types()
for cuisine in cuisines:
    print(cuisine)

preference = input("Which cuisine would you prefer?\n")
available_restaurants = list.type_search(preference)

print("These restaurant's are available:")
for restaurant in available_restaurants:
    restaurant.print_restaurant()



