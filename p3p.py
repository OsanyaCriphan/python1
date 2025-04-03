# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Main 
try:
    # Prompt the user to enter the original price and discount percentage
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percentage)

    # Check if the discount was applied and print the final price
    if final_price < original_price:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
