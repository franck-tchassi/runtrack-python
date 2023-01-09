
def replace_element(L):

    if len(L) < 5:
        print("La liste doit avoir au moins 5 éléments!")
        return
    sum = L[2] + L[4]
    L[3] = sum

L = [1, 2, 3, 4, 5]
replace_element(L)
print("la valeur de L[1] est:" + " " + str(L[1]))
print("somme des cases voisines L[2] & L[4]:" + " " +str(L)) 
print("le dernier élement est:" + " " +str(L.pop())) 




