class Booking_Movie_Ticket(object):
    def __init__(self,movie,price,seats):
        self.movie=movie
        self.price=price
        self.seats=seats
    def movie_details(self):
        print("Movie Name   :",self.movie)
        print("Ticket Price :",self.price)
        print("No.of seats  :",self.seats)
    def show_ticket(self):
        self.seats=['A1','A2','A3','A4']
        print("Available Seats: ",self.seats )
    def book_ticket(self):
        s1,s2=map(str,input("Choose Tickets you want: ").split())
        if s1 or s2 in self.seats:
            print("Book Now")
        else:
            print("Sorry Booking Closed. \n. thank you for visiting. see you again ")
        self.seats.remove(s1)
        self.seats.remove(s2)
        print(f'{s1,s2} seats Booked successfully')
        print(f'{self.seats} has left ')
b=Booking_Movie_Ticket("Rangam",50,4) 
b.movie_details()
b.show_ticket()
b.book_ticket()   
