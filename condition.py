from xml.sax.handler import property_interning_dict

wallet = 5000
computer_price = 1000

#le prix de l'ordi est inferieur a 1000
if computer_price <= wallet or computer_price > 1000:
    print("l'achat est possible")
    wallet -= computer_price
else:
    print("l'achat n'est pas possible, vous n'avez que {}$". format(wallet) )

texte = ("l'achat est possible", "l'achat est impossible")[computer_price <= 1000]

print(wallet)
