# devoir : systeme de verification de mot de passe
password = input("entrer votre mot de passe")
password_length = len(password)

# verifier si le mot de passe est inferieur
if password_length <= 8:
    print("mot de passe trop court !")
else:
    print("mot de passe valide")


print(password_length)