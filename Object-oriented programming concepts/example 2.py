class Product:
    next_id = 0 #static variable
    def __init__(self,description,id_num,price):
        self.description = description #instance variable 
        self.id_num = Product.next_id
        Product.next_id += 1
        self.price = price

    def __str__(self):
        return f'{self.description} {self.id_num} = {self.price}'
    
pc = Product('PC', 1, 199.95) #__init__ automatically called
mac = Product('macmac', 2, 2999.95)
print (pc,mac) 
