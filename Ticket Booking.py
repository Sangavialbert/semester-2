import random

class Customer:
    def _init_(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

    @staticmethod
    def generate_customer_id():
        return f"TICK{random.randint(1000, 9999)}"

    @staticmethod
    def verify_customer_id(cust_id):
        if cust_id.startswith("TICK") and cust_id[4:].isdigit():
            print("Customer ID is valid")
            return True
        else:
            print("Invalid Customer ID")
            return False


class TicketBooking:
    def _init_(self):
        self.events = {
            "Concert": {"price": 1000, "seats": 100},
            "Movie": {"price": 100, "seats": 100},
            "Drama": {"price": 150, "seats": 150},
        }
        self.booked_tickets = []

    def view_events(self):
        print("\nAvailable Events:")
        for event, details in self.events.items():
            print(f"{event}: {details['price']} per ticket, {details['seats']} seats available")

    def book_tickets(self, event_name, quantity, customer):
        if event_name in self.events:
            event = self.events[event_name]
            if event["seats"] >= quantity:
                total_price = event["price"] * quantity
                event["seats"] -= quantity
                self.booked_tickets.append({
                    "customer_id": customer.customer_id,
                    "event": event_name,
                    "quantity": quantity,
                    "total_price": total_price,
                })
                print(f"\nSuccessfully booked {quantity} ticket(s) for {event_name}. Total price: {total_price}")
            else:
                print("\nNot enough seats available.")
        else:
            print("\nEvent not found.")

    def view_tickets(self, customer):
        print("\nYour Tickets:")
        customer_tickets = [t for t in self.booked_tickets if t["customer_id"] == customer.customer_id]
        if not customer_tickets:
            print("No tickets booked.")
        else:
            for ticket in customer_tickets:
                print(f"Event: {ticket['event']}, Quantity: {ticket['quantity']}, Total Cost: {ticket['total_price']}")


# Main program
print("************ Welcome to the Ticket Booking Application ***********")
cust_id = input("Enter your customer ID (or press Enter to register): ")

if cust_id and Customer.verify_customer_id(cust_id):
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    customer = Customer(cust_id, name, phone)
    print("\nCustomer ID verified. Proceeding to booking details.")
else:
    print("\nInvalid or missing Customer ID. Please register.")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    cust_id = Customer.generate_customer_id()
    customer = Customer(cust_id, name, phone)
    print(f"Your new Customer ID is: {cust_id}")

book = TicketBooking()

while True:
    print("\n********* Booking Info **********")
    print("1. View Events")
    print("2. Book Tickets")
    print("3. View My Tickets")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        book.view_events()
    elif choice == "2":
        event_name = input("Enter the event name: ")
        quantity = int(input("Enter the number of tickets: "))
        book.book_tickets(event_name, quantity, customer)
    elif choice == "3":
        book.view_tickets(customer)
    elif choice == "4":
        print("Thank you for using the Ticket Booking Application!")
        break
    else:
        print("Invalid choice. Please try again.")
