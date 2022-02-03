TEXTS = ['''
Situated about 10, miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

user_pass = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
     }
separator = "=" * 50

user = input("Zadej uzivatelske jmeno: ")
if user not in user_pass:
    print("Uzivatel nebyl nalezen. Ukoncuji.")
    quit()
else:
    password = input("Zadej heslo: ")
    if user_pass.get(user) == password:
        print("Prihlaseni probehlo v poradku.")
        if user == "bob":
            print(f"Vitejte v textovem analyzatoru, {user}e!")
        elif user == "ann":
            print(f"Vitejte v textovem analyzatoru, {user}o!")
        elif user == "mike":
            print(f"Vitejte v textovem analyzatoru, {user[:-1]}u!")
        elif user == "liz":
            print(f"Vitejte v textovem analyzatoru, {user}o!")
    else:
        print("Zadane heslo neni spravne. Ukoncuji.")
        quit()
print(separator)

cislo_textu = input("Vyberte text, ktery chcete analyzovat (1 - 3): ")

if cislo_textu.isnumeric():
    cislo_textu = int(cislo_textu)
    if cislo_textu in range(1, 4):
        vyber = TEXTS[cislo_textu - 1]
    else:
        print("Vyber mimo rozsah. Ukoncuji.")
        quit()
else:
    print("Nezadal jsi cislo. Ukoncuji.")
    quit()
print(separator)

rozdeleny_text = []
prvni_velke = []
vsechny_velke = []
vsechny_male = []
numeric = []

for slovo in vyber.split():
    rozdeleny_text.append(slovo.strip(".,:;"))
print(rozdeleny_text)

for slovo in vyber.split():
    if slovo[0].isupper():
        prvni_velke.append(slovo)
    elif slovo.isupper():
        vsechny_velke.append(slovo)
    elif slovo.islower():
        vsechny_male.append(slovo)

for slovo in rozdeleny_text:
    if slovo.isdigit():
        numeric.append(slovo)

print(f"There are {len(rozdeleny_text)} words in the selected text.")
print(f"There are {len(prvni_velke)} titlecase words.")
print(f"There are {len(vsechny_velke)} uppercase words.")
print(f"There are {len(vsechny_male)} lowercase words.")
print(f"There are {len(numeric)} numeric strings.")

soucet = 0
for cislo in range(0, len(numeric)):
    numeric[cislo] = int(numeric[cislo])
    soucet = soucet + numeric[cislo]

print(f"The sum of all the numbers {soucet}")
print(separator)

delka_slov = dict()
for slovo in rozdeleny_text:
    if len(slovo) not in delka_slov:
        delka_slov.setdefault(len(slovo), 1)
    else:
        delka_slov[len(slovo)] = delka_slov[len(slovo)] + 1

print(f"{'LEN': >3} | {'OCCURENCES': ^26} | {'NR.': <3}")

for slovo in sorted(delka_slov):
    print(f"{slovo: >3} | {'*' * delka_slov[slovo]: <25}  | {delka_slov[slovo]: <3}")
print(separator)
