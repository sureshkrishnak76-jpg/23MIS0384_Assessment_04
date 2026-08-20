from datetime import datetime


class ParkingManagement:

    # =========================================================
    # PARKING MANAGEMENT SYSTEM
    # =========================================================

    def __init__(self):

        # Slot format:
        # slot_id : slot_type

        self.slots = {
            "B1": "Bike",
            "B2": "Bike",

            "C1": "Car",
            "C2": "Car",

            "S1": "SUV",

            "T1": "Truck",

            "E1": "Electric Vehicle",

            "VIP1": "VIP"
        }

        # Currently occupied slots
        self.occupied = {}

        # Vehicle -> parking ticket
        self.tickets = {}

        self.next_ticket = 1001

        # Base hourly rates
        self.base_rates = {
            "Bike": 30,
            "Car": 50,
            "SUV": 70,
            "Truck": 100,
            "Electric Vehicle": 50
        }

    # =========================================================
    # VEHICLE VALIDATION
    # =========================================================

    def validate_vehicle_type(self, vehicle_type):

        valid_types = [
            "Bike",
            "Car",
            "SUV",
            "Truck",
            "Electric Vehicle"
        ]

        if vehicle_type not in valid_types:

            raise ValueError(
                "Invalid vehicle type"
            )

    # =========================================================
    # SLOT COMPATIBILITY
    # =========================================================

    def is_compatible(self, slot_type, vehicle_type):

        # VIP slot can accept any vehicle
        if slot_type == "VIP":

            return True

        # EV must use EV slot
        if vehicle_type == "Electric Vehicle":

            return slot_type == "Electric Vehicle"

        return slot_type == vehicle_type

    # =========================================================
    # SLOT ALLOCATION
    # =========================================================

    def allocate_slot(
        self,
        vehicle_type,
        vip=False
    ):

        self.validate_vehicle_type(
            vehicle_type
        )

        # VIP vehicle gets VIP slot first
        if vip:

            if "VIP1" not in self.occupied:

                return "VIP1"

            raise ValueError(
                "VIP parking slot unavailable"
            )

        # Normal allocation
        for slot_id, slot_type in self.slots.items():

            if slot_id in self.occupied:
                continue

            if self.is_compatible(
                slot_type,
                vehicle_type
            ):

                return slot_id

        raise ValueError(
            "No appropriate parking slot available"
        )

    # =========================================================
    # VEHICLE ENTRY
    # =========================================================

    def vehicle_entry(
        self,
        vehicle_number,
        vehicle_type,
        entry_time,
        vip=False
    ):

        if not vehicle_number:

            raise ValueError(
                "Invalid vehicle number"
            )

        self.validate_vehicle_type(
            vehicle_type
        )

        # Duplicate vehicle check
        if vehicle_number in self.tickets:

            existing_ticket = self.tickets[
                vehicle_number
            ]

            if existing_ticket["status"] == "PARKED":

                raise ValueError(
                    "Vehicle already parked"
                )

        # Allocate slot
        slot = self.allocate_slot(
            vehicle_type,
            vip
        )

        # Validate datetime
        try:

            datetime.strptime(
                entry_time,
                "%Y-%m-%d %H:%M"
            )

        except ValueError:

            raise ValueError(
                "Invalid entry time"
            )

        ticket_id = self.next_ticket

        self.next_ticket += 1

        ticket = {
            "ticket_id": ticket_id,
            "vehicle_number": vehicle_number,
            "vehicle_type": vehicle_type,
            "slot": slot,
            "entry_time": entry_time,
            "vip": vip,
            "status": "PARKED"
        }

        self.tickets[
            vehicle_number
        ] = ticket

        self.occupied[slot] = ticket

        return ticket

    # =========================================================
    # PEAK HOUR
    # =========================================================

    def is_peak_hour(self, time_string):

        dt = datetime.strptime(
            time_string,
            "%Y-%m-%d %H:%M"
        )

        hour = dt.hour

        # Morning peak: 8 AM - 10 AM
        # Evening peak: 5 PM - 8 PM

        if (
            8 <= hour < 10
            or
            17 <= hour < 20
        ):

            return True

        return False

    # =========================================================
    # PARKING FEE
    # =========================================================

    def calculate_fee(
        self,
        vehicle_type,
        entry_time,
        exit_time,
        vip=False,
        lost_ticket=False
    ):

        self.validate_vehicle_type(
            vehicle_type
        )

        # Lost ticket
        if lost_ticket:

            return 500

        entry = datetime.strptime(
            entry_time,
            "%Y-%m-%d %H:%M"
        )

        exit = datetime.strptime(
            exit_time,
            "%Y-%m-%d %H:%M"
        )

        if exit < entry:

            raise ValueError(
                "Exit time cannot be before entry time"
            )

        duration_seconds = (
            exit - entry
        ).total_seconds()

        duration_hours = (
            duration_seconds / 3600
        )

        # Early exit / minimum one hour
        billable_hours = max(
            1,
            int(duration_hours)
            if duration_hours.is_integer()
            else int(duration_hours) + 1
        )

        # Overnight parking
        days = (
            exit.date() - entry.date()
        ).days

        if days >= 1:

            # Daily maximum
            base_fee = (
                self.base_rates[vehicle_type]
                * 24
                * days
            )

            remaining_hours = (
                billable_hours - (24 * days)
            )

            if remaining_hours > 0:

                base_fee += (
                    remaining_hours
                    * self.base_rates[vehicle_type]
                )

        else:

            base_fee = (
                billable_hours
                * self.base_rates[vehicle_type]
            )

        # Peak hour pricing
        if self.is_peak_hour(exit_time):

            base_fee *= 1.25

        # VIP pricing
        if vip:

            base_fee *= 1.50

        return round(
            base_fee,
            2
        )

    # =========================================================
    # EXIT
    # =========================================================

    def vehicle_exit(
        self,
        vehicle_number,
        exit_time,
        lost_ticket=False
    ):

        if vehicle_number not in self.tickets:

            raise ValueError(
                "Vehicle not found"
            )

        ticket = self.tickets[
            vehicle_number
        ]

        if ticket["status"] == "EXITED":

            raise ValueError(
                "Vehicle already exited"
            )

        # Calculate fee
        fee = self.calculate_fee(
            ticket["vehicle_type"],
            ticket["entry_time"],
            exit_time,
            ticket["vip"],
            lost_ticket
        )

        # Release slot
        slot = ticket["slot"]

        if slot in self.occupied:

            del self.occupied[slot]

        ticket["exit_time"] = exit_time

        ticket["fee"] = fee

        ticket["lost_ticket"] = lost_ticket

        ticket["status"] = "EXITED"

        return fee

    # =========================================================
    # SLOT AVAILABILITY
    # =========================================================

    def available_slots(self):

        return [
            slot
            for slot in self.slots
            if slot not in self.occupied
        ]


# =============================================================
# MAIN PROGRAM
# =============================================================

def main():

    print("========================================")
    print("       SMART PARKING MANAGEMENT")
    print("========================================")

    parking = ParkingManagement()

    try:

        ticket = parking.vehicle_entry(
            "TN01AB1234",
            "Car",
            "2026-08-20 10:00"
        )

        print()
        print("Vehicle Entry Successful")

        print(
            "Ticket ID:",
            ticket["ticket_id"]
        )

        print(
            "Vehicle:",
            ticket["vehicle_number"]
        )

        print(
            "Slot:",
            ticket["slot"]
        )

        fee = parking.vehicle_exit(
            "TN01AB1234",
            "2026-08-20 13:00"
        )

        print()
        print("Vehicle Exit Successful")

        print(
            "Parking Fee:",
            fee
        )

    except ValueError as e:

        print(
            "ERROR:",
            e
        )


if __name__ == "__main__":
    main()
