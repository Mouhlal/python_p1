import random

def jeu_devinette():
    nombre_secret = random.randint(1, 100)
    tentatives = 0

    print("Bienvenue au jeu de devinette!")
    print("Je pense à un nombre entre 1 et 100. Essayez de deviner!")

    while True:
        tentative = int(input("Entrez votre devinette: "))
        tentatives += 1

        if tentative < nombre_secret:
            print("Trop bas! Essayez encore.")
        elif tentative > nombre_secret:
            print("Trop haut! Essayez encore.")
        else:
            print(f"Félicitations! Vous avez deviné le nombre en {tentatives} tentatives.")
            break

jeu_devinette()
