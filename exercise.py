



print("===== INVENTORY ALERT SYSTEM =====")

product_name = input("Enter product name: ")

stock = int(input("Enter available stock: "))

if stock < 0:
    print("Invalid stock quantity")

elif stock == 0:
    print(f"{product_name}: Out of stock!")

elif stock <= 10:
    print(f"{product_name}: Critical stock!")

elif stock <= 25:
    print(f"{product_name}: Low stock!")

elif stock <= 100:
    print(f"{product_name}: Stock available.")

else:
    print(f"{product_name}: High inventory.")

print("==================================")