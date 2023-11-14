def Manipulation_string():
    Maj = ""
    Min = ""
    long = 0
    phrase = str(input("Veuillez entrer une phrase: "))
    while not any(char.isalpha() for char in phrase):
        print("ceci n'est pas une phrase")
        phrase = str(input("Veuillez entrer au moins une lettre: "))
    else:
        Maj = phrase.upper()
        Min = phrase.lower()
        long = len(phrase)
    print(f"Voici votre phrase en majuscule: {Maj}")
    print(f"Voici votre phrase en minuscule: {Min}")
    print(f"Voici la longueur de votre phrase: {long}")


Manipulation_string()
      
