from random import randint
class Train:

    def __init__(self, train_number):
        self.train_number = train_number


    def book(self, fro, to):
        print(f"Booking ticket on train {self.train_number} from {fro} to {to}")
        # Logic to book the ticket
        

    def getStatus(self):
        print(f"Status of train {self.train_number} is: On Time")
        

    def getFare(self, fro, to):
        print(f"Calculating fare for train {self.train_number} from {fro} to {to} is {randint(100,10000)}")

t = Train("12345")
t.book("Bangalore", "Delhi") 
t.getStatus()       
t.getFare("Bangalore", "Delhi")
        