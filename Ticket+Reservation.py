class Flight:
    def __init__(self, flight_number, destination, departure_time, price, capacity, flight_type):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.price = price
        self.capacity = capacity
        self.flight_type = flight_type
        self.reservations = []

    def add_reservation(self, passenger_name):
        if self.is_available():
            self.reservations.append(passenger_name)
            return True
        else:
            return False

    def is_available(self):
        return len(self.reservations) < self.capacity

    def cancel_reservation(self, passenger_name):
        if passenger_name in self.reservations:
            self.reservations.remove(passenger_name)
            return True
        else:
            return False

    def __repr__(self):
        return f"Flight(flight_number={self.flight_number}, destination={self.destination}, departure_time={self.departure_time}, price={self.price}, capacity={self.capacity}, flight_type={self.flight_type})"

class FlightBookingSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def book_flight(self, flight_number, passenger_name):
        for flight in self.flights:
            if flight.flight_number == flight_number and flight.is_available():
                flight.add_reservation(passenger_name)
                return True
        return False

    def get_flight(self, flight_number):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                return flight
        return None

    def cancel_flight(self, flight_number, passenger_name):
        flight = self.get_flight(flight_number)
        if flight:
            return flight.cancel_reservation(passenger_name)
        return False

booking_system = FlightBookingSystem()

# Add flights to the system
flight1 = Flight('AA123', 'New York', '2024-02-01T09:00:00', 150, 200, 'Domestic')
flight2 = Flight('BA456', 'London', '2024-02-05T10:30:00', 250, 300, 'International')
booking_system.add_flight(flight1)
booking_system.add_flight(flight2)

# Book flights for passengers
booking_system.book_flight('AA123', 'Brian Baca')
booking_system.book_flight('AA123', 'Alexi Aldinger')
booking_system.book_flight('BA456', 'Jim Brown')

# Get flight details
flight = booking_system.get_flight('AA123')
print(flight.reservations)  # ['Brian Baca', 'Alexi Aldinger']

# Cancel a reservation
booking_system.cancel_flight('AA123', 'Alexi Aldinger')
print(flight.reservations)  # ['Brian Baca']
