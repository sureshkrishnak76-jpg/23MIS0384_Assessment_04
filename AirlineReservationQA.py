from AirlineReservation import AirlineReservation


passed = 0
failed = 0


def test_result(name, condition):

    global passed, failed

    if condition:

        print(f"{name} : PASS")
        passed += 1

    else:

        print(f"{name} : FAIL")
        failed += 1


def exception_test(name, function):

    global passed, failed

    try:

        function()

        print(f"{name} : FAIL")
        failed += 1

    except ValueError:

        print(f"{name} : PASS")
        passed += 1


# =========================================================
# TC01 - SUCCESSFUL BOOKING
# =========================================================

def test_successful_booking():

    airline = AirlineReservation()

    booking_id = airline.book_passenger(
        "P001",
        "Suresh",
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Adult",
        "Economy",
        10
    )

    test_result(
        "TC01 Successful Booking",
        booking_id in airline.passengers
    )


# =========================================================
# TC02 - DOUBLE BOOKING
# =========================================================

def test_double_booking():

    airline = AirlineReservation()

    airline.book_passenger(
        "P002",
        "Rahul",
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Adult",
        "Economy",
        10
    )

    exception_test(
        "TC02 Double Booking",
        lambda: airline.book_passenger(
            "P002",
            "Rahul",
            "AI101",
            "2026-09-15",
            "2026-08-20",
            "Adult",
            "Economy",
            10
        )
    )


# =========================================================
# TC03 - CANCELLATION
# =========================================================

def test_cancellation():

    airline = AirlineReservation()

    booking_id = airline.book_passenger(
        "P003",
        "Arun",
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Adult",
        "Economy",
        10
    )

    refund = airline.cancel_booking(
        booking_id
    )

    test_result(
        "TC03 Cancellation",
        airline.passengers[
            booking_id
        ]["status"] == "CANCELLED"
    )


# =========================================================
# TC04 - REFUND
# =========================================================

def test_refund():

    airline = AirlineReservation()

    booking_id = airline.book_passenger(
        "P004",
        "Kumar",
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Adult",
        "Economy",
        10
    )

    refund = airline.calculate_refund(
        booking_id
    )

    test_result(
        "TC04 Refund Calculation",
        refund > 0
    )


# =========================================================
# TC05 - FULLY BOOKED FLIGHT
# =========================================================

def test_fully_booked():

    airline = AirlineReservation()

    for i in range(10):

        airline.book_passenger(
            f"P{i}",
            f"Passenger{i}",
            "AI101",
            "2026-09-15",
            "2026-08-20",
            "Adult",
            "Economy",
            10
        )

    exception_test(
        "TC05 Fully Booked Flight",
        lambda: airline.book_passenger(
            "P999",
            "Extra Passenger",
            "AI101",
            "2026-09-15",
            "2026-08-20",
            "Adult",
            "Economy",
            10
        )
    )


# =========================================================
# TC06 - INVALID PASSENGER
# =========================================================

def test_invalid_passenger():

    airline = AirlineReservation()

    exception_test(
        "TC06 Invalid Passenger",
        lambda: airline.book_passenger(
            "",
            "",
            "AI101",
            "2026-09-15",
            "2026-08-20",
            "Adult",
            "Economy",
            10
        )
    )


# =========================================================
# TC07 - EXCESS BAGGAGE
# =========================================================

def test_excess_baggage():

    airline = AirlineReservation()

    charge = airline.calculate_baggage_charge(
        25,
        "Economy"
    )

    test_result(
        "TC07 Excess Baggage",
        charge == 5000
    )


# =========================================================
# TC08 - DYNAMIC FARE
# =========================================================

def test_dynamic_fare():

    airline = AirlineReservation()

    normal_fare = airline.calculate_fare(
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Adult",
        "Economy"
    )

    # Reduce available seats
    airline.flights["AI101"][
        "available_seats"
    ] = 2

    high_demand_fare = airline.calculate_fare(
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Adult",
        "Economy"
    )

    test_result(
        "TC08 Dynamic Fare Calculation",
        high_demand_fare > normal_fare
    )


# =========================================================
# TC09 - BUSINESS CLASS
# =========================================================

def test_business_class():

    airline = AirlineReservation()

    fare = airline.calculate_fare(
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Adult",
        "Business"
    )

    test_result(
        "TC09 Business Class Fare",
        fare > 5000
    )


# =========================================================
# TC10 - FIRST CLASS
# =========================================================

def test_first_class():

    airline = AirlineReservation()

    fare = airline.calculate_fare(
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Adult",
        "First"
    )

    test_result(
        "TC10 First Class Fare",
        fare > 10000
    )


# =========================================================
# TC11 - SENIOR PASSENGER
# =========================================================

def test_senior_passenger():

    airline = AirlineReservation()

    adult_fare = airline.calculate_fare(
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Adult",
        "Economy"
    )

    senior_fare = airline.calculate_fare(
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Senior",
        "Economy"
    )

    test_result(
        "TC11 Senior Passenger Discount",
        senior_fare < adult_fare
    )


# =========================================================
# TC12 - STUDENT PASSENGER
# =========================================================

def test_student_passenger():

    airline = AirlineReservation()

    adult_fare = airline.calculate_fare(
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Adult",
        "Economy"
    )

    student_fare = airline.calculate_fare(
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Student",
        "Economy"
    )

    test_result(
        "TC12 Student Passenger Discount",
        student_fare < adult_fare
    )


# =========================================================
# TC13 - CHILD PASSENGER
# =========================================================

def test_child_passenger():

    airline = AirlineReservation()

    adult_fare = airline.calculate_fare(
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Adult",
        "Economy"
    )

    child_fare = airline.calculate_fare(
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Child",
        "Economy"
    )

    test_result(
        "TC13 Child Passenger Discount",
        child_fare < adult_fare
    )


# =========================================================
# TC14 - FLIGHT SEARCH
# =========================================================

def test_flight_search():

    airline = AirlineReservation()

    flights = airline.search_flight(
        "Chennai",
        "Delhi",
        "2026-09-15"
    )

    test_result(
        "TC14 Flight Search",
        "AI101" in flights
    )


# =========================================================
# TC15 - INVALID FLIGHT
# =========================================================

def test_invalid_flight():

    airline = AirlineReservation()

    exception_test(
        "TC15 Invalid Flight",
        lambda: airline.check_seat_availability(
            "INVALID"
        )
    )


# =========================================================
# TC16 - INVALID CLASS
# =========================================================

def test_invalid_class():

    airline = AirlineReservation()

    exception_test(
        "TC16 Invalid Class",
        lambda: airline.calculate_fare(
            "AI101",
            "2026-09-15",
            "2026-08-20",
            "Adult",
            "Premium"
        )
    )


# =========================================================
# TC17 - NEGATIVE BAGGAGE
# =========================================================

def test_negative_baggage():

    airline = AirlineReservation()

    exception_test(
        "TC17 Negative Baggage",
        lambda: airline.calculate_baggage_charge(
            -10,
            "Economy"
        )
    )


# =========================================================
# TC18 - FREE BAGGAGE
# =========================================================

def test_free_baggage():

    airline = AirlineReservation()

    charge = airline.calculate_baggage_charge(
        15,
        "Economy"
    )

    test_result(
        "TC18 Free Baggage Limit",
        charge == 0
    )


# =========================================================
# TC19 - BUSINESS BAGGAGE
# =========================================================

def test_business_baggage():

    airline = AirlineReservation()

    charge = airline.calculate_baggage_charge(
        35,
        "Business"
    )

    test_result(
        "TC19 Business Excess Baggage",
        charge == 2500
    )


# =========================================================
# TC20 - CANCELLATION REFUND
# =========================================================

def test_cancellation_refund():

    airline = AirlineReservation()

    booking_id = airline.book_passenger(
        "P020",
        "Passenger 20",
        "AI101",
        "2026-09-15",
        "2026-08-20",
        "Adult",
        "Economy",
        10
    )

    original_amount = airline.passengers[
        booking_id
    ]["total_amount"]

    refund = airline.cancel_booking(
        booking_id
    )

    test_result(
        "TC20 Cancellation Refund",
        refund > 0
        and refund < original_amount
    )


# =========================================================
# MAIN
# =========================================================

def main():

    print("========================================")
    print("       AIRLINE RESERVATION QA")
    print("========================================")
    print()

    test_successful_booking()
    test_double_booking()
    test_cancellation()
    test_refund()
    test_fully_booked()
    test_invalid_passenger()
    test_excess_baggage()
    test_dynamic_fare()
    test_business_class()
    test_first_class()
    test_senior_passenger()
    test_student_passenger()
    test_child_passenger()
    test_flight_search()
    test_invalid_flight()
    test_invalid_class()
    test_negative_baggage()
    test_free_baggage()
    test_business_baggage()
    test_cancellation_refund()

    print()
    print("========================================")
    print("             QA SUMMARY")
    print("========================================")

    print(f"TOTAL TESTS : {passed + failed}")
    print(f"PASSED      : {passed}")
    print(f"FAILED      : {failed}")

    if failed == 0:

        print("RESULT      : ALL TESTS PASSED")

    else:

        print("RESULT      : SOME TESTS FAILED")

    print("========================================")

    if failed > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
