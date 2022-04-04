hraci_plocha = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
for i in hraci_plocha:
    print(" ".join(i))


def zapis(hrac, znak):
    index_1 = int((hrac - 1) / 3)
    index_2 = int((hrac - 1) % 3)
    hraci_plocha[index_1][index_2] = znak



def kontrola_radku():
    for i in range(3):
        if hraci_plocha[i].count("X") == 3:
            print("""vyhral hrac "X" """)
            return False
        elif hraci_plocha[i].count("O") == 3:
            print("""vyhral hrac "O" """)
            return False
        else:
            return True

def kontrola_sloupce():
    sloupec = [[], [], []]
    for i in range(3):
        for j in range(3):
            sloupec[i].append(hraci_plocha[j][i])
    for i in range(3):
        if sloupec[i].count("X") == 3:
            print("""vyhral hrac "X" """)
            return False
        elif sloupec[i].count("O") == 3:
            print("""vyhral hrac "O" """)
            return False
        else:
            return True



def kontrola_diagonaly():
    diagonala_1 = [hraci_plocha[0][0], hraci_plocha[1][1], hraci_plocha[2][2]]
    diagonala_2 = [hraci_plocha[0][2], hraci_plocha[1][1], hraci_plocha[2][0]]
    if diagonala_1.count("X") == 3 or diagonala_2.count("X") == 3:
        print("""vyhral hrac "X" """)
        return False

    elif diagonala_1.count("O") == 3 or diagonala_2.count("O") == 3:
        print("""vyhral hrac "O" """)
        return False
    else:
        return True

run = True

while run:
    hrac1 = int(input("""Hrac "O", zadej cislo tahu: """))
    zapis(hrac1, "O")
    hrac2 = int(input("""Hrac "X", zadej cislo tahu: """))
    zapis(hrac2, "X")
    for i in hraci_plocha:
        print(" ".join(i))
    run = kontrola_radku() and kontrola_sloupce() and kontrola_diagonaly()


