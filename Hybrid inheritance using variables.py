class Restaurant:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def displayRestaurant(self):
        print("Name=",self.name,"Price=",self.price)

class Table(Restaurant):
    def __init__(self,name,price,tableno):
        super().__init__(name,price)
        self.tableno=tableno
    def displayTable(self):
        print("Tableno=",self.tableno)

class Details(Table,Restaurant):
    def __init__(self,name,price,tableno,seats):
        super().__init__(name,price,tableno)
        self.seats=seats
    def displayDetails(self):
        self.displayRestaurant()
        self.displayTable()
        print("Seat:",self.seats)
        
obb=Details("Biriyani",500,2,6)
obb.displayDetails()
