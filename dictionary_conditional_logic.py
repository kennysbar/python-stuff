purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

grocery = input()
amount = input()

grocery_price = purchase[grocery]
total_price = float(grocery_price) * float(amount)
total_price_rounded = "{:.2f}".format(total_price)

if int(amount) < 10:
    print(grocery + " $" + total_price_rounded)

elif int(amount) >= 10 and int(amount) < 20:
    total_price = float(total_price) * float(0.95)
    total_price_rounded = "{:.2f}".format(total_price)
    print(grocery + " $" + total_price_rounded)

elif int(amount) >= 21:
    total_price = float(total_price) * float(0.90)
    total_price_rounded = "{:.2f}".format(total_price)
    print(grocery + " $" + total_price_rounded)

#print(grocery_price)

