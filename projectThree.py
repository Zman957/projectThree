def main():
    # Initialize the seating arrangement
    seats = ["Available" for _ in range(20)]  # 20 seats available
    first_class_seats = [0, 1, 2, 3]  # First-class seats
    emergency_seats = [6, 7, 14, 15]  # Emergency row seats

    def display_seats():
        print("\nSeating Arrangement:")
        for i, status in enumerate(seats):
            seat_type = "First-Class" if i in first_class_seats else (
                "Emergency" if i in emergency_seats else "Regular")
            print(f"Seat {i + 1}: {status} ({seat_type})")
        print()

    def is_seat_valid(seat_num):
        return 1 <= seat_num <= 20

    def is_seat_available(seat_num):
        return seats[seat_num - 1] == "Available"

    def purchase_seat(seat_num):
        if not is_seat_valid(seat_num):
            print("Invalid seat number. Please select a number between 1 and 20.")
            return False
        if not is_seat_available(seat_num):
            print("Seat already taken. Please choose another seat.")
            return False

        if seat_num - 1 in emergency_seats:
            print("You have selected an emergency row seat.")
            confirm = input(
                "Do you accept responsibility to assist in case of an emergency? (yes/no): ").strip().lower()
            if confirm != "yes":
                print("You must accept responsibility to book an emergency row seat.")
                return False

        if seat_num - 1 in first_class_seats:
            print("You have selected a first-class seat. A fee of $50 applies.")
            confirm = input("Do you want to proceed? (yes/no): ").strip().lower()
            if confirm != "yes":
                print("Booking canceled.")
                return False

        seats[seat_num - 1] = "Taken"
        print(f"Seat {seat_num} successfully booked!")
        return True

    print("Welcome to the Come Fly with Me booking system!")

    while True:
        display_seats()
        user_input = input("Enter seat number(s) to book (comma-separated) or 'exit' to quit: ").strip()
        if user_input.lower() == "exit":
            print("Thank you for using the Come Fly with Me booking system. Have a great flight!")
            break

        try:
            seat_numbers = list(map(int, user_input.split(',')))
        except ValueError:
            print("Invalid input. Please enter seat numbers separated by commas.")
            continue

        for seat_num in seat_numbers:
            purchase_seat(seat_num)

        if __name__ == "__main__":
            main()