def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)
    
    if final_price == original_price:
        print(f"No discount applied. The price remains: {original_price:.2f}")
    else:
        print(f"The final price after applying the discount is: {final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount.")
