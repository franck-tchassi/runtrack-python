def max_and_min():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    min = L[0]
    max = L[0]
    for i in L:
        if i < min:
            min = i
        if i > max:
            max = i 
    sum = min + max
    print("le maximum est:" +''+ str(max))
    print("le minimun est:" +''+ str(min))
    print("la somme est:", sum)

max_and_min()
