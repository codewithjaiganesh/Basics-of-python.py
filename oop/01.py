class product :
    count = 0
    def __init__(self,name,price,discount):
        self.Name = name
        self.price = price
        self.discount = discount
        product.count+=1
    def get_info(self):
     print(f"The product is {self.Name} price {self.price} and discount {self.discount}")
 
    @classmethod
    def get_count(cls):
         print(f"total products in the store {cls.count}")
@staticmethod
def final_price(price,discount):
      f_price = price-(discount*price/100)
      print("final price is :",f_price)




p1 = product("book",500,40)
p2 = product("car",500000,10)
p3 = product("phone",100000,20)

product.get_count()
p1.get_info()
final_price(5000,50)

