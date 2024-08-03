import pickle

class Products:
    
    def __init__(self ,name ,category ,price ,quantity ) -> None:
        self.__name = name
        self.__price = price
        self.__category = category
        self.__quantity = quantity
        self.__rates = []

    @staticmethod
    def mean(lst):
        if len(lst) > 0:
            return round(sum(lst) / len(lst) , 2)
        return 0
    @staticmethod
    def rate_check(rate):
        try:
            if 0 < int(rate) < 5:
                return True
            return False
        except:
            return False
    def get_quantity(self):
        return self.__quantity
    
    def get_category(self):
        return self.__category
    
    def get_rate(self):
        return self.mean(self.__rates)
    
    def get_price(self):
        return self.__price
    
    def get_name(self):
        return self.__name
    
    def set_rate(self , rate):
        if self.rate_check(rate):
            self.__rates.append(int(rate))
            return
        print("wrong rate")
    
    def quantity_reducer(self):
        if self.__quantity == 0:
            print("product not available")
        else:
            pass

    
class ProductManager:

    def __init__(self) -> None:
        try:
            with open('product_data.pkl', 'rb') as inp:
                data = pickle.load(inp)
                inp.close()
                self.product_list = data
        except:
            self.product_list = []
        self.shoping_cart = []


    def save(self):
        with open('product_data.pkl', 'wb') as otp:
            pickle.dump(self.product_list , otp)


    def add_new_product(self ,name ,category ,price):
        self.product_list.append(Products(name , category ,price))

    def search_by_name(self, product_name):
        # search self.product_list if the products name == product_name return object otherwise return false
        pass

    def search_by_category(self ,category):
        # similar to search by name but this time show a list of product that have given category as attribute
        pass

    def add_to_cart(self ,product_object : Products):
        self.shoping_cart.append(product_object)

    def show_cart(self):
        return self.shoping_cart
    
    def kharid_nahaee(self):
        # show the total price and change the quantities of each product
        pass

    def rate_menu(self):
        #creat a menu that costumer choos one of his cart product and add a rating to it
        pass



#====================================menu==========================================

manage = ProductManager()

while True:
    print("press 'c' to search by category")
    print("press 'n' to search by products name")
    print("press 'm' to see your shopping cart")
    print("press 'f' to submit your shopping")
    print("press 'x' to exit")
    inp = input().upper()

    if inp == 'C':
        cat = input("write your category")
        selected_product = manage.search_by_category(cat)
        manage.add_to_cart(selected_product)

    if inp == 'N':
        name = input("write your product name")
        selected_product = manage.search_by_name(name)
        manage.add_to_cart(selected_product)

    if inp == 'M':
        manage.show_cart()

    if inp == 'F':
        manage.kharid_nahaee()

    if inp == 'X':
        manage.save()
        exit()
