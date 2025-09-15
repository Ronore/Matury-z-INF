drontestowylista = []
pliktestowy = open("Matura2025_zrodla/dron.txt", "r+")
for i in pliktestowy:
    if i is None:
        break
    temp = []
    temp.append(int(i.partition(" ")[0]))
    temp.append(int(i.partition(" ")[2]))
    drontestowylista.append(temp)

def NWD3_1(lista_zmian_drona):
    counter = 0
    for i in lista_zmian_drona:
        if i[0] < 0:
            liczba1 = i[0] * -1
        else:
            liczba1 = i[0]
        if i[1] < 0:
            liczba2 = i[1] * -1
        else:
            liczba2 = i[1]
        while True:
            if liczba2 == 0:
                break
            if liczba1 != liczba2:
                if liczba1 > liczba2:
                    liczba1 = liczba1 - liczba2
                else:
                    liczba2 = liczba2 - liczba1
            else:
                 break
        if liczba1 > 1:
            counter += 1
    print(counter)


def Czy_w_kwadracie(lista_zmian_drona):
    licznik = 0
    pozycja_x = 0
    pozycja_y = 0
    for index_listy_pozycji_drona in range (len(lista_zmian_drona)-1):
        pozycja_x += lista_zmian_drona[index_listy_pozycji_drona][0]
        pozycja_y += lista_zmian_drona[index_listy_pozycji_drona][1]
        if pozycja_x > 0 and pozycja_y > 0 and pozycja_x < 5000 and pozycja_y < 5000:
            licznik += 1
    print(licznik)


def Czy_w_lini(lista_zmian_drona):
    pozycja_x = 0
    pozycja_y = 0
    pozycje_drona = [[0,0]]
    for index_listy_pozycji_drona in range(len(lista_zmian_drona)):
        pozycja_x += lista_zmian_drona[index_listy_pozycji_drona][0]
        pozycja_y += lista_zmian_drona[index_listy_pozycji_drona][1]
        pozycje_drona.append([pozycja_x, pozycja_y])
    for i in range(len(pozycje_drona)-2):
        for j in range(len(pozycje_drona)-i):
            for k in range(len(pozycje_drona)-i):
                if pozycje_drona[i][0] - pozycje_drona[j+i][0] == pozycje_drona[j+i][0] - pozycje_drona[k+i][0] != 0:
                    if pozycje_drona[i][1] - pozycje_drona[j+i][1]  == pozycje_drona[j+i][1] - pozycje_drona[k+i][1] != 0:
                        print(f"{pozycje_drona[i]},{pozycje_drona[j+i]},{pozycje_drona[k+i]}")



NWD3_1(drontestowylista)
Czy_w_kwadracie(drontestowylista)
Czy_w_lini(drontestowylista)