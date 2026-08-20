class HospitalManagement:

    # Consultation fees based on department
    DEPARTMENT_FEES = {
        "Cardiology": 1000,
        "Neurology": 1200,
        "Orthopedics": 800,
        "General": 500,
        "Pediatrics": 600
    }

    # Lab test charges
    LAB_CHARGES = {
        "Blood Test": 300,
        "Urine Test": 200,
        "X-Ray": 500,
        "CT Scan": 2500,
        "MRI": 5000
    }

    # Medicine prices
    MEDICINE_PRICES = {
        "Paracetamol": 50,
        "Antibiotic": 150,
        "Painkiller": 100,
        "Vitamin": 80,
        "Cough Syrup": 120
    }

    def __init__(
        self,
        patient_id,
        patient_name,
        age,
        doctor,
        department,
        appointment_type,
        duration,
        lab_tests,
        medicines,
        insurance
    ):

        self.patient_id = patient_id
        self.patient_name = patient_name
        self.age = age
        self.doctor = doctor
        self.department = department
        self.appointment_type = appointment_type
        self.duration = duration
        self.lab_tests = lab_tests
        self.medicines = medicines
        self.insurance = insurance

    # ------------------------------------------------
    # Consultation Fee
    # ------------------------------------------------

    def calculate_consultation_fee(self):

        if self.department not in self.DEPARTMENT_FEES:
            raise ValueError("Invalid department")

        base_fee = self.DEPARTMENT_FEES[self.department]

        # Emergency charge = 50%
        if self.appointment_type.lower() == "emergency":
            base_fee = base_fee * 1.50

        # Follow-up = 50% of normal consultation fee
        elif self.appointment_type.lower() == "follow-up":
            base_fee = base_fee * 0.50

        # Senior citizen discount = 20%
        if self.age >= 60:
            base_fee = base_fee * 0.80

        # Additional duration charge
        if self.duration > 30:
            extra_minutes = self.duration - 30
            base_fee += extra_minutes * 10

        return base_fee

    # ------------------------------------------------
    # Lab Charges
    # ------------------------------------------------

    def calculate_lab_charges(self):

        total = 0

        for test in self.lab_tests:

            if test not in self.LAB_CHARGES:
                raise ValueError(
                    f"Invalid lab test: {test}"
                )

            total += self.LAB_CHARGES[test]

        return total

    # ------------------------------------------------
    # Medicine Charges
    # ------------------------------------------------

    def calculate_medicine_charges(self):

        total = 0

        for medicine in self.medicines:

            if medicine not in self.MEDICINE_PRICES:
                raise ValueError(
                    f"Invalid medicine: {medicine}"
                )

            total += self.MEDICINE_PRICES[medicine]

        return total

    # ------------------------------------------------
    # Insurance Coverage
    # ------------------------------------------------

    def calculate_insurance_coverage(self, total):

        if not self.insurance:
            return 0

        coverage_type = self.insurance.lower()

        if coverage_type == "basic":
            coverage = total * 0.50

        elif coverage_type == "premium":
            coverage = total * 0.80

        elif coverage_type == "government":
            coverage = total * 0.70

        else:
            raise ValueError("Invalid insurance type")

        return coverage

    # ------------------------------------------------
    # Final Bill
    # ------------------------------------------------

    def calculate_bill(self):

        consultation = self.calculate_consultation_fee()

        lab = self.calculate_lab_charges()

        medicines = self.calculate_medicine_charges()

        total = consultation + lab + medicines

        insurance_coverage = self.calculate_insurance_coverage(
            total
        )

        payable = total - insurance_coverage

        return {
            "consultation_fee": consultation,
            "lab_charges": lab,
            "medicine_charges": medicines,
            "total_bill": total,
            "insurance_coverage": insurance_coverage,
            "patient_payable": payable
        }


# ====================================================
# MAIN PROGRAM
# ====================================================

def main():

    print("========================================")
    print("       HOSPITAL APPOINTMENT & BILLING")
    print("========================================")

    try:

        patient_id = input("Patient ID: ")
        patient_name = input("Patient Name: ")

        age = int(input("Age: "))

        doctor = input("Doctor: ")
        department = input("Department: ")

        appointment_type = input(
            "Appointment Type "
            "(Normal/Emergency/Follow-up): "
        )

        duration = int(
            input("Consultation Duration (minutes): ")
        )

        lab_input = input(
            "Lab Tests (comma separated): "
        )

        if lab_input.strip():
            lab_tests = [
                x.strip()
                for x in lab_input.split(",")
            ]
        else:
            lab_tests = []

        medicine_input = input(
            "Medicines (comma separated): "
        )

        if medicine_input.strip():
            medicines = [
                x.strip()
                for x in medicine_input.split(",")
            ]
        else:
            medicines = []

        insurance = input(
            "Insurance "
            "(None/Basic/Premium/Government): "
        )

        if insurance.lower() == "none":
            insurance = None

        hospital = HospitalManagement(
            patient_id,
            patient_name,
            age,
            doctor,
            department,
            appointment_type,
            duration,
            lab_tests,
            medicines,
            insurance
        )

        bill = hospital.calculate_bill()

        print()
        print("========================================")
        print("              BILL DETAILS")
        print("========================================")

        print(
            f"Patient ID          : {patient_id}"
        )

        print(
            f"Patient Name        : {patient_name}"
        )

        print(
            f"Doctor              : {doctor}"
        )

        print(
            f"Department          : {department}"
        )

        print(
            f"Appointment Type    : {appointment_type}"
        )

        print("----------------------------------------")

        print(
            f"Consultation Fee    : "
            f"{bill['consultation_fee']:.2f}"
        )

        print(
            f"Lab Charges         : "
            f"{bill['lab_charges']:.2f}"
        )

        print(
            f"Medicine Charges    : "
            f"{bill['medicine_charges']:.2f}"
        )

        print(
            f"Total Bill          : "
            f"{bill['total_bill']:.2f}"
        )

        print(
            f"Insurance Coverage  : "
            f"{bill['insurance_coverage']:.2f}"
        )

        print(
            f"Patient Payable     : "
            f"{bill['patient_payable']:.2f}"
        )

        print("========================================")

    except ValueError as e:

        print("ERROR:", e)

    except Exception as e:

        print("UNEXPECTED ERROR:", e)


if __name__ == "__main__":
    main()
