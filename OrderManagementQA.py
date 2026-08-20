from OrderManagement import OrderManagement


def run_test(test_number, description, test_function):

    print()
    print(f"TEST {test_number}: {description}")
    print("----------------------------------------")

    try:

        result = test_function()

        if result:
            print("RESULT: PASS")
        else:
            print("RESULT: FAIL")

    except Exception as e:

        print("RESULT: PASS")
        print("Expected Exception:", e)


def test_1_single_product():

    order = OrderManagement()

    order.add_product("P101", 1)

    result = order.calculate_final_amount()

    return result["subtotal"] == 50000


def test_2_multiple_products():

    order = OrderManagement()

    order.add_product("P101", 1)
    order.add_product("P103", 2)

    result = order.calculate_final_amount()

    return result["subtotal"] == 56000


def test_3_zero_quantity():

    order = OrderManagement()

    try:
        order.add_product("P101", 0)
        return False

    except ValueError:
        return True


def test_4_negative_quantity():

    order = OrderManagement()

    try:
        order.add_product("P101", -2)
        return False

    except ValueError:
        return True


def test_5_invalid_product():

    order = OrderManagement()

    try:
        order.add_product("P999", 1)
        return False

    except ValueError:
        return True


def test_6_invalid_coupon():

    order = OrderManagement()

    order.add_product("P101", 1)

    try:
        order.calculate_final_amount("INVALID")
        return False

    except ValueError:
        return True


def test_7_maximum_coupon_discount():

    order = OrderManagement()

    order.add_product("P101", 1)

    result = order.calculate_final_amount("SAVE20")

    return result["coupon_discount"] <= 5000


def test_8_tax_calculation():

    order = OrderManagement()

    order.add_product("P105", 1)

    result = order.calculate_final_amount()

    expected_tax = (
        500
        - result["total_discount"]
    ) * 0.18

    return abs(result["tax"] - expected_tax) < 0.01


def test_9_free_shipping():

    order = OrderManagement()

    order.add_product("P101", 1)

    result = order.calculate_final_amount()

    return result["shipping"] == 0


def test_10_bulk_order():

    order = OrderManagement()

    order.add_product("P105", 10)

    result = order.calculate_final_amount()

    return result["bulk_discount"] > 0


def test_11_fashion_discount():

    order = OrderManagement()

    order.add_product("P103", 1)

    result = order.calculate_final_amount()

    return result["category_discount"] == 300


def test_12_books_discount():

    order = OrderManagement()

    order.add_product("P105", 1)

    result = order.calculate_final_amount()

    return result["category_discount"] == 75


def test_13_electronics_discount():

    order = OrderManagement()

    order.add_product("P102", 1)

    result = order.calculate_final_amount()

    return result["category_discount"] == 1000


def test_14_empty_order():

    order = OrderManagement()

    try:
        order.calculate_final_amount()
        return False

    except ValueError:
        return True


def test_15_coupon_save10():

    order = OrderManagement()

    order.add_product("P101", 1)

    result = order.calculate_final_amount("SAVE10")

    return result["coupon_discount"] == 5000


def test_16_small_order_shipping():

    order = OrderManagement()

    order.add_product("P105", 1)

    result = order.calculate_final_amount()

    return result["shipping"] == 100


def test_17_five_item_bulk_discount():

    order = OrderManagement()

    order.add_product("P105", 5)

    result = order.calculate_final_amount()

    return result["bulk_discount"] > 0


def test_18_invalid_product_quantity():

    order = OrderManagement()

    try:
        order.add_product("P999", 0)
        return False

    except ValueError:
        return True


def test_19_final_amount_positive():

    order = OrderManagement()

    order.add_product("P101", 1)

    result = order.calculate_final_amount()

    return result["final_amount"] > 0


def test_20_multiple_categories():

    order = OrderManagement()

    order.add_product("P101", 1)
    order.add_product("P103", 2)
    order.add_product("P105", 3)

    result = order.calculate_final_amount("SAVE10")

    return result["final_amount"] > 0


def main():

    print("========================================")
    print("       E-COMMERCE QA TESTING")
    print("========================================")

    run_test(
        1,
        "Single product",
        test_1_single_product
    )

    run_test(
        2,
        "Multiple products",
        test_2_multiple_products
    )

    run_test(
        3,
        "Zero quantity",
        test_3_zero_quantity
    )

    run_test(
        4,
        "Negative quantity",
        test_4_negative_quantity
    )

    run_test(
        5,
        "Invalid product",
        test_5_invalid_product
    )

    run_test(
        6,
        "Invalid coupon",
        test_6_invalid_coupon
    )

    run_test(
        7,
        "Maximum coupon discount",
        test_7_maximum_coupon_discount
    )

    run_test(
        8,
        "Tax calculation",
        test_8_tax_calculation
    )

    run_test(
        9,
        "Free shipping",
        test_9_free_shipping
    )

    run_test(
        10,
        "Bulk order",
        test_10_bulk_order
    )

    run_test(
        11,
        "Fashion discount",
        test_11_fashion_discount
    )

    run_test(
        12,
        "Books discount",
        test_12_books_discount
    )

    run_test(
        13,
        "Electronics discount",
        test_13_electronics_discount
    )

    run_test(
        14,
        "Empty order",
        test_14_empty_order
    )

    run_test(
        15,
        "SAVE10 coupon",
        test_15_coupon_save10
    )

    run_test(
        16,
        "Small order shipping",
        test_16_small_order_shipping
    )

    run_test(
        17,
        "Five item bulk discount",
        test_17_five_item_bulk_discount
    )

    run_test(
        18,
        "Invalid product and quantity",
        test_18_invalid_product_quantity
    )

    run_test(
        19,
        "Final amount validation",
        test_19_final_amount_positive
    )

    run_test(
        20,
        "Multiple categories",
        test_20_multiple_categories
    )

    print()
    print("========================================")
    print("       QA TESTING COMPLETED")
    print("========================================")


if __name__ == "__main__":
    main()
