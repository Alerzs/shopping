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
    
    def set_quantity(self):
        self.__quantity = int(self.__quantity) - 1
        

    
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
        self.product_name = product_name
        for items in self.product_list:
            if item.get_name() == self.product_name:
                return items
            
        return False
        # search self.product_list if the products name == product_name return object otherwise return false

    def search_by_category(self ,category):
        self.category = category
        list_by_category = []
        for items in self.product_list:
            if item.get_category()== self.category:
                list_by_category.append(item)
        return (f"{self.categry}: {list_by_category}")
                
        # similar to search by name but this time show a list of product that have given category as attribute
    def add_to_cart(self ,product_object : Products):
        self.shoping_cart.append(product_object)

    def show_cart(self):
        return self.shoping_cart
    
    def kharid_nahaee(self):
        price = 0
        for prod in self.shopping_cart:
            price += prod.get_price()
            prod.set_quantity()
        return price 
            
            
        # show the total price and change the quantities of each product

    def rate_menu(self):
        
        for i in range(len(self.shopping_cart)):
            print(i , self.shopping_cart[i])
        prod = input("pls enterthe number of your chosen product  \n or if you want to quit enter 00 " , )
        if rate == "00":
            return
        rate = input("pls enter your rate" , )
        self.shopping_cart[int(prod)].set_rate(rate)
        print("thanks for your rate")


        
        
        #creat a menu that costumer choos one of his cart product and add a rating to it

