with open('data.txt', 'r', encoding='utf8') as fichier:
    contenu = fichier.read()
new_content = contenu.split()
print(new_content)

def read_file(file):
    nb_word = 0
    for i in range(len(file)):
        print(i)
        nb_word += 1
    print(f" le fichier contient {nb_word} mots")
    fichier = open("resultat.txt", "w")
    fichier.write(str(nb_word))
    fichier.close()
read_file(new_content)

