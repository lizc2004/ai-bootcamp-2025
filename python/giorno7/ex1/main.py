import random
import json
import datetime


# Funzione per caricare i punteggi salvati
def load_high_scores():
    try:
        with open("high_scores.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Funzione per salvare i punteggi
def save_high_scores(high_scores):
    with open("high_scores.json", "w") as file:
        json.dump(high_scores, file, indent=4)


# Gioco principale
def indovina_il_numero():
    numero_da_indovinare = random.randint(1, 100)
    tentativi = 0
    high_scores = load_high_scores()

    print("Benvenuto! Indovina il numero tra 1 e 100")
    start_time = datetime.datetime.now()

    while True:
        user_input = input("Inserisci il numero: ")
        try:
            numero_ut = int(user_input)
        except ValueError:
            print("Input errato, riprova!")
            continue

        tentativi += 1

        if numero_ut < numero_da_indovinare:
            print("Numero troppo basso!")
        elif numero_ut > numero_da_indovinare:
            print("Numero troppo alto!")
        else:
            print("Bravo! Hai indovinato!!\nTi meriti un premio!")
            player_name = input("Inserisci il tuo nome: ")
            current_time = datetime.datetime.now()
            time_taken = current_time - start_time
            high_scores.append({
                "name": player_name,
                "attempts": tentativi,
                "date": current_time.strftime("%Y-%m-%d %H:%M:%S"),
                "time_taken": time_taken.total_seconds()
            })
            high_scores.sort(key=lambda x: x["attempts"])
            save_high_scores(high_scores)
            break

    print("Punteggi migliori:")
    for score in high_scores:
        print(
            f"Giocatore: {score['name']}, Tentativi: {score['attempts']}, Data: {score['date']}, Tempo impiegato: {score['time_taken']} secondi")

    play_again = input("Vuoi continuare a giocare? (s/n): ")
    if play_again.lower() == 's':
        indovina_il_numero()
    else:
        print("Grazie per aver giocato!")


# Avvio del gioco
if __name__ == "__main__":
    indovina_il_numero()
