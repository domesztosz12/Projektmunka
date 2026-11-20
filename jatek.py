# Játékos változók
hp = 100
max_hp = 100
gold = 0
days = 0
dmg = 10
pancel = 1
sarkany_hp = 1000
# Név
name = input("Adj meg egy karakter nevet: ")
name = name.strip().title()
kisbetus = name.lower()
if kisbetus == "naplopó jános" or kisbetus == "naplopo janos":
    hp = hp + 50
    max_hp = max_hp + 50
    gold = gold + 25
    print("Kecses a neved, kapsz 50 extra hp-t és 25 aranyat!")
# Tutorial
print("")
print("Szia", name)
print("Story: Te vagy", name + ", Dandória lovagja, akinek meg kell védenie Dandória városát a buta sárkány elől.")
print("Tutorial:")
print("- Minden nap 2 választási lehetőséget kapsz hogy mit csinálhatsz.")
print("- Balra vagy jobbra, melyik lesz?")
print("- Minden 3. napon jön egy kereskedő, akitől vehetsz dolgokat.")
print("- A 10. napon jön a sárkány, neki 1000 hp-ja van.")
print("- Jó játékot!")

# 1. nap: goblin vagy arany
if hp > 0:
    days = days + 1
    print("1. nap")
    print("Balra egy buta goblin szeretne harcolni veled.")
    print("Jobbra pedig találsz 10 aranyat egy szénabálába eldugva.")
    valasztas = int(input("Balra vagy jobbra szeretnél menni? Írd be hogy 1 (balra), vagy 2 (jobbra): "))
    if valasztas == 1:
        print("Balra mentél!")
        print("Elmentél buta goblint ölni a dandus folyó mentén.")
        goblin_dmg = 3
        goblin_hp = 30
        utesek = 0
        while goblin_hp > 0:
            goblin_hp = goblin_hp - dmg
            utesek = utesek + 1
        sebzes = round(utesek * goblin_dmg / pancel)
        hp = hp - sebzes
        gold = gold + 25
        print("Legyőzted a goblint", utesek, "ütéssel!")
        print("Kaptál 25 aranyat, de veszítettél", sebzes, "hp-t!")
    elif valasztas == 2:
        print("Jobbra mentél!")
        print("Találtál 10 aranyat!")
        gold = gold + 10
    else:
        print("Egész nap egy helyben álltál.")
    if hp < 0:
        hp = 0
    print(hp, "❤️   hp-d maradt.")
    print(gold, "gold-od lett.")
    print(days, ". napod ért véget.")

# 2. nap: kard vagy pajzs
if hp > 0:
    days = days + 1
    print("2. nap")
    print("Balra láttál egy kardot, ami megnöveli a dmg-ed.")
    print("Jobbra láttál egy pajzsot, ami megnöveli a shielded.")
    valasztas = int(input("Balra vagy jobbra szeretnél menni? Írd be hogy 1 (balra), vagy 2 (jobbra): "))
    if valasztas == 1:
        print("Balra mentél!")
        print("Az utadon találtál egy kardot!")
        print("Felment a dmg-ed 10-zel!")
        dmg = dmg + 10
    elif valasztas == 2:
        print("Jobbra mentél!")
        print("Találtál az úton egy pajzsot!")
        print("Ez megvéd a kapott dmg felétől.")
        pancel = 2
    else:
        print("Egy helyben álltál egész nap.")
    print(hp, "❤️   hp-d maradt.")
    print(gold, "gold-od lett.")
    print(days, ". napod ért véget.")

# 3. nap: kereskedő
if hp > 0:
    days = days + 1
    print("3. nap")
    print("Találkoztál egy kereskedővel.")
    print("Kereskedő: Szia! Mit szeretnél venni?")
    vasarlas = 0
    while vasarlas != 4:
        print("Aranyad:", gold, "| hp:", hp, "/", max_hp, "| dmg:", dmg, "| páncél:", pancel)
        print("1 - Jobb kard (+25 dmg)  30 arany")
        print("2 - Jobb páncél (+0.5 páncél)  30 arany")
        print("3 - Gyógyital (+40 hp)  15 arany")
        print("4 - Továbbállok")
        vasarlas = int(input("Mit szeretnél venni? "))
        if vasarlas == 1:
            if gold >= 30:
                gold = gold - 30
                dmg = dmg + 25
                print("Megvetted a kardot! A dmg-ed most", dmg)
            else:
                print("Kereskedő: Nincs elég aranyad.")
        elif vasarlas == 2:
            if gold >= 30:
                gold = gold - 30
                pancel = pancel + 0.5
                print("Megvetted a páncélt! A páncélod most", pancel)
            else:
                print("Kereskedő: Nincs elég aranyad.")
        elif vasarlas == 3:
            if gold >= 15:
                gold = gold - 15
                hp = hp + 40
                if hp > max_hp:
                    hp = max_hp
                print("Megittad a gyógyitalt! A hp-d most", hp)
            else:
                print("Kereskedő: Nincs elég aranyad.")
        elif vasarlas == 4:
            print("Kereskedő: Szia!")
        else:
            print("Kereskedő: Ilyen nincs.")
    print(days, ". napod ért véget.")

# 4. nap: mocsár vagy forrás
if hp > 0:
    days = days + 1
    print("4. nap")
    print("Balra egy mocsár van, lehet hogy van benne kincs.")
    print("Jobbra egy forrás van.")
    valasztas = int(input("Balra vagy jobbra szeretnél menni? Írd be hogy 1 (balra), vagy 2 (jobbra): "))
    if valasztas == 1:
        print("Balra mentél!")
        print("Találtál egy ládát, 40 arany volt benne!")
        print("De megcsípett egy kígyó és megmérgezett!")
        gold = gold + 40
        for kor in range(3, 0, -1):
            mereg = kor * 4
            hp = hp - mereg
            if hp < 0:
                hp = 0
            print("A méreg sebzett:", mereg, "-> hp-d:", hp)
        print("Elmúlt a méreg.")
    elif valasztas == 2:
        print("Jobbra mentél!")
        print("Ittál a forrásból, kaptál 20 hp-t!")
        hp = hp + 20
        if hp > max_hp:
            hp = max_hp
    else:
        print("Egy helyben álltál egész nap.")
    if hp < 0:
        hp = 0
    print(hp, "❤️   hp-d maradt.")
    print(gold, "gold-od lett.")
    print(days, ". napod ért véget.")

# 5. nap: troll vagy kocsma
if hp > 0:
    days = days + 1
    print("5. nap")
    print("Balra egy híd van, amit egy troll őriz.")
    print("Jobbra egy kocsma van.")
    valasztas = int(input("Balra vagy jobbra szeretnél menni? Írd be hogy 1 (balra), vagy 2 (jobbra): "))
    if valasztas == 1:
        print("Balra mentél!")
        print("A troll nem enged át, harcolnod kell vele!")
        troll_hp = 120
        troll_dmg = 8
        utesek = 0
        while troll_hp > 0 and hp > 0:
            utesek = utesek + 1
            troll_hp = troll_hp - dmg
            if troll_hp < 0:
                troll_hp = 0
            print(utesek, ". ütés:", dmg, "sebzés -> troll hp:", troll_hp)
            if troll_hp > 0:
                sebzes = round(troll_dmg / pancel)
                hp = hp - sebzes
                if hp < 0:
                    hp = 0
                print("A troll visszaütött:", sebzes, "sebzés -> hp-d:", hp)
        if hp > 0:
            gold = gold + 50
            print("Megölted a trollt! Kaptál 50 aranyat!")
        else:
            print("A troll megölt...")
    elif valasztas == 2:
        print("Jobbra mentél!")
        print("Kő papír ollóztál egy kalózzal.")
        if gold < 10:
            print("Nincs pénzed, nem kő papír ollózhatsz.")
        elif (gold + hp) % 2 == 0:
            gold = gold + 20
            print("Nyertél 20 aranyat!")
        else:
            gold = gold - 10
            print("Vesztettél 10 aranyat.")
        hp = hp + 10
        if hp > max_hp:
            hp = max_hp
        print("Pihentél is egy kicsit, kaptál 10 hp-t.")
    else:
        print("Egy helyben álltál egész nap.")
    if hp < 0:
        hp = 0
    print(hp, "❤️   hp-d maradt.")
    print(gold, "gold-od lett.")
    print(days, ". napod ért véget.")

# 6. nap: kereskedő
if hp > 0:
    days = days + 1
    print("6. nap")
    print("Megint jött a kereskedő.")
    print("Kereskedő: Szia! Mit szeretnél venni?")
    vasarlas = 0
    while vasarlas != 4:
        print("")
        print("Aranyad:", gold, "| hp:", hp, "/", max_hp, "| dmg:", dmg, "| páncél:", pancel)
        print("1 - Jobb kard (+25 dmg)  30 arany")
        print("2 - Jobb páncél (+0.5 páncél)  30 arany")
        print("3 - Gyógyital (+40 hp)  15 arany")
        print("4 - Továbbállok")
        vasarlas = int(input("Mit szeretnél venni? "))
        if vasarlas == 1:
            if gold >= 30:
                gold = gold - 30
                dmg = dmg + 25
                print("Megvetted a kardot! A dmg-ed most", dmg)
            else:
                print("Kereskedő: Nincs elég aranyad.")
        elif vasarlas == 2:
            if gold >= 30:
                gold = gold - 30
                pancel = pancel + 0.5
                print("Megvetted a páncélt! A páncélod most", pancel)
            else:
                print("Kereskedő: Nincs elég aranyad.")
        elif vasarlas == 3:
            if gold >= 15:
                gold = gold - 15
                hp = hp + 40
                if hp > max_hp:
                    hp = max_hp
                print("Megittad a gyógyitalt! A hp-d most", hp)
            else:
                print("Kereskedő: Nincs elég aranyad.")
        elif vasarlas == 4:
            print("Kereskedő: Szia!")
        else:
            print("Kereskedő: Ilyen nincs.")
    print(days, ". napod ért véget.")

# 7. nap: ogre vagy bánya
if hp > 0:
    days = days + 1
    print("7. nap")
    print("Balra egy öreg ogre lakik.")
    print("Jobbra egy bánya van.")
    valasztas = int(input("Balra vagy jobbra szeretnél menni? Írd be hogy 1 (balra), vagy 2 (jobbra): "))
    if valasztas == 1:
        print("Balra mentél!")
        print("Ogre: Ha kitalálod a rejtvényt, erősebb lesz a kardod.")
        print("Ogre: Minél többet veszel el belőle, annál nagyobb lesz. Mi az?")
        valasz = input("A válaszod: ")
        valasz = valasz.strip().lower()
        if valasz == "gödör" or valasz == "godor" or valasz == "lyuk":
            dmg = dmg + 20
            print("Ogre: Jó válasz! Kaptál 20 dmg-t.")
        else:
            hp = hp - 10
            print("Ogre: Rossz válasz, a gödör volt a jó.")
            print("Az ogre megdobott egy kővel. -10 hp")
    elif valasztas == 2:
        print("Jobbra mentél!")
        print("Elkezdtél bányászni.")
        for utes in range(1, 6):
            if utes == 5:
                gold = gold + 10
                print(utes, ". ütés: találtál egy nagy aranyat! +10 arany")
            else:
                gold = gold + 4
                print(utes, ". ütés: +4 arany")
    else:
        print("Egy helyben álltál egész nap.")
    if hp < 0:
        hp = 0
    print(hp, "❤️   hp-d maradt.")
    print(gold, "gold-od lett.")
    print(days, ". napod ért véget.")

    # 8. nap: buta goblin vezér vagy íjászok
if hp > 0:
    days = days + 1
    print("8. nap")
    print("Balra van a buta goblinoknak a vezére.")
    print("Jobbra vannak az íjászok.")
    valasztas = int(input("Balra vagy jobbra szeretnél menni? Írd be hogy 1 (balra), vagy 2 (jobbra): "))
    if valasztas == 1:
        print("Balra mentél!")
        print("Megtámadott a buta goblin vezér!")
        vezer_hp = 150
        vezer_dmg = 12
        utesek = 0
        while vezer_hp > 0 and hp > 0:
            utesek = utesek + 1
            vezer_hp = vezer_hp - dmg
            if vezer_hp < 0:
                vezer_hp = 0
            print(utesek, ". ütés:", dmg, "sebzés -> buta goblin vezér hp:", vezer_hp)
            if vezer_hp > 0:
                sebzes = round(vezer_dmg / pancel)
                hp = hp - sebzes
                if hp < 0:
                    hp = 0
                print("A buta goblin vezér visszaütött:", sebzes, "sebzés -> hp-d:", hp)
        if hp > 0:
            gold = gold + 40
            print("Megölted a buta goblin vezért! Kaptál 40 aranyat!")
        else:
            print("A buta goblin vezér megölt...")
    elif valasztas == 2:
        print("Jobbra mentél!")
        print("Az íjászok azt mondták, hogy segítenek a sárkány ellen.")
        sarkany_hp = sarkany_hp - 200
        print("A sárkánynak 200-zal kevesebb hp-ja lesz!")
    else:
        print("Egy helyben álltál egész nap.")
    if hp < 0:
        hp = 0
    print(hp, "❤️   hp-d maradt.")
    print(gold, "gold-od lett.")
    print(days, ". napod ért véget.")

# 9. nap: kereskedő
if hp > 0:
    days = days + 1
    print("9. nap")
    print("Utoljára jött a kereskedő a sárkány előtt.")
    print("Kereskedő: Szia! Mit szeretnél venni?")
    vasarlas = 0
    while vasarlas != 4:
        print("")
        print("Aranyad:", gold, "| hp:", hp, "/", max_hp, "| dmg:", dmg, "| páncél:", pancel)
        print("1 - Jobb kard (+25 dmg)  30 arany")
        print("2 - Jobb páncél (+0.5 páncél)  30 arany")
        print("3 - Gyógyital (+40 hp)  15 arany")
        print("4 - Továbbállok")
        vasarlas = int(input("Mit szeretnél venni? "))
        if vasarlas == 1:
            if gold >= 30:
                gold = gold - 30
                dmg = dmg + 25
                print("Megvetted a kardot! A dmg-ed most", dmg)
            else:
                print("Kereskedő: Nincs elég aranyad.")
        elif vasarlas == 2:
            if gold >= 30:
                gold = gold - 30
                pancel = pancel + 0.5
                print("Megvetted a páncélt! A páncélod most", pancel)
            else:
                print("Kereskedő: Nincs elég aranyad.")
        elif vasarlas == 3:
            if gold >= 15:
                gold = gold - 15
                hp = hp + 40
                if hp > max_hp:
                    hp = max_hp
                print("Megittad a gyógyitalt! A hp-d most", hp)
            else:
                print("Kereskedő: Nincs elég aranyad.")
        elif vasarlas == 4:
            print("Kereskedő: Szia!")
        else:
            print("Kereskedő: Ilyen nincs.")
    print(days, ". napod ért véget.")