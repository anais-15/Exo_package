class Shoes:
    def __init__(self, size, brand, color, price, stock):
        self.size=size
        self.brand=brand
        self.color=color
        self.price=price
        self.stock=stock

    def sold(self, number):
        mes = ""

        if self.stock > number:
            self.stock=self.stock-number
            mes="Vendu"
        else :
            mes="Pas assez en stock" 

        return mes

    def sale(self, pourcentage):
        print(f"Ancien prix: {self.price}")
        self.price=self.price*(1-pourcentage)
        print (f"Nouveau prix : {self.price}")


    

        