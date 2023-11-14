def calculatrice(calcul):
     nb1 = ""
     nb2 = 0
     sign = ""
     for num in calcul:
        while num.isalpha():
                nb1 += num
        print(nb1)   
       
calculatrice("28*5")