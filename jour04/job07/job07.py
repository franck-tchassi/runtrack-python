def Nbr_multipre_de_trois():
    compteur = 0
    L = [8, 24,48,2,16]
    for i in L:
        if i % 3 == 0:
            compteur +=1
    print(compteur)

Nbr_multipre_de_trois()
