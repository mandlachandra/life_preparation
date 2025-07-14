class Car:

    def __init__(self,price,model):
        self.price = price
        self.model = model

    def display_price(self):
        print("price of this car")

    def display_model(self):
        print("model of this car")

obj = Car(10,"BMW")
print(obj.display_price())
print(obj.display_model())

