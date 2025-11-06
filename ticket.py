class Theater:
    def __init__(self, name):
        self.name = name
        self.seats = {}
        self.bookings = {}
        rows = ["A", "B", "C", "D", "E"]
        for row in rows:
            for num in range(1, 6):
                self.seats[f"{row}{num}"] = True  # True means available

    def show_seats(self):
        print(f"\n{self.name} Seat Layout:")
        for row in ["A", "B", "C", "D", "E"]:
            for num in range(1, 6):
                seat = f"{row}{num}"
                mark = "□" if self.seats[seat] else "▣"
                print(f"{seat}:{mark}", end="\t")
            seat_type = "Standard" if row in ["A", "B"] else "Premium"
            print(f"<= {seat_type}")

    def get_price(self, seat):
        return 100 if seat[0] in ["A", "B"] else 150

    def book_seat(self, seat, name):
        seat = seat.upper()
        if seat not in self.seats:
            return False, "Invalid seat."
        if not self.seats[seat]:
            return False, "Seat already booked."
        self.seats[seat] = False
        self.bookings[seat] = name
        return True, ""

    def cancel_seat(self, seat):
        seat = seat.upper()
        if seat not in self.seats:
            return "Invalid seat."
        if self.seats[seat]:
            return "Seat is already available."
        self.seats[seat] = True
        user = self.bookings.pop(seat)
        return f"Cancelled {seat} booked by {user}."

    def book_multiple(self, name, total_seats):
        booked = []
        total_price = 0
        self.show_seats()
        while len(booked) < total_seats:
            seat = input(f"Enter seat #{len(booked)+1}: ").upper()
            success, msg = self.book_seat(seat, name)
            if success:
                price = self.get_price(seat)
                booked.append(seat)
                total_price += price
                print(f"{seat} booked for Rs.{price}")
            else:
                print(msg)
        print("\nBooking done:", booked)
        print("Total price: Rs.", total_price)

# Create 3 screens
screens = {
    "1": Theater("Screen 1"),
    "2": Theater("Screen 2"),
    "3": Theater("Screen 3")
}

# Main program
while True:
    choice = input("\nSelect Screen (1-3) or 0 to Exit: ")
    if choice == "0":
        print("Thanks for using our booking system!")
        break
    if choice not in screens:
        print("Invalid screen.")
        continue

    theater = screens[choice]
    while True:
        print(f"\n{theater.name} Options:")
        print("1. View Seats")
        print("2. Book Seats")
        print("3. Cancel Seat")
        print("4. Back to Main Menu")

        option = input("Choose an option: ")
        if option == "1":
            theater.show_seats()
        elif option == "2":
            name = input("Enter your name: ")
            try:
                count = int(input("How many seats to book? "))
                theater.book_multiple(name, count)
            except:
                print("Enter a valid number.")
        elif option == "3":
            seat = input("Enter seat to cancel (e.g., B3): ")
            print(theater.cancel_seat(seat))
        elif option == "4":
            break
        else:
            print("Invalid option.")
