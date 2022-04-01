product_price = float(input("What's product price? "))
payment_plan = int(input("Digit your payment plan (1 - Credit card | 2 - Debit card | 3 - In cash): "))

if product_price >= 400 and (payment_plan == 1 or payment_plan == 2):
    discount_value = 20
    price_discount = product_price * (discount_value / 100)
    final_price = product_price - price_discount

    print("You have {}% of discount, you need pay only {:.2f}, you saved {:.2f}!".format(discount_value, final_price, price_discount))
else:
    print("You don't have a discount")
