class OrderManagement:

    PRODUCTS = {
        "P101": {"name": "Laptop", "category": "Electronics", "price": 50000},
        "P102": {"name": "Mobile", "category": "Electronics", "price": 20000},
        "P103": {"name": "Shoes", "category": "Fashion", "price": 3000},
        "P104": {"name": "Shirt", "category": "Fashion", "price": 1500},
        "P105": {"name": "Book", "category": "Books", "price": 500}
    }

    COUPONS = {
        "SAVE10": 10,
        "SAVE20": 20
    }

    def __init__(self):
        self.items = []

    def add_product(self, product_id, quantity):

        if product_id not in self.PRODUCTS:
            raise ValueError("Invalid product ID")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        product = self.PRODUCTS[product_id]

        self.items.append({
            "id": product_id,
            "name": product["name"],
            "category": product["category"],
            "price": product["price"],
            "quantity": quantity
        })

    def calculate_subtotal(self):

        subtotal = 0

        for item in self.items:
            subtotal += item["price"] * item["quantity"]

        return subtotal

    def calculate_category_discount(self):

        discount = 0

        for item in self.items:

            amount = item["price"] * item["quantity"]

            if item["category"] == "Electronics":
                discount += amount * 0.05

            elif item["category"] == "Fashion":
                discount += amount * 0.10

            elif item["category"] == "Books":
                discount += amount * 0.15

        return discount

    def calculate_bulk_discount(self):

        total_quantity = sum(
            item["quantity"] for item in self.items
        )

        subtotal = self.calculate_subtotal()

        if total_quantity >= 10:
            return subtotal * 0.10

        if total_quantity >= 5:
            return subtotal * 0.05

        return 0

    def calculate_coupon_discount(self, coupon_code):

        if coupon_code is None or coupon_code == "":
            return 0

        if coupon_code not in self.COUPONS:
            raise ValueError("Invalid coupon code")

        subtotal = self.calculate_subtotal()

        discount = subtotal * self.COUPONS[coupon_code] / 100

        # Maximum coupon discount = 5000
        return min(discount, 5000)

    def calculate_tax(self, amount):

        # GST = 18%
        return amount * 0.18

    def calculate_shipping(self, amount):

        # Free shipping for orders >= 5000
        if amount >= 5000:
            return 0

        return 100

    def calculate_final_amount(self, coupon_code=None):

        if len(self.items) == 0:
            raise ValueError("Order is empty")

        subtotal = self.calculate_subtotal()

        category_discount = self.calculate_category_discount()

        bulk_discount = self.calculate_bulk_discount()

        coupon_discount = self.calculate_coupon_discount(coupon_code)

        total_discount = (
            category_discount
            + bulk_discount
            + coupon_discount
        )

        # Maximum total discount = 30% of subtotal
        max_discount = subtotal * 0.30

        if total_discount > max_discount:
            total_discount = max_discount

        taxable_amount = subtotal - total_discount

        tax = self.calculate_tax(taxable_amount)

        shipping = self.calculate_shipping(taxable_amount)

        final_amount = taxable_amount + tax + shipping

        return {
            "subtotal": subtotal,
            "category_discount": category_discount,
            "bulk_discount": bulk_discount,
            "coupon_discount": coupon_discount,
            "total_discount": total_discount,
            "tax": tax,
            "shipping": shipping,
            "final_amount": final_amount
        }


def main():

    print("========================================")
    print("       E-COMMERCE ORDER SYSTEM")
    print("========================================")

    order = OrderManagement()

    try:

        order.add_product("P101", 1)
        order.add_product("P103", 2)

        result = order.calculate_final_amount("SAVE10")

        print()
        print("ORDER DETAILS")
        print("----------------------------------------")

        print(f"Subtotal           : {result['subtotal']:.2f}")
        print(
            f"Category Discount  : "
            f"{result['category_discount']:.2f}"
        )
        print(
            f"Bulk Discount      : "
            f"{result['bulk_discount']:.2f}"
        )
        print(
            f"Coupon Discount    : "
            f"{result['coupon_discount']:.2f}"
        )
        print(
            f"Total Discount     : "
            f"{result['total_discount']:.2f}"
        )
        print(f"GST                : {result['tax']:.2f}")
        print(f"Shipping           : {result['shipping']:.2f}")

        print("----------------------------------------")

        print(
            f"FINAL AMOUNT       : "
            f"{result['final_amount']:.2f}"
        )

        print("========================================")

    except Exception as e:

        print("ERROR:", e)


if __name__ == "__main__":
    main()
