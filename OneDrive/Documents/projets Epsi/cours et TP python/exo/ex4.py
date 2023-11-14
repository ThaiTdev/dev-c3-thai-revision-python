number_list = [10,51,-9,-32,32,94,98,-615,1,-2]

def calcul_moyenne(array):
    new_array = sorted(array)
    max = 0
    min = new_array[len(array) - 1]
    print(min)
    moyenne = 0
    total_min = 0
    total_max = 0
    total_general = 0

    for item in range(len(array) - 1):
        if array[item] > max:
            total_max += array[item]
            max = array[item]
        elif array[item] < min:
            total_min += array[item]
            min = array[item]

    total_general = total_min + total_max
    moyenne = total_general / len(array)

    print(f"la plus petite valeur du tableau est {min}")
    print(f"la plus grande valeur du tableau est {max}")
    print(f"la moyenne du tableau est {moyenne}")

calcul_moyenne(number_list)