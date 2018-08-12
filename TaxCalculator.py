items = int(input("How many items do you need ? "))
subtotal = 0

for i in range(items):
    price = float(input("What is the price of the item ? "))
    subtotal += price

tax = float(input("What is the tax rate of your country ? (in decimals) "))

tax_needed = tax*subtotal
total = subtotal + tax_needed

print("Your subtotal cost is " + subtotal)
print("Your total tax is " + tax_needed)
print("Your total cost is " + total)