import random

oszlop_betuk = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

ulesek = [["🟩" for _ in range(10)] for _ in range(10)]

print("Üdvözlünk a Csafer Színház Online felületén!")
print("______________________________________________\n")

valasztas = " "
nez = " "

while nez != "":
    print("Mai előadásaink:")
    print("1. előadás - részletekért '1' kulcsszót írd be.")
    print("2. előadás - részletekért '2' kulcsszót írd be.")
    print("3. előadás - részletekért '3' kulcsszót írd be.")
    print("4. előadás - részletekért '4' kulcsszót írd be.")
    print("5. előadás: Kabdebon - avagy Varbó árnyékában | részletekért '5' kulcsszót írd be.")
    print("6. előadás - részletekért '6' kulcsszót írd be.")
    print("______________________________________________\n")

    valasztas = input("Melyik előadás érdekel? ")
    
    if valasztas == "1":
        print("\nAZ ELSŐ ELŐADÁS")
        print("Leírás: Egyszer volt hol nem volt, volt egyszer egy feri...")
    elif valasztas == "2":
        print("\n2. ELŐADÁS")
        print("Leírás: Egyszer volt hol nem volt, volt egyszer egy feri...")
    elif valasztas == "3":
        print("\n3. ELŐADÁS")
        print("Leírás: Egyszer volt hol nem volt, volt egyszer egy feri...")
    elif valasztas == "4":
        print("\n4. ELŐADÁS")
        print("Leírás: Egyszer volt hol nem volt, volt egyszer egy feri...")
    elif valasztas == "5":
        print("\nKABDEBON - AVAGY VARBÓ ÁRNYÉKÁBAN")
        print("Leírás: Kabdebon mindennapi túléléséről szól a Varbó nevű településen.")
    elif valasztas == "6":
        print("\n6. ELŐADÁS")
        print("Leírás: Egyszer volt hol nem volt, volt egyszer egy feri...")
    else:
        print("\nNincs ilyen előadás, próbáld újra!\n")
        continue

    nez = input("\nTovább a helyválasztáshoz -> Enter lenyomása, minden más visszalépés a többi előadáshoz. ")

vasarlas_folyamatban = True
fizetendo_osszeg = 0 

while vasarlas_folyamatban:
    print("______________________________________________")
    print("\nÜlőhelyek kiválasztása")
    print("Árak: 1-2. sor (VIP): 5.000 Ft | 3-10. sor: 4.000 Ft | Zsákbamacska hely: 3.000 Ft")
    print("Jelmagyarázat: 🟩 = Üres, 🟥 = Foglalt\n")
    
    print("   A B C D E F G H I J")
    for i in range(10):
        sor_szam = str(i + 1).rjust(2)
        sor_tartalom = "".join(ulesek[i])
        print(f"{sor_szam} {sor_tartalom}")
        
    print(f"\nJelenlegi kosár értéke: {fizetendo_osszeg} Ft")
    print("\nLehetőségek:")
    print("1 - Konkrét hely választása")
    print("2 - Random hely (Zsákbamacska - 3.000 Ft)")
    print("3 - Fizetés és kilépés")
    
    opcio = input("Mit szeretnél tenni? (1/2/3): ")
    
    if opcio == "1":
        soros = input("Kérem a sor számát (1-10): ")
        oszlopos = input("Kérem az oszlop betűjét (A-J): ").upper()
        
        if soros.isdigit() and 1 <= int(soros) <= 10 and oszlopos in oszlop_betuk:
            sor_idx = int(soros) - 1
            oszlop_idx = oszlop_betuk.index(oszlopos)
            
            if ulesek[sor_idx][oszlop_idx] == "🟩":
                ulesek[sor_idx][oszlop_idx] = "🟥" 
                
                if sor_idx == 0 or sor_idx == 1:
                    print(f"\nSikeres VIP foglalás! Hely: {soros}{oszlopos}.")
                    fizetendo_osszeg += 5000
                else:
                    print(f"\nSikeres foglalás! Hely: {soros}{oszlopos}.")
                    fizetendo_osszeg += 4000
            else:
                print("\nSajnos ez a hely már foglalt, kérlek válassz másikat!")
        else:
            print("\nÉrvénytelen sor vagy oszlop!")
            
    elif opcio == "2":
        ures_helyek = []
        for r in range(10): 
            for c in range(10):
                if ulesek[r][c] == "🟩":
                    ures_helyek.append((r, c))
                    
        if ures_helyek:
            random_sor, random_oszlop = random.choice(ures_helyek)
            ulesek[random_sor][random_oszlop] = "🟥" 
            betu = oszlop_betuk[random_oszlop]
            print(f"\nSikeres Zsákbamacska foglalás! Kaptál egy helyet: {random_sor + 1}{betu}.")
            fizetendo_osszeg += 3000
        else:
            print("\nSajnos már nincs szabad hely a színházban!")
            
    elif opcio == "3":
        if fizetendo_osszeg == 0:
            print("\nNem választottál helyet, így nincs fizetendő összeg. Viszlát!")
            vasarlas_folyamatban = False
        else:
            print("______________________________________________")
            print(f"\nFizetés: Összesen {fizetendo_osszeg} Ft.")
            
            fizetes_kesz = False
            while fizetes_kesz != True:
                print("\n1 - Bankkártya")
                print("2 - Készpénz")
                fiz_mod = input("Válassz fizetési módot (1/2): ")
                
                if fiz_mod == "1":
                    kartyaszam = input("\nKérem a kártyaszámot (csak számokat írj be): ")
                    if kartyaszam.isdigit():
                        print("\nSikeres tranzakció! Köszönjük a vásárlást!")
                        fizetes_kesz = True
                    else:
                        print("Érvénytelen formátum, próbáld újra!")
                        
                elif fiz_mod == "2":
                    hatralevo = fizetendo_osszeg
                    print(f"\nFizetendő: {hatralevo} Ft.")
                    
                    while hatralevo > 0:
                        bedobott = input("Kérem a készpénzt (összeg): ")
                        if bedobott.isdigit():
                            bedobott = int(bedobott)
                            hatralevo -= bedobott
                            
                            if hatralevo > 0:
                                print(f"Még hiányzik: {hatralevo} Ft.")
                        else:
                            print("Kérlek, csak számot adj meg!")
                    
                    if hatralevo < 0:
                        visszajaro = hatralevo
                        print(f"Sikeres fizetés! A visszajáró: {visszajaro*(-1)} Ft.")
                    else:
                        print("Sikeres fizetés! Pontosan adtad, nincs visszajáró.")
                        
                    print("Köszönjük a vásárlást!")
                    fizetes_kesz = True
                    
                else:
                    print("Érvénytelen választás!")
            
            vasarlas_folyamatban = False
            
    else:
        print("\nÉrvénytelen választás, próbáld újra!")