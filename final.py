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
            if 0 <= int(rate) <= 5:
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

    def quantity_reducer(self):
        if self.get_quantity() == 0:
            print(f"{self.get_name()} not available")
            return False
        else:
            self.set_quantity()
            return True

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


    def add_new_product(self ,name ,category ,price , quantity):
        self.product_list.append(Products(name , category ,price , quantity))

    def search_by_name(self, product_name):
        for item in self.product_list:
            if item.get_name() == product_name:
                print(f"1) {item.get_name()}\t{item.get_category()}\t{item.get_price()}$\tqnt: {item.get_quantity()}\trate: {item.get_rate()}")
                inp = input("press 'A' to add this item to your cart : ")
                if inp.upper() =='A':
                    return item
        print("no match found")


    def search_by_category(self ,category):
        list_by_category = []
        for item in self.product_list:
            if item.get_category() == category:
                list_by_category.append(item)
        if list_by_category:
            for indx , prod in enumerate(list_by_category):
                print(f"{indx +1}) {prod.get_name()}\t{prod.get_category()}\t{prod.get_price()}$\tqnt: {prod.get_quantity()}\trate: {prod.get_rate()}")
            inp = input("enter your chioce number : ")
            try:
                return list_by_category[int(inp)-1]
            except:
                return False
        else:
            print("no match found")
            return False
                
    def add_to_cart(self ,product_object : Products):
        self.shoping_cart.append(product_object)

    def show_cart(self):
        for indx , prod in enumerate(self.shoping_cart):
            print(f"{indx+1}) {prod.get_name()}\t{prod.get_category()}\t{prod.get_price()}$\tqnt: {prod.get_quantity()}\trate: {prod.get_rate()}")

    def kharid_nahaee(self):
        price = 0
        for prod in self.shoping_cart:
            price += prod.get_price()
            qnt = prod. quantity_reducer()
            if qnt:
                return price 
            return False
            


    def rate_menu(self):
        if self.shoping_cart:
            self.show_cart()
            product = input("if you want to rate enter products number  \n to quit enter 0 : " , )
            if product == "0":
                return
            rate = input("pls enter your rate : ")
            self.shoping_cart[int(product)-1].set_rate(rate)
            print("thanks for your rate")
        else:
            print("your cat is empty!!!")



manage = ProductManager()

while True:
    print("press 'c' to search by category")
    print("press 'n' to search by products name")
    print("press 'm' to see your shopping cart")
    print("press 'f' to submit your shopping")
    print("press 'x' to exit")
    inp = input().upper()

    if inp == 'C':
        cat = input("write your category : ")
        selected_product = manage.search_by_category(cat)
        if selected_product is not False:
            print("product was added to your cart!!!")
            manage.add_to_cart(selected_product)


    if inp == 'N':
        name = input("write your product name : ")
        selected_product = manage.search_by_name(name)
        if selected_product is not False:
            print("product was added to your cart!!!")
            manage.add_to_cart(selected_product)
  

    if inp == 'M':
        manage.rate_menu()


    if inp == 'F':
        price = manage.kharid_nahaee()
        if price:
            manage.show_cart()
            print(f"your payment price is {price}$")
            inp = input("press 'P' to submit yor order and pay : ")
            if inp.upper() == 'P':
                manage.save()
                print("your order was submited")
        

    if inp == 'X':
        manage.save()
        exit()


# manage .add_new_product("maast" ,"labaniat" , 5 ,10)
# manage .add_new_product("moz" ,"miveh" , 2 , 5)
# manage .add_new_product("shir" ,"labaniat" , 3 , 10)
# manage .add_new_product("sib" ,"miveh" , 2 , 5)
# manage .add_new_product("mobile" ,"electronic" , 100 , 2)
# manage .add_new_product("laptop" ,"electronic" , 350 , 1)
# manage.save()