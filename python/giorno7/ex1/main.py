import random
import json
import datetime

def indovina_il_numero():
    numero_da_indovinare = random.randint (1, 100)
    tentativi = 0
    high_scores = load_high_scores()

    print("benvenuto! Indovina il numero tra 1 e 100")

    while True:
        user_input =input("inserisci il numero: ")
        try:
            numero_ut = int(user_input)
        except ValueError:
            print("input errato, riprova!")
        continue

        tentativi += 1

        numero_ut = int(user_input)

        if numero_ut < numero_da_indovinare:
            print ("numero troppo basso!")
        elif numero_ut > numero_da_indovinare:
            print ("numero troppo alto!")
        else:
            print ("Bravo! hai indovinato !!\n Ti meriti un premio!")

            break

        indovina_il_numero()