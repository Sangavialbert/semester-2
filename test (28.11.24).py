class Inventory:
    def __init__(self,prodId,prodName,prodCount):
        self.prodId=prodId
        self.prodName=prodName
        self.prodCount=prodCount
class Display1(Inventory):
    def show1(self):
        print("ID:",self.prodId)
        print("Name:",self.prodName)
        print("Count:",self.prodCount)
display=Display1(1234567890,"Mobile Case",5)
display.show1()
