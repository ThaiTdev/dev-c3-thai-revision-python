def calculatrice(calcul):
    nb1 = ""
    nb2 = 0
    sign = ""
    list_calcul = list(calcul)

    for item in list_calcul:
        if item.isdigit() or item == '.':
            nb1 += item
        elif item in ['+', '-', '*', '/']:
            sign = item
            nb2 = float(nb1)
            print(nb2)
            nb1 = ""

    # Prend en compte le dernier nombre après le dernier opérateur
    nb3 = float(nb1)
    print(nb3)

    if sign == '+':
        resultat = nb2 + nb3
    elif sign == '-':
        resultat = nb2 - nb3
    elif sign == '*':
        resultat = nb2 * nb3
    elif sign == '/':
        resultat = nb2 / nb3
    else:
        print("Opérateur non valide.")
        return

    print(f"Résultat du calcul {calcul} : {resultat}")

# Exemple d'utilisation
calculatrice("3.22/10")



