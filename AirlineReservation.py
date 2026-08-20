from datetime import datetime


class AirlineReservation:

    def __init__(self):

        self.flights = {
            "AI101": {
                "source": "Chennai",
                "destination": "Delhi",
                "travel_date": "2026-09-15",
                "total_seats": 10,
                "available_seats": 10,
                "base_fare": {
                    "Economy": 5000,
                    "Business": 10000,
                    "First": 20000
                }
            },

            "AI202": {
                "source": "Chennai",
                "destination": "Mumbai",
                "travel_date": "2026-09-20",
                "total_seats": 5,
                "available_seats": 5,
                "base_fare": {
                    "Economy": 4000,
                    "Business": 8000,
                    "First": 16000
                }
            }
        }

        self.passengers = {}

        self.next_booking_id = 1001

    # =========================================================
    # FLIGHT SEARCH
    # =========================================================

    def search_flight(
        self,
        source,
        destination,
        travel_date
    ):

        results = []

        for flight_id, flight in self.flights.items():

            if (
                flight["source"].lower() == source.lower()
                and
                flight["destination"].lower()
                == destination.lower()
                and
                flight["travel_date"]
                == travel_date
            ):

                results.append(flight_id)

        return results

    # =========================================================
    # SEAT AVAILABILITY
    # =========================================================

    def check_seat_availability(self, flight_id):

        if flight_id not in self.flights:
            raise ValueError("Invalid flight")

        return self.flights[flight_id]["available_seats"]

    # =========================================================
    # DYNAMIC PRICING
    # =========================================================

    def calculate_fare(
        self,
        flight_id,
        travel_date,
        booking_date,
        passenger_type,
        seat_class
    ):

        if flight_id not in self.flights:
            raise ValueError("Invalid flight")

        flight = self.flights[flight_id]

        if seat_class not in flight["base_fare"]:
            raise ValueError("Invalid class")

        base_fare = flight["base_fare"][seat_class]

        available = flight["available_seats"]
        total = flight["total_seats"]

        fare = base_fare

        # -----------------------------------------------------
        # Seat availability pricing
        # -----------------------------------------------------

        availability_ratio = available / total

        if availability_ratio <= 0.20:

            fare *= 1.50

        elif availability_ratio <= 0.50:

            fare *= 1.25

        else:

            fare *= 1.00

        # -----------------------------------------------------
        # Booking date vs travel date
        # -----------------------------------------------------

        booking = datetime.strptime(
            booking_date,
            "%Y-%m-%d"
        )

        travel = datetime.strptime(
            travel_date,
            "%Y-%m-%d"
        )

        days_before_travel = (
            travel - booking
        ).days

        if days_before_travel <= 3:

            fare *= 1.30

        elif days_before_travel <= 7:

            fare *= 1.15

        elif days_before_travel <= 30:

            fare *= 1.05

        # -----------------------------------------------------
        # Passenger type
        # -----------------------------------------------------

        if passenger_type.lower() == "senior":

            fare *= 0.90

        elif passenger_type.lower() == "student":

            fare *= 0.85

        elif passenger_type.lower() == "child":

            fare *= 0.75

        elif passenger_type.lower() == "adult":

            fare *= 1.00

        else:

            raise ValueError(
                "Invalid passenger type"
            )

        return round(fare, 2)

    # =========================================================
    # BOOKING
    # =========================================================

    def book_passenger(
        self,
        passenger_id,
        passenger_name,
        flight_id,
        travel_date,
        booking_date,
        passenger_type,
        seat_class,
        baggage_kg
    ):

        if not passenger_id or not passenger_name:
            raise ValueError(
                "Invalid passenger"
            )

        if flight_id not in self.flights:
            raise ValueError("Invalid flight")

        flight = self.flights[flight_id]

        if travel_date != flight["travel_date"]:
            raise ValueError(
                "Invalid travel date"
            )

        if flight["available_seats"] <= 0:
            raise ValueError(
                "Flight is fully booked"
            )

        # Prevent double booking
        for booking in self.passengers.values():

            if (
                booking["passenger_id"]
                == passenger_id
                and
                booking["flight_id"]
                == flight_id
                and
                booking["status"]
                == "CONFIRMED"
            ):

                raise ValueError(
                    "Passenger already booked"
                )

        fare = self.calculate_fare(
            flight_id,
            travel_date,
            booking_date,
            passenger_type,
            seat_class
        )

        baggage_charge = self.calculate_baggage_charge(
            baggage_kg,
            seat_class
        )

        total_amount = fare + baggage_charge

        booking_id = self.next_booking_id

        self.next_booking_id += 1

        self.passengers[booking_id] = {
            "passenger_id": passenger_id,
            "passenger_name": passenger_name,
            "flight_id": flight_id,
            "travel_date": travel_date,
            "booking_date": booking_date,
            "passenger_type": passenger_type,
            "seat_class": seat_class,
            "baggage_kg": baggage_kg,
            "fare": fare,
            "baggage_charge": baggage_charge,
            "total_amount": total_amount,
            "status": "CONFIRMED"
        }

        flight["available_seats"] -= 1

        return booking_id

    # =========================================================
    # BAGGAGE CHARGES
    # =========================================================

    def calculate_baggage_charge(
        self,
        baggage_kg,
        seat_class
    ):

        if baggage_kg < 0:
            raise ValueError(
                "Invalid baggage weight"
            )

        free_baggage = {
            "Economy": 15,
            "Business": 30,
            "First": 40
        }

        if seat_class not in free_baggage:
            raise ValueError(
                "Invalid class"
            )

        if baggage_kg <= free_baggage[seat_class]:

            return 0

        excess = (
            baggage_kg
            - free_baggage[seat_class]
        )

        return excess * 500

    # =========================================================
    # CANCELLATION
    # =========================================================

    def cancel_booking(self, booking_id):

        if booking_id not in self.passengers:
            raise ValueError(
                "Invalid booking"
            )

        booking = self.passengers[booking_id]

        if booking["status"] == "CANCELLED":
            raise ValueError(
                "Booking already cancelled"
            )

        refund = self.calculate_refund(
            booking_id
        )

        booking["status"] = "CANCELLED"

        flight_id = booking["flight_id"]

        self.flights[flight_id][
            "available_seats"
        ] += 1

        return refund

    # =========================================================
    # REFUND
    # =========================================================

    def calculate_refund(self, booking_id):

        if booking_id not in self.passengers:
            raise ValueError(
                "Invalid booking"
            )

        booking = self.passengers[booking_id]

        booking_date = datetime.strptime(
            booking["booking_date"],
            "%Y-%m-%d"
        )

        travel_date = datetime.strptime(
            booking["travel_date"],
            "%Y-%m-%d"
        )

        days = (
            travel_date - booking_date
        ).days

        amount = booking["total_amount"]

        if days > 30:

            refund_percentage = 0.90

        elif days >= 7:

            refund_percentage = 0.75

        elif days >= 2:

            refund_percentage = 0.50

        else:

            refund_percentage = 0.20

        return round(
            amount * refund_percentage,
            2
        )


# =============================================================
# MAIN PROGRAM
# =============================================================

def main():

    print("========================================")
    print("       AIRLINE RESERVATION SYSTEM")
    print("========================================")

    airline = AirlineReservation()

    try:

        print("\nFlight Search")

        flights = airline.search_flight(
            "Chennai",
            "Delhi",
            "2026-09-15"
        )

        print("Available Flights:", flights)

        print(
            "\nSeats available on AI101:",
            airline.check_seat_availability("AI101")
        )

        booking_id = airline.book_passenger(
            "P001",
            "Suresh",
            "AI101",
            "2026-09-15",
            "2026-08-20",
            "Adult",
            "Economy",
            20
        )

        print(
            "\nBooking Successful"
        )

        print(
            "Booking ID:",
            booking_id
        )

        booking = airline.passengers[
            booking_id
        ]

        print(
            "Fare:",
            booking["fare"]
        )

        print(
            "Baggage Charge:",
            booking["baggage_charge"]
        )

        print(
            "Total:",
            booking["total_amount"]
        )

        refund = airline.cancel_booking(
            booking_id
        )

        print(
            "\nCancellation Successful"
        )

        print(
            "Refund:",
            refund
        )

    except ValueError as e:

        print(
            "ERROR:",
            e
        )


if __name__ == "__main__":
    main()
