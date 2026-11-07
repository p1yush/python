






print("===== INVENTORY ALERT SYSTEM =====")

product_name = input("Enter product name: ")
product_price = int(input("Enter product price: "))

stock = int(input("Enter available stock: "))

if stock < 0:
    print("Invalid stock quantity")

elif stock == 0:
    print(f"{product_name}: Unavailable")

elif stock <= 10:
    print(f"{product_name}: Critical stock! Need more stock")

elif stock <= 25:
    print(f"{product_name}: Low stock!")

elif stock <= 100:
    print(f"{product_name}: Stock available.")

else:
    print(f"{product_name}: High inventory.")

total_inventory = product_price * stock
print(f"Total Value: {total_inventory}")

print("==================================")