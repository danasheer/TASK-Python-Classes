class Wallet:
    def __init__(self, money):
        self.money=0
       
        pass

    def credit(self, amount):
       amount = input(int("write the credit amount "))
       self.money += amount 
       return ("the amount of credit card ")

    def debit(self, amount):
       amount = input(int("write the debit amount "))
       self.money -= amount 
       return ("the amount of credit card ")



wallet = Wallet(6)
wallet = Wallet()  # This should default money inside the wallet to 0
print(wallet)


class Person :
    def __init__(self, name, location, wallet ):
        self.name = name
        self.location= location
        self.wallet = wallet 

    def moveto(self, point):
        point = input(int("write th location value"))
        self.location += point  
        return (f" the new location that you have {self.location}")

person = Person("Moh", 5, 50)
     


class Vendor:
    def __init__(self, name, location, wallet, range, price ):
        super().__init__(self, name, location, wallet )
        self.range = 5
        self.price = 1

    def sellTo(self, customer, number_of_icecreams, moveto, debit, credit):
        newlocation = moveto(3,4)
        print (f" the location is { newlocation }")
        self.depit(6)
        vendor.cridet(6)

vendor = Vendor("Abdallah", 3, 6)


class Customer:
    def __init__(self, name, location, wallet,  ):
        super().__init__(self, name, location, wallet )
    
    def _is_in_range(self, vendor):
        range = vendor.location - self.location
        if range >= 1:
           print("the customer in the range of location")
        else :
         print(" he is out the range ")

    def  have_enough_money(self, vendor, number_of_icecreams):
        if self.wallet >= 1:
            print(" the customer has enough money")
            return True
            
        else:
            print("the customer dosent have enough money ")
            return False
    
    def request_icecream(vendor, number_of_icecreams):
        if 


customer1 = Customer("Abdallah", 3, 6)
