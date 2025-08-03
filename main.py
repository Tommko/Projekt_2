"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Tomáš Kolárik
email: kolarik-tomas@seznam.cz
"""
import random

cary = "_"*47

uvodni_zprava = f"""
Hi there!
{cary}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{cary}
"""


def generovaní_cisla():                                     #vygeneruje náhodné 4 ciferné číslo
    moznost = range(0,9,1)
    moznost_nula = range(1,9,1)

    nahodne_cislo = str(random.choice(moznost_nula))

    while len(nahodne_cislo) != 4:
        vyber = str(random.choice(moznost))
        while vyber in nahodne_cislo:
            vyber = str(random.choice(moznost))
        else:
            nahodne_cislo = nahodne_cislo + vyber

    return nahodne_cislo

def kontrola_cisla_hrace(vstup):                            #kontrola čísla zadaného uživatelem
    pomoc_unikatni_cislice = []
    for A in vstup:
        if str(vstup).count(A) > 1:
            pomoc_unikatni_cislice.append(False)
        else:
            pomoc_unikatni_cislice.append(True)
    if pomoc_unikatni_cislice.count(True) < 4:
        vystup_unikatni_cislice = False
    else:
        vystup_unikatni_cislice = True
        
    X = [len(vstup) == 4, vstup.isnumeric(), str(vstup[0]) != "0", vystup_unikatni_cislice]

    while X.count(True) != 4:
        pomoc_unikatni_cislice = []
        vstup = input("Warning! Number must be 4 digits long, can't contain duplicates, letters or start with 0!: ")
        for A in vstup:
            if str(vstup).count(A) > 1:
                pomoc_unikatni_cislice.append(False)
            else:
                pomoc_unikatni_cislice.append(True)
        if pomoc_unikatni_cislice.count(True) < 4:
            vystup_unikatni_cislice = False
        else:
            vystup_unikatni_cislice = True
        X = [len(vstup) == 4, vstup.isnumeric(), str(vstup[0]) != "0", vystup_unikatni_cislice]
    else:
        vstup = vstup
    return vstup
                                 
def bullsy(bullos):                                         #jednotné/množné číslo pro býky
    if bullos > 1:
        pocet_1 = "bulls"
    else:
        pocet_1 = "bull"
    return pocet_1

def cowsy(cowos):                                           #jednotné/množné číslo pro krávy
    if cowos > 1:
        pocet_2 = "cows"
    else:
        pocet_2 = "cow"
    return pocet_2

def pocitani(kauntr):
    if kauntr > 1:
        countr = "gueses!"
    else:
        countr = "guess!"
    return countr


cislo_pocitace = str(generovaní_cisla())

print(uvodni_zprava)

vstup = input("Insert number please: ")

cislo_hrace = str(kontrola_cisla_hrace(vstup))


pocet_bullu = 0
pocet_cowsu = 0
i = 0
counter = 1

while pocet_bullu < 4:
    
    pocet_bullu = 0
    pocet_cowsu = 0
    i = 0
    
    for A in cislo_hrace:
        if A == cislo_pocitace[i]:
            pocet_bullu = pocet_bullu + 1
            i = i + 1   
        elif A in cislo_pocitace:
            pocet_cowsu = pocet_cowsu + 1 
            i = i + 1

    print(pocet_bullu, bullsy(pocet_bullu), "," , pocet_cowsu, cowsy(pocet_cowsu))
    if pocet_bullu < 4:          
        vstup = input("Insert number please: ")

        cislo_hrace = str(kontrola_cisla_hrace(vstup))
        counter = counter + 1
else:
    print("You've won! You've made it in", counter ,pocitani(counter))