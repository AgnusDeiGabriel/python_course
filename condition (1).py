wallet = 5000
computer_price = 6000

if computer_price <= wallet:
    print("l'achat est possible")
    wallet -= computer_price
else:
    print("l'achat n'est pas possible vous n'avez que {}$".format(wallet))

text = ("l'achat est posible", "l'achat n'est pas possible") [computer_price <= 1000]

print("il vous reste {}$".format(wallet) )