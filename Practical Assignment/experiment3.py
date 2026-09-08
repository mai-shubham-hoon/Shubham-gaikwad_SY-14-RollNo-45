# Function that creates a discount closure
def create_discount(discount_rate):
    
    # Inner function remembers discount_rate
    def apply_discount(price):
        discount = price * discount_rate / 100
        final_price = price - discount
        return final_price
    
    return apply_discount


# Create multiple discount closures
discount10 = create_discount(10)
discount20 = create_discount(20)

# Apply discounts on different item prices
price1 = 1000
price2 = 2000
price3 = 500

print("Original Price:", price1)
print("After 10% Discount:", discount10(price1))

print("\nOriginal Price:", price2)
print("After 20% Discount:", discount20(price2))

print("\nOriginal Price:", price3)
print("After 10% Discount:", discount10(price3))