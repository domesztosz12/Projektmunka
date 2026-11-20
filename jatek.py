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
