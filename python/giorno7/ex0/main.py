import csv
# Funzione per leggere i dati dal file csv
def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
            return data
# Funzione per scrivere i dati ordinati in un nuovo file csv
def write_data(file_path, data):
    with open(file_path, 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

# Caricamento dei dati dal file csv
data = load_data("data.csv")

#Riorganizzare delle righe in prdine alfabetico crescente per cognome
data_sorted = sorted(data[1:], key=lambda x: x[2]) #assume che il cognome sia nella terza colonna

# Aggiunta dell'indice sequenziale a ciascuna riga
data_with_index = [[i+1] + row for i, row in enumerate(data_sorted)]

# Stampa le righe ordinate con l'indice
for row in data_with_index:
    print(row)

#scrivere i dati ordinati in un nuovo file csv senza l'indice
write_data('data2.csv', data_sorted)

#Bonus
#riorganizzare delle righe in ordine alfatetico crescente per cognome e poi per nome
data_sorted = sorted(data[1:], key=lambda x: (x[2], x[1]))

#aggiunta dell'indice sequenziale a ciascuna riga
data_with_index = [[i+1] + row for i, row in enumerate(data_sorted)]

#stampa le righe ordinate con l'indice
for row in data_with_index:
    print(row)

#scrivere i dati ordinati in un nuovo file csv senza l'indice
write_data('data2.csv', data_sorted)

