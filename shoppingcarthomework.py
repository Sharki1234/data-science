import pandas as p
import random as r
shoppingcart_file = open("shoppingcart_data.csv","x")

with open("shoppingcart_data.csv","a") as shoppingcart_file:
    shoppingcart_file.write("OrderId,Category,Price\n")
def add_orders(OrderId,Category,Price):
    with open("shoppingcart_data.csv","a") as shoppingcart_file:
        shoppingcart_file.write(f"{OrderId},{Category},{Price}\n")

add_orders(r.randint(0,10000),"Electronics",r.randint(0,10000))
add_orders(r.randint(0,10000),"Furniture",r.randint(0,10000))
add_orders(r.randint(0,10000),"Electronics",r.randint(0,10000))
add_orders(r.randint(0,10000),"Decorations",r.randint(0,10000))
add_orders(r.randint(0,10000),"Electronics",r.randint(0,10000))
add_orders(r.randint(0,10000),"Clothes",r.randint(0,10000))
add_orders(r.randint(0,10000),"Clothes",r.randint(0,10000))
add_orders(r.randint(0,10000),"Electronics",r.randint(0,10000))

cart = p.read_csv("shoppingcart_data.csv")
above_1000 = cart[cart["Price"]>1000]
electronics = cart[cart["Category"]=="Electronics"]
both = cart[(cart["Price"]>1500) & (cart["Category"]=="Electronics")]
print(above_1000.head())
print(electronics.head())
print(both.head())