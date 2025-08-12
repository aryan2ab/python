from random import randint
class Train:

    def __init__(slf, train_number):
        slf.train_number = train_number


    def book(slf, fro, to):
        print(f"Booking ticket on train {slf.train_number} from {fro} to {to}")
        # Logic to book the ticket
        

    def getStatus(slf):
        print(f"Status of train {slf.train_number} is: On Time")
        

    def getFare(slf, fro, to):
        print(f"Calculating fare for train {slf.train_number} from {fro} to {to} is {randint(100,10000)}")

t = Train("12345")
t.book("Bangalore", "Delhi") 
t.getStatus()       
t.getFare("Bangalore", "Delhi")
        