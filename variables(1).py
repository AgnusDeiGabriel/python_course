from django.db.models.expressions import result


def main ():
    # recolter une valeur sur le porte monnaie d'une persone
    username = "ander"
    porte_monnaie = 400
    # un produit qui aura pour valeur 50
    valise = 50
    # afficher la nouvelle valeur du porrte monnaie
    result = porte_monnaie - valise
    print("la nouvelle valeur de la porte monnaie de " + username + " est " + str(result))


if __name__ == '__main__':
    main()