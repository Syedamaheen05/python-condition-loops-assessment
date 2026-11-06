#  PHARMACY INVENTORY SYSTEM

print("===== Pharmacy Inventory System =====")

# Get number of medicines
while True:
    try:
        total_medicines = int(input("How many medicines do you want to process? "))

        if total_medicines > 0:
            break
        else:
            print("Please enter a number greater than zero!")

    except ValueError:
        print("Invalid input! Please enter a whole number.")

# Initialize accumulators
total_revenue = 0
restock_count = 0

# Process medicines
for medicine_number in range(1, total_medicines + 1):

    print(f"\n--- Medicine {medicine_number} ---")

    # Get medicine name
    medicine_name = input("Enter medicine name: ")

    # Validate available stock
    while True:
        try:
            available_stock = int(input("Enter available stock: "))

            if available_stock >= 0:
                break
            else:
                print("Stock cannot be negative!")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    # Validate price per unit
    while True:
        try:
            price_per_unit = float(input("Enter price per unit: "))

            if price_per_unit >= 0:
                break
            else:
                print("Price cannot be negative!")

        except ValueError:
            print("Invalid input! Please enter a numeric price.")

    # Validate quantity sold
    while True:
        try:
            quantity_sold = int(input("Enter quantity sold: "))

            if quantity_sold > 0:
                break
            else:
                print("Quantity sold must be greater than zero!")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    # Check stock availability
    if quantity_sold <= available_stock:

        # Calculate sales amount
        sales_amount = quantity_sold * price_per_unit

        # Update total revenue
        total_revenue += sales_amount

        # Calculate remaining stock
        remaining_stock = available_stock - quantity_sold

        print(f"Sales amount: Rs. {sales_amount}")
        print(f"Remaining stock: {remaining_stock}")

    else:
        print("Insufficient stock! Sale cannot be completed.")

        sales_amount = 0
        remaining_stock = available_stock

        print(f"Remaining stock: {remaining_stock}")

    # Check low stock
    if remaining_stock < 10:

        print(f"WARNING: {medicine_name} is low in stock. Restocking is required!")

        # Count medicines requiring restocking
        restock_count += 1

# Final pharmacy report
print("\n=================================")
print("       PHARMACY SALES REPORT")
print("=================================")

print(f"Total medicines processed: {total_medicines}")
print(f"Total pharmacy revenue: Rs. {total_revenue}")
print(f"Medicines requiring restocking: {restock_count}")


