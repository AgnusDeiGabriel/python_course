def main():
    note1 = int(input("entrer la premierer note"))
    note2 = int(input("entrer la seconde note"))
    note3 = int(input("entrer la derniere note"))
    result = (note1 + note2 + note3) / 3
    print("le resultat est " + str(result))
if __name__ == '__main__':
    main()