def calcul_factoriel(num):
    if not isinstance(num, int):
        print("La valeur passée en paramètre de votre fonction n'est pas un nombre entier.")
        return

    facto = 1
    for i in range(1, num + 1):
        facto *= i

    print(f"Le factoriel de {num} est: {facto}")


calcul_factoriel(5)
