from ParkingManagement import ParkingManagement


passed = 0
failed = 0


# =========================================================
# TEST RESULT
# =========================================================

def test_result(
    test_name,
    condition
):

    global passed
    global failed

    if condition:

        print(
            f"{test_name} : PASS"
        )

        passed += 1

    else:

        print(
            f"{test_name} : FAIL"
        )

        failed += 1


# =========================================================
# EXCEPTION TEST
# =========================================================

def exception_test(
    test_name,
    function
):

    global passed
    global failed

    try:

        function()

        print(
            f"{test_name} : FAIL"
        )

        failed += 1

    except ValueError:

        print(
            f"{test_name} : PASS"
        )

        passed += 1


# =========================================================
# TC01 - VEHICLE ENTRY
# =========================================================

def test_vehicle_entry():

    parking = ParkingManagement()

    ticket = parking.vehicle_entry(
        "TN01AA1111",
        "Car",
        "2026-08-20 10:00"
    )

    test_result(
        "TC01 Vehicle Entry",
        ticket["slot"] in [
            "C1",
            "C2"
        ]
    )


# =========================================================
# TC02 - AUTOMATIC SLOT ALLOCATION
# =========================================================

def test_automatic_slot():

    parking = ParkingManagement()

    ticket = parking.vehicle_entry(
        "TN02BB2222",
        "Bike",
        "2026-08-20 10:00"
    )

    test_result(
        "TC02 Automatic Slot Allocation",
        ticket["slot"] in [
            "B1",
            "B2"
        ]
    )


# =========================================================
# TC03 - WRONG VEHICLE SLOT COMBINATION
# =========================================================

def test_wrong_vehicle_slot():

    parking = ParkingManagement()

    # Occupy both car slots
    parking.vehicle_entry(
        "CAR001",
        "Car",
        "2026-08-20 10:00"
    )

    parking.vehicle_entry(
        "CAR002",
        "Car",
        "2026-08-20 10:00"
    )

    # Third car cannot use SUV/Bike/Truck slot
    exception_test(
        "TC03 Wrong Vehicle-Slot Combination",
        lambda: parking.vehicle_entry(
            "CAR003",
            "Car",
            "2026-08-20 10:00"
        )
    )


# =========================================================
# TC04 - DUPLICATE VEHICLE
# =========================================================

def test_duplicate_vehicle():

    parking = ParkingManagement()

    parking.vehicle_entry(
        "DUP001",
        "Car",
        "2026-08-20 10:00"
    )

    exception_test(
        "TC04 Duplicate Vehicle",
        lambda: parking.vehicle_entry(
            "DUP001",
            "Car",
            "2026-08-20 11:00"
        )
    )


# =========================================================
# TC05 - LOST TICKET
# =========================================================

def test_lost_ticket():

    parking = ParkingManagement()

    parking.vehicle_entry(
        "LOST001",
        "Car",
        "2026-08-20 10:00"
    )

    fee = parking.vehicle_exit(
        "LOST001",
        "2026-08-20 13:00",
        True
    )

    test_result(
        "TC05 Lost Ticket",
        fee == 500
    )


# =========================================================
# TC06 - EARLY EXIT
# =========================================================

def test_early_exit():

    parking = ParkingManagement()

    parking.vehicle_entry(
        "EARLY001",
        "Car",
        "2026-08-20 10:00"
    )

    fee = parking.vehicle_exit(
        "EARLY001",
        "2026-08-20 10:15"
    )

    # Minimum one hour
    test_result(
        "TC06 Early Exit",
        fee == 50
    )


# =========================================================
# TC07 - OVERNIGHT PARKING
# =========================================================

def test_overnight():

    parking = ParkingManagement()

    parking.vehicle_entry(
        "NIGHT001",
        "Car",
        "2026-08-20 10:00"
    )

    fee = parking.vehicle_exit(
        "NIGHT001",
        "2026-08-21 10:00"
    )

    # 24 hours × Rs.50
    test_result(
        "TC07 Overnight Parking",
        fee == 1200
    )


# =========================================================
# TC08 - PEAK HOUR PRICING
# =========================================================

def test_peak_hour():

    parking = ParkingManagement()

    parking.vehicle_entry(
        "PEAK001",
        "Car",
        "2026-08-20 10:00"
    )

    normal_fee = parking.calculate_fee(
        "Car",
        "2026-08-20 10:00",
        "2026-08-20 13:00"
    )

    peak_fee = parking.calculate_fee(
        "Car",
        "2026-08-20 10:00",
        "2026-08-20 18:00"
    )

    test_result(
        "TC08 Peak Hour Pricing",
        peak_fee > normal_fee
    )


# =========================================================
# TC09 - EV CHARGING FEE
# =========================================================

def test_ev_charging():

    parking = ParkingManagement()

    # EV has dedicated slot
    ticket = parking.vehicle_entry(
        "EV001",
        "Electric Vehicle",
        "2026-08-20 10:00"
    )

    test_result(
        "TC09 EV Slot Allocation",
        ticket["slot"] == "E1"
    )


# =========================================================
# TC10 - FULL PARKING LOT
# =========================================================

def test_full_parking():

    parking = ParkingManagement()

    parking.vehicle_entry(
        "BIKE001",
        "Bike",
        "2026-08-20 10:00"
    )

    parking.vehicle_entry(
        "BIKE002",
        "Bike",
        "2026-08-20 10:00"
    )

    parking.vehicle_entry(
        "CAR001",
        "Car",
        "2026-08-20 10:00"
    )

    parking.vehicle_entry(
        "CAR002",
        "Car",
        "2026-08-20 10:00"
    )

    parking.vehicle_entry(
        "SUV001",
        "SUV",
        "2026-08-20 10:00"
    )

    parking.vehicle_entry(
        "TRUCK001",
        "Truck",
        "2026-08-20 10:00"
    )

    parking.vehicle_entry(
        "EV001",
        "Electric Vehicle",
        "2026-08-20 10:00"
    )

    parking.vehicle_entry(
        "VIP001",
        "Car",
        "2026-08-20 10:00",
        True
    )

    # Now all slots are occupied
    exception_test(
        "TC10 Full Parking Lot",
        lambda: parking.vehicle_entry(
            "EXTRA001",
            "Car",
            "2026-08-20 10:00"
        )
    )


# =========================================================
# TC11 - VIP PARKING
# =========================================================

def test_vip():

    parking = ParkingManagement()

    ticket = parking.vehicle_entry(
        "VIP001",
        "Car",
        "2026-08-20 10:00",
        True
    )

    test_result(
        "TC11 VIP Parking",
        ticket["slot"] == "VIP1"
    )


# =========================================================
# TC12 - VIP PRICING
# =========================================================

def test_vip_pricing():

    parking = ParkingManagement()

    normal_fee = parking.calculate_fee(
        "Car",
        "2026-08-20 10:00",
        "2026-08-20 13:00"
    )

    vip_fee = parking.calculate_fee(
        "Car",
        "2026-08-20 10:00",
        "2026-08-20 13:00",
        True
    )

    test_result(
        "TC12 VIP Pricing",
        vip_fee > normal_fee
    )


# =========================================================
# TC13 - SUV SLOT
# =========================================================

def test_suv_slot():

    parking = ParkingManagement()

    ticket = parking.vehicle_entry(
        "SUV001",
        "SUV",
        "2026-08-20 10:00"
    )

    test_result(
        "TC13 SUV Slot Allocation",
        ticket["slot"] == "S1"
    )


# =========================================================
# TC14 - TRUCK SLOT
# =========================================================

def test_truck_slot():

    parking = ParkingManagement()

    ticket = parking.vehicle_entry(
        "TRUCK001",
        "Truck",
        "2026-08-20 10:00"
    )

    test_result(
        "TC14 Truck Slot Allocation",
        ticket["slot"] == "T1"
    )


# =========================================================
# TC15 - EV WRONG SLOT
# =========================================================

def test_ev_slot():

    parking = ParkingManagement()

    ticket = parking.vehicle_entry(
        "EV001",
        "Electric Vehicle",
        "2026-08-20 10:00"
    )

    test_result(
        "TC15 EV Dedicated Slot",
        ticket["slot"] == "E1"
    )


# =========================================================
# TC16 - INVALID VEHICLE
# =========================================================

def test_invalid_vehicle():

    parking = ParkingManagement()

    exception_test(
        "TC16 Invalid Vehicle Type",
        lambda: parking.vehicle_entry(
            "INVALID001",
            "Bus",
            "2026-08-20 10:00"
        )
    )


# =========================================================
# TC17 - INVALID EXIT
# =========================================================

def test_invalid_exit():

    parking = ParkingManagement()

    exception_test(
        "TC17 Invalid Vehicle Exit",
        lambda: parking.vehicle_exit(
            "NOTFOUND",
            "2026-08-20 12:00"
        )
    )


# =========================================================
# TC18 - EXIT BEFORE ENTRY
# =========================================================

def test_exit_before_entry():

    parking = ParkingManagement()

    parking.vehicle_entry(
        "TIME001",
        "Car",
        "2026-08-20 10:00"
    )

    exception_test(
        "TC18 Exit Before Entry",
        lambda: parking.vehicle_exit(
            "TIME001",
            "2026-08-20 09:00"
        )
    )


# =========================================================
# TC19 - NORMAL PARKING FEE
# =========================================================

def test_normal_fee():

    parking = ParkingManagement()

    parking.vehicle_entry(
        "FEE001",
        "Car",
        "2026-08-20 10:00"
    )

    fee = parking.vehicle_exit(
        "FEE001",
        "2026-08-20 13:00"
    )

    test_result(
        "TC19 Normal Parking Fee",
        fee == 150
    )


# =========================================================
# TC20 - SLOT RELEASE AFTER EXIT
# =========================================================

def test_slot_release():

    parking = ParkingManagement()

    ticket = parking.vehicle_entry(
        "RELEASE001",
        "Car",
        "2026-08-20 10:00"
    )

    slot = ticket["slot"]

    parking.vehicle_exit(
        "RELEASE001",
        "2026-08-20 12:00"
    )

    test_result(
        "TC20 Slot Release After Exit",
        slot not in parking.occupied
    )


# =========================================================
# MAIN
# =========================================================

def main():

    print("========================================")
    print("       SMART PARKING QA")
    print("========================================")
    print()

    test_vehicle_entry()
    test_automatic_slot()
    test_wrong_vehicle_slot()
    test_duplicate_vehicle()
    test_lost_ticket()
    test_early_exit()
    test_overnight()
    test_peak_hour()
    test_ev_charging()
    test_full_parking()
    test_vip()
    test_vip_pricing()
    test_suv_slot()
    test_truck_slot()
    test_ev_slot()
    test_invalid_vehicle()
    test_invalid_exit()
    test_exit_before_entry()
    test_normal_fee()
    test_slot_release()

    print()
    print("========================================")
    print("             QA SUMMARY")
    print("========================================")

    print(
        f"TOTAL TESTS : {passed + failed}"
    )

    print(
        f"PASSED      : {passed}"
    )

    print(
        f"FAILED      : {failed}"
    )

    if failed == 0:

        print(
            "RESULT      : ALL TESTS PASSED"
        )

    else:

        print(
            "RESULT      : SOME TESTS FAILED"
        )

    print(
        "========================================"
    )

    # Jenkins should fail if any QA test fails
    if failed > 0:

        raise SystemExit(1)


if __name__ == "__main__":

    main()
