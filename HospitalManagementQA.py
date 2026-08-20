from HospitalManagement import HospitalManagement


passed = 0
failed = 0


def check(test_name, actual, expected):

    global passed, failed

    if abs(actual - expected) < 0.01:

        print(f"{test_name} : PASS")
        passed += 1

    else:

        print(f"{test_name} : FAIL")
        print(f"    Expected : {expected:.2f}")
        print(f"    Actual   : {actual:.2f}")

        failed += 1


def check_boolean(test_name, actual, expected):

    global passed, failed

    if actual == expected:

        print(f"{test_name} : PASS")
        passed += 1

    else:

        print(f"{test_name} : FAIL")
        failed += 1


# ====================================================
# TC01 - NORMAL PATIENT
# ====================================================

def test_normal_patient():

    hospital = HospitalManagement(
        "P001",
        "Patient 1",
        30,
        "Dr. Kumar",
        "General",
        "Normal",
        30,
        [],
        [],
        None
    )

    bill = hospital.calculate_bill()

    check(
        "TC01 Normal Patient",
        bill["consultation_fee"],
        500
    )


# ====================================================
# TC02 - EMERGENCY PATIENT
# ====================================================

def test_emergency_patient():

    hospital = HospitalManagement(
        "P002",
        "Patient 2",
        30,
        "Dr. Kumar",
        "General",
        "Emergency",
        30,
        [],
        [],
        None
    )

    bill = hospital.calculate_bill()

    check(
        "TC02 Emergency Patient",
        bill["consultation_fee"],
        750
    )


# ====================================================
# TC03 - SENIOR CITIZEN
# ====================================================

def test_senior_citizen():

    hospital = HospitalManagement(
        "P003",
        "Patient 3",
        60,
        "Dr. Kumar",
        "General",
        "Normal",
        30,
        [],
        [],
        None
    )

    bill = hospital.calculate_bill()

    check(
        "TC03 Senior Citizen",
        bill["consultation_fee"],
        400
    )


# ====================================================
# TC04 - FOLLOW-UP
# ====================================================

def test_follow_up():

    hospital = HospitalManagement(
        "P004",
        "Patient 4",
        30,
        "Dr. Kumar",
        "General",
        "Follow-up",
        30,
        [],
        [],
        None
    )

    bill = hospital.calculate_bill()

    check(
        "TC04 Follow-up Consultation",
        bill["consultation_fee"],
        250
    )


# ====================================================
# TC05 - CARDIOLOGY
# ====================================================

def test_cardiology():

    hospital = HospitalManagement(
        "P005",
        "Patient 5",
        30,
        "Dr. Kumar",
        "Cardiology",
        "Normal",
        30,
        [],
        [],
        None
    )

    bill = hospital.calculate_bill()

    check(
        "TC05 Cardiology Consultation",
        bill["consultation_fee"],
        1000
    )


# ====================================================
# TC06 - NEUROLOGY
# ====================================================

def test_neurology():

    hospital = HospitalManagement(
        "P006",
        "Patient 6",
        30,
        "Dr. Kumar",
        "Neurology",
        "Normal",
        30,
        [],
        [],
        None
    )

    bill = hospital.calculate_bill()

    check(
        "TC06 Neurology Consultation",
        bill["consultation_fee"],
        1200
    )


# ====================================================
# TC07 - LAB TEST
# ====================================================

def test_lab_charge():

    hospital = HospitalManagement(
        "P007",
        "Patient 7",
        30,
        "Dr. Kumar",
        "General",
        "Normal",
        30,
        ["Blood Test"],
        [],
        None
    )

    bill = hospital.calculate_bill()

    check(
        "TC07 Blood Test Charge",
        bill["lab_charges"],
        300
    )


# ====================================================
# TC08 - MULTIPLE LAB TESTS
# ====================================================

def test_multiple_lab_tests():

    hospital = HospitalManagement(
        "P008",
        "Patient 8",
        30,
        "Dr. Kumar",
        "General",
        "Normal",
        30,
        ["Blood Test", "X-Ray"],
        [],
        None
    )

    bill = hospital.calculate_bill()

    check(
        "TC08 Multiple Lab Tests",
        bill["lab_charges"],
        800
    )


# ====================================================
# TC09 - MEDICINE CHARGE
# ====================================================

def test_medicine_charge():

    hospital = HospitalManagement(
        "P009",
        "Patient 9",
        30,
        "Dr. Kumar",
        "General",
        "Normal",
        30,
        [],
        ["Paracetamol"],
        None
    )

    bill = hospital.calculate_bill()

    check(
        "TC09 Medicine Charge",
        bill["medicine_charges"],
        50
    )


# ====================================================
# TC10 - MULTIPLE MEDICINES
# ====================================================

def test_multiple_medicines():

    hospital = HospitalManagement(
        "P010",
        "Patient 10",
        30,
        "Dr. Kumar",
        "General",
        "Normal",
        30,
        [],
        ["Paracetamol", "Antibiotic"],
        None
    )

    bill = hospital.calculate_bill()

    check(
        "TC10 Multiple Medicines",
        bill["medicine_charges"],
        200
    )


# ====================================================
# TC11 - BASIC INSURANCE
# ====================================================

def test_basic_insurance():

    hospital = HospitalManagement(
        "P011",
        "Patient 11",
        30,
        "Dr. Kumar",
        "General",
        "Normal",
        30,
        [],
        [],
        "Basic"
    )

    bill = hospital.calculate_bill()

    check(
        "TC11 Basic Insurance",
        bill["insurance_coverage"],
        250
    )


# ====================================================
# TC12 - PREMIUM INSURANCE
# ====================================================

def test_premium_insurance():

    hospital = HospitalManagement(
        "P012",
        "Patient 12",
        30,
        "Dr. Kumar",
        "General",
        "Normal",
        30,
        [],
        [],
        "Premium"
    )

    bill = hospital.calculate_bill()

    check(
        "TC12 Premium Insurance",
        bill["insurance_coverage"],
        400
    )


# ====================================================
# TC13 - GOVERNMENT INSURANCE
# ====================================================

def test_government_insurance():

    hospital = HospitalManagement(
        "P013",
        "Patient 13",
        30,
        "Dr. Kumar",
        "General",
        "Normal",
        30,
        [],
        [],
        "Government"
    )

    bill = hospital.calculate_bill()

    check(
        "TC13 Government Insurance",
        bill["insurance_coverage"],
        350
    )


# ====================================================
# TC14 - NO INSURANCE
# ====================================================

def test_no_insurance():

    hospital = HospitalManagement(
        "P014",
        "Patient 14",
        30,
        "Dr. Kumar",
        "General",
        "Normal",
        30,
        [],
        [],
        None
    )

    bill = hospital.calculate_bill()

    check(
        "TC14 No Insurance",
        bill["insurance_coverage"],
        0
    )


# ====================================================
# TC15 - LONG CONSULTATION
# ====================================================

def test_long_consultation():

    hospital = HospitalManagement(
        "P015",
        "Patient 15",
        30,
        "Dr. Kumar",
        "General",
        "Normal",
        60,
        [],
        [],
        None
    )

    bill = hospital.calculate_bill()

    check(
        "TC15 Long Consultation",
        bill["consultation_fee"],
        800
    )


# ====================================================
# TC16 - EMERGENCY SENIOR
# ====================================================

def test_emergency_senior():

    hospital = HospitalManagement(
        "P016",
        "Patient 16",
        65,
        "Dr. Kumar",
        "General",
        "Emergency",
        30,
        [],
        [],
        None
    )

    bill = hospital.calculate_bill()

    check(
        "TC16 Emergency Senior Patient",
        bill["consultation_fee"],
        600
    )


# ====================================================
# TC17 - INVALID DEPARTMENT
# ====================================================

def test_invalid_department():

    hospital = HospitalManagement(
        "P017",
        "Patient 17",
        30,
        "Dr. Kumar",
        "Unknown",
        "Normal",
        30,
        [],
        [],
        None
    )

    try:

        hospital.calculate_bill()

        check_boolean(
            "TC17 Invalid Department",
            False,
            True
        )

    except ValueError:

        check_boolean(
            "TC17 Invalid Department",
            True,
            True
        )


# ====================================================
# TC18 - INVALID LAB TEST
# ====================================================

def test_invalid_lab():

    hospital = HospitalManagement(
        "P018",
        "Patient 18",
        30,
        "Dr. Kumar",
        "General",
        "Normal",
        30,
        ["Invalid Test"],
        [],
        None
    )

    try:

        hospital.calculate_bill()

        check_boolean(
            "TC18 Invalid Lab Test",
            False,
            True
        )

    except ValueError:

        check_boolean(
            "TC18 Invalid Lab Test",
            True,
            True
        )


# ====================================================
# TC19 - INVALID MEDICINE
# ====================================================

def test_invalid_medicine():

    hospital = HospitalManagement(
        "P019",
        "Patient 19",
        30,
        "Dr. Kumar",
        "General",
        "Normal",
        30,
        [],
        ["Invalid Medicine"],
        None
    )

    try:

        hospital.calculate_bill()

        check_boolean(
            "TC19 Invalid Medicine",
            False,
            True
        )

    except ValueError:

        check_boolean(
            "TC19 Invalid Medicine",
            True,
            True
        )


# ====================================================
# TC20 - COMPLETE BILL
# ====================================================

def test_complete_bill():

    hospital = HospitalManagement(
        "P020",
        "Patient 20",
        65,
        "Dr. Kumar",
        "Cardiology",
        "Emergency",
        45,
        ["Blood Test", "X-Ray"],
        ["Paracetamol", "Antibiotic"],
        "Premium"
    )

    bill = hospital.calculate_bill()

    result = (
        bill["consultation_fee"] > 0
        and bill["lab_charges"] > 0
        and bill["medicine_charges"] > 0
        and bill["insurance_coverage"] > 0
        and bill["patient_payable"] > 0
    )

    check_boolean(
        "TC20 Complete Hospital Bill",
        result,
        True
    )


# ====================================================
# RUN ALL TESTS
# ====================================================

def main():

    print("========================================")
    print("       HOSPITAL MANAGEMENT QA")
    print("========================================")
    print()

    test_normal_patient()
    test_emergency_patient()
    test_senior_citizen()
    test_follow_up()
    test_cardiology()
    test_neurology()
    test_lab_charge()
    test_multiple_lab_tests()
    test_medicine_charge()
    test_multiple_medicines()
    test_basic_insurance()
    test_premium_insurance()
    test_government_insurance()
    test_no_insurance()
    test_long_consultation()
    test_emergency_senior()
    test_invalid_department()
    test_invalid_lab()
    test_invalid_medicine()
    test_complete_bill()

    print()
    print("========================================")
    print("              QA SUMMARY")
    print("========================================")

    print(f"TOTAL TESTS : {passed + failed}")
    print(f"PASSED      : {passed}")
    print(f"FAILED      : {failed}")

    if failed == 0:
        print("RESULT      : ALL TESTS PASSED")
    else:
        print("RESULT      : SOME TESTS FAILED")

    print("========================================")

    # Jenkins fails if any test fails
    if failed > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
