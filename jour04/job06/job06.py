def echange_liste(maListe):
    if len(maListe) < 2:
        return
    maListe[0], maListe[-1] = maListe[-1], maListe[0]
    print(maListe)

maListe = [5, 8, 9, 19]
echange_liste(maListe)
