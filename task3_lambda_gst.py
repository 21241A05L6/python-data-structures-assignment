# Task 3: Lambda GST

gst = lambda price: price + (0.18 * price)

print(gst(100))

final_price = lambda price, discount: (price - price * discount/100) * 1.18

print(final_price(1000, 10))