class Product:
    def __init__(self,description,id_num,price):
        self.description = description
        self.id_num = id_num
        self.price = price

    def __str__(self):
        return f'{self.description} {self.id_num} = {self.price}'
    
pc = Product('PC', 1, 199.95)
print (pc)
lst = [str(Product('some',n,19.99)) for n in range(10)]
print (lst)
