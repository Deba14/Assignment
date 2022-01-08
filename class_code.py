class Movie():
    
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns=columns
        self.booking={}
    def is_booked(self,row,col):
        seat_id=str(row) + str(col)
        if seat_id in self.booking:
            return True
        else:
            False
        
    def show_seats(self):
        for row in range(0,self.rows+1):
            for column in range(0,columns+1):
                if row == 0:
                    if column == 0:
                        print(" ",end=" ")
                    else:
                        print(column,end=" ")
                else:
                    if column == 0:
                        print(row,end=" ")
                    else:
                        if self.is_booked(row,column):
                            print("B",end=" ")
                        else:
                            print("S",end=" ")
                       
            print()
    
    def book_ticket(self):
        booking_row = int(input("Enter the number of the row that you want to book:"))
        booking_column = int(input("Enter the number of the column that you want to book:"))
        seat_id = str(booking_row) + str(booking_column)
        no_of_seats = self.rows * self.columns
        if no_of_seats <=60:
            price=10
        else:
            row_factor = self.rows//2
            if booking_row <= row_factor:
                price=10
            else:
                price=8
        print("Here is your price for the seat :",price)
        choice = int(input("Do you want to book ?:\n1.Yes\n2.No\nEnter your choice :"))
        if choice == 1:
            print("We are booking your ticket! \npleade enter your following details:")
            name = input("Please Enter your name :")
            age = input("Please Enter your age :")
            gender = input("Please Enter your gender :")
            mob = input("Please Enter your mobile no :")
            details = {'Name':name,'Age':age,'Gender':gender,'Mobile':mob,'Price':price}
            self.booking[seat_id] = details
            print("Your ticket is booked successfully!!!")
        elif choice == 2:
            print("Cancelling booking")
    
    def show_details(self,row,col):
        seat_id = str(row) + str(col)
        if seat_id in self.booking:
            detail = self.booking[seat_id]
            print("Here is the deatils: ")
            print("Name: ",detail['Name'])
            print("Age: ",detail['Age'])
            print("Gender: ",detail['Gender'])
            print("Mobile number: ",detail['Mobile'])
            print("Ticket book for : $",detail['Price'])
        else:
            print(f"seat for row {row} and seat for column{col} is not booked yet")