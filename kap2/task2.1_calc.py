price_message, money_message = "Wie viel Euro kostet der Artikel: ", "Wie viel Euro wurden bezahlt: "
price, money = input(price_message), input(money_message)

result = float(money) - float(price)

formatted_float_value = "Es müssen {:.2f}€ zurückgegeben werden".format(result)
print(formatted_float_value)
