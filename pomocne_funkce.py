# pokus
hraci_plocha = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
oddelovac = "========================================"

def uvod():
    print("""Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game
========================================""")

def vypis_hraci_plochy():
    for i in hraci_plocha:
        print(" ".join(i))

def zapis_hrac1():
#  funkce bezi dokud neni spravne zadana pozice na hraci plose
    run = True
    while run:
        print(oddelovac)
        try:
            hrac1 = int(input("""Hrac "O", zadej cislo tahu: """))
            hrac1_znak = "O"
            index_1_hrac1 = int((hrac1 - 1) / 3)
            index_2_hrac1 = int((hrac1 - 1) % 3)
            if not str(hrac1).isdigit():
                print("Neplatny znak, zadej cislo")
            elif hrac1 not in range(1,10):
                print("Zadej cislo v rozmezi 1 az 9")
            elif hraci_plocha[index_1_hrac1][index_2_hrac1] != "-":
                print("Pole uz je obsazene, zadej znovu")
            else:
                hraci_plocha[index_1_hrac1][index_2_hrac1] = hrac1_znak
                run = False

        except ValueError:
            print("Zadej ciselnou hodnotu")


def zapis_hrac2():
    run = True
    while run:
        print(oddelovac)
        try:
            hrac2 = int(input("""Hrac "X", zadej cislo tahu: """))
            hrac2_znak = "X"
            index_1_hrac2 = int((hrac2 - 1) / 3)
            index_2_hrac2 = int((hrac2 - 1) % 3)
            if hrac2 not in range(1,10):
                print("Zadej cislo v rozmezi 1 az 9")
            elif hraci_plocha[index_1_hrac2][index_2_hrac2] != "-":
                print("Pole uz je obsazene, zadej znovu")
            else:
                hraci_plocha[index_1_hrac2][index_2_hrac2] = hrac2_znak
                run = False
        except ValueError:
            print("Zadej ciselnou hodnotu")


def kontrola_radku():
    remiza = 0
    for i in range(3):
        if hraci_plocha[i].count("X") == 3:
            print("""vyhral hrac "X" """)
            return False
        elif hraci_plocha[i].count("O") == 3:
            print("""vyhral hrac "O" """)
            return False
        elif hraci_plocha[i].count("-") == 0:
            remiza += 1
            if remiza == 3:
                print("Remiza")
                return False
    return True



def kontrola_sloupce():
    # sloupce prevartim na na radky a pak je kontrola stejna jako u radku
    sloupec = [[], [], []]
    for i in range(3):
        for j in range(3):
            sloupec[i].append(hraci_plocha[j][i])
    for i in range(3):
        if sloupec[i].count("O") == 3:
            print("""vyhral hrac "O" """)
            return False
        if sloupec[i].count("X") == 3:
            print("""vyhral hrac "X" """)
            return False
    return True


def kontrola_diagonaly():
    diagonala_1 = [hraci_plocha[0][0], hraci_plocha[1][1], hraci_plocha[2][2]]
    diagonala_2 = [hraci_plocha[0][2], hraci_plocha[1][1], hraci_plocha[2][0]]
    if diagonala_1.count("X") == 3 or diagonala_2.count("X") == 3:
        print("""vyhral hrac "X" """)
        return False
    if diagonala_1.count("O") == 3 or diagonala_2.count("O") == 3:
        print("""vyhral hrac "O" """)
        return False

    return True
