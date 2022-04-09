from pomocne_funkce import*

def main():
    run = True
    vypis_hraci_plochy()
    while run:
        zapis_hrac1()
        vypis_hraci_plochy()
        run = kontrola_radku() and kontrola_sloupce() and kontrola_diagonaly()
        if run == False:
            break
        zapis_hrac2()
        vypis_hraci_plochy()
        run = kontrola_radku() and kontrola_sloupce() and kontrola_diagonaly()
        if run == False:
            break

if __name__ == "__main__":
    uvod()
    main()
