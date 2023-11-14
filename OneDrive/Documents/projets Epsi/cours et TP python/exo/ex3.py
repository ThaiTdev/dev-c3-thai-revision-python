def calculatrice(calcul):
    nb1 = ""
    nb2 = 0
    sign = ""
    list_calcul = list(calcul)
    print(list_calcul) 

    for item in list_calcul:
        if item.isdigit() or item == '.':
            nb1 += item
        elif item in ['+', '-', '*', '/']:
            sign = item
            nb2 = float(nb1)
            nb1 = ""

    nb2 = float(nb1)  # Prend en compte le dernier nombre après le dernier opérateur

    if sign == '+':
        resultat = nb2 + float(nb1)
    elif sign == '-':
        resultat = nb2 - float(nb1)
    elif sign == '*':
        resultat = nb2 * float(nb1)
    elif sign == '/':
        resultat = nb2 / float(nb1)
    else:
        print("Opérateur non valide.")
        return

    print(f"Résultat du calcul {resultat}") 
calculatrice("3*9")