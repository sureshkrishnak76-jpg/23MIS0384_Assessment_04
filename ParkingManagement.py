from datetime import datetime


class ParkingManagement:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(self):

        # Parking slot ID -> slot type
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

        # Occupied slots
        self.occupied = {}

        # Vehicle number -> ticket
        self.tickets = {}

        # Ticket number
        self.next_ticket = 1001

        # Base parking charges per hour
        self.base_rates = {
            "Bike": 30,
            "Car": 50,
            "SUV": 70,
            "Truck": 100,
            "Electric Vehicle": 50
        }

        # EV charging fee per hour
        self.ev_charging_rate = 20

        # Lost ticket fixed charge
        self.lost_ticket_charge = 500

    # =========================================================
    # VALIDATE VEHICLE TYPE
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
    # CHECK SLOT COMPATIBILITY
    # =========================================================

    def is_compatible(
        self,
        slot_type,
        vehicle_type
    ):

        # VIP slot cannot be used by
        # normal vehicles
        if slot_type == "VIP":

            return False

        # EV must use dedicated EV slot
        if vehicle_type == "Electric Vehicle":

            return (
                slot_type
                == "Electric Vehicle"
            )

        # Other vehicles need matching slot
        return slot_type == vehicle_type

    # =========================================================
    # ALLOCATE SLOT
    # =========================================================

    def allocate_slot(
        self,
        vehicle_type,
        vip=False
    ):

        self.validate_vehicle_type(
            vehicle_type
        )

        # -----------------------------------------------------
        # VIP vehicle
        # -----------------------------------------------------

        if vip:

            if "VIP1" not in self.occupied:

                return "VIP1"

            raise ValueError(
                "VIP parking slot unavailable"
            )

        # -----------------------------------------------------
        # Normal vehicle
        # -----------------------------------------------------

        for slot_id, slot_type in self.slots.items():

            # Skip occupied slot
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

        # Validate vehicle number
        if not vehicle_number:

            raise ValueError(
                "Invalid vehicle number"
            )

        # Validate vehicle type
        self.validate_vehicle_type(
            vehicle_type
        )

        # Validate entry time
        try:

            datetime.strptime(
                entry_time,
                "%Y-%m-%d %H:%M"
            )

        except ValueError:

            raise ValueError(
                "Invalid entry time"
            )

        # -----------------------------------------------------
        # Duplicate vehicle check
        # -----------------------------------------------------

        if vehicle_number in self.tickets:

            existing_ticket = self.tickets[
                vehicle_number
            ]

            if existing_ticket["status"] == "PARKED":

                raise ValueError(
                    "Vehicle already parked"
                )

        # -----------------------------------------------------
        # Allocate parking slot
        # -----------------------------------------------------

        slot = self.allocate_slot(
            vehicle_type,
            vip
        )

        # -----------------------------------------------------
        # Generate ticket
        # -----------------------------------------------------

        ticket_id = self.next_ticket

        self.next_ticket += 1

        ticket = {

            "ticket_id": ticket_id,

            "vehicle_number":
                vehicle_number,

            "vehicle_type":
                vehicle_type,

            "slot":
                slot,

            "entry_time":
                entry_time,

            "vip":
                vip,

            "status":
                "PARKED"
        }

        self.tickets[
            vehicle_number
        ] = ticket

        self.occupied[
            slot
        ] = ticket

        return ticket

    # =========================================================
    # PEAK HOUR CHECK
    # =========================================================

    def is_peak_hour(
        self,
        time_string
    ):

        dt = datetime.strptime(
            time_string,
            "%Y-%m-%d %H:%M"
        )

        hour = dt.hour

        # Morning peak:
        # 08:00 - 09:59

        # Evening peak:
        # 17:00 - 19:59

        if (
            8 <= hour < 10
            or
            17 <= hour < 20
        ):

            return True

        return False

    # =========================================================
    # PARKING FEE CALCULATION
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

        # -----------------------------------------------------
        # Lost ticket
        # -----------------------------------------------------

        if lost_ticket:

            return self.lost_ticket_charge

        # -----------------------------------------------------
        # Convert dates
        # -----------------------------------------------------

        entry = datetime.strptime(
            entry_time,
            "%Y-%m-%d %H:%M"
        )

        exit_time_obj = datetime.strptime(
            exit_time,
            "%Y-%m-%d %H:%M"
        )

        # -----------------------------------------------------
        # Validate exit
        # -----------------------------------------------------

        if exit_time_obj < entry:

            raise ValueError(
                "Exit time cannot be before entry time"
            )

        # -----------------------------------------------------
        # Calculate duration
        # -----------------------------------------------------

        duration_seconds = (
            exit_time_obj - entry
        ).total_seconds()

        duration_hours = (
            duration_seconds / 3600
        )

        # Minimum one hour
        if duration_hours <= 1:

            billable_hours = 1

        else:

            billable_hours = int(
                duration_hours
            )

            if duration_hours > billable_hours:

                billable_hours += 1

        # -----------------------------------------------------
        # Base parking charge
        # -----------------------------------------------------

        rate = self.base_rates[
            vehicle_type
        ]

        base_fee = (
            billable_hours * rate
        )

        # -----------------------------------------------------
        # Peak hour pricing
        # -----------------------------------------------------

        if self.is_peak_hour(
            exit_time
        ):

            base_fee *= 1.25

        # -----------------------------------------------------
        # VIP pricing
        # -----------------------------------------------------

        if vip:

            base_fee *= 1.50

        # -----------------------------------------------------
        # EV charging fee
        # -----------------------------------------------------

        charging_fee = 0

        if vehicle_type == "Electric Vehicle":

            charging_fee = (
                billable_hours
                * self.ev_charging_rate
            )

        # -----------------------------------------------------
        # Final amount
        # -----------------------------------------------------

        total_fee = (
            base_fee
            + charging_fee
        )

        return round(
            total_fee,
            2
        )

    # =========================================================
    # VEHICLE EXIT
    # =========================================================

    def vehicle_exit(
        self,
        vehicle_number,
        exit_time,
        lost_ticket=False
    ):

        # Check vehicle
        if vehicle_number not in self.tickets:

            raise ValueError(
                "Vehicle not found"
            )

        ticket = self.tickets[
            vehicle_number
        ]

        # Check already exited
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

        # Update ticket
        ticket["exit_time"] = exit_time

        ticket["fee"] = fee

        ticket["lost_ticket"] = (
            lost_ticket
        )

        ticket["status"] = "EXITED"

        return fee

    # =========================================================
    # AVAILABLE SLOTS
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

    print(
        "========================================"
    )

    print(
        "       SMART PARKING MANAGEMENT"
    )

    print(
        "========================================"
    )

    parking = ParkingManagement()

    try:

        # Vehicle entry
        ticket = parking.vehicle_entry(

            "TN01AB1234",

            "Car",

            "2026-08-20 10:00"
        )

        print()

        print(
            "Vehicle Entry Successful"
        )

        print(
            "Ticket ID:",
            ticket["ticket_id"]
        )

        print(
            "Vehicle:",
            ticket["vehicle_number"]
        )

        print(
            "Vehicle Type:",
            ticket["vehicle_type"]
        )

        print(
            "Parking Slot:",
            ticket["slot"]
        )

        print(
            "Entry Time:",
            ticket["entry_time"]
        )

        # Vehicle exit
        fee = parking.vehicle_exit(

            "TN01AB1234",

            "2026-08-20 13:00"
        )

        print()

        print(
            "Vehicle Exit Successful"
        )

        print(
            "Parking Fee:",
            fee
        )

        print()

        print(
            "Available Slots:"
        )

        print(
            parking.available_slots()
        )

    except ValueError as e:

        print(
            "ERROR:",
            e
        )


if __name__ == "__main__":

    main()
