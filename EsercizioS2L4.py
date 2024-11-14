import math

def calcola_perimetro():
    # Mostra il menu di scelta all'utente
    print("Scegli la figura per cui calcolare il perimetro:")
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo")

    # Chiedi all'utente di scegliere una figura
    scelta = input("Inserisci il numero corrispondente alla tua scelta (1, 2 o 3): ")

    if scelta == "1":
        # Perimetro del quadrato
        lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
        perimetro = 4 * lato
        print(f"Il perimetro del quadrato è: {perimetro}")
        
    elif scelta == "2":
        # Perimetro del cerchio
        raggio = float(input("Inserisci il raggio del cerchio: "))
        perimetro = 2 * math.pi * raggio
        print(f"Il perimetro (circonferenza) del cerchio è: {perimetro}")
        
    elif scelta == "3":
        # Perimetro del rettangolo
        lunghezza = float(input("Inserisci la lunghezza del rettangolo: "))
        larghezza = float(input("Inserisci la larghezza del rettangolo: "))
        perimetro = 2 * (lunghezza + larghezza)
        print(f"Il perimetro del rettangolo è: {perimetro}")
        
    else:
        print("Scelta non valida. Riprova inserendo 1, 2 o 3.")

# Esegui la funzione
calcola_perimetro()