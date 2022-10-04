def calc_discount(disc, p):
    return (disc / 100) * p


price_message, money_message = "Wie viel Euro kostet der Artikel: ", "Wie viel Euro wurden bezahlt: "
discount_message = "Wie viel Prozent Rabatt sollen gewährt werden: "
rerun = "j"
while rerun == "j":
    price = float(input(price_message))
    discount = int(input(discount_message))
    discount_in_euro = calc_discount(discount, price)

    discounted_price = price - discount_in_euro
    discount_price_message = "Es müssen {:.2f}€ bezahlt werden.".format(discounted_price)
    print(discount_price_message)

    paid = float(input(money_message))

    result = paid - discounted_price

    formatted_float_value = "Es müssen {:.2f}€ zurückgegeben werden".format(result)
    print(formatted_float_value)

    rerun = input("Soll noch eine Berechnung durchgeführt werden?: ")
