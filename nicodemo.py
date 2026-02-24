# Verifica su File e JSON 

# Consegna
# Consegna un singolo file Python rinominato come `cognome.py` (es. `rossi.py`).
# Testa il codice eseguendolo in terminale con `python cognome.py`.

# ---

# ## Esercizio: Gestione Biblioteca

# Stai costruendo un sistema per gestire una piccola biblioteca.
# I dati di partenza sono da definire hardcoded nel `main()`:

# python
# libri = [
#     {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
#     {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
#     {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
#     {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
# ]

# Punto A – Salvataggio e caricamento JSON 

# 1. Definisci `salva_biblioteca(libri: list[dict], nome_file: str) -> None`:
#    Salva la lista in formato JSON con indentazione. Stampa un messaggio di conferma.

# 2. Definisci `carica_biblioteca(nome_file: str) -> list[dict]`:
#    Carica e restituisce la lista da JSON.
#    Se il file non esiste, stampa un messaggio di errore e restituisce `[]`.

import json

def salva_biblioteca(libri: list[dict], nome_file: str) -> None:
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            json.dump(libri, file, indent = 4)
            print(f"{nome_file} scritto con successo")
    except IOError as e:
        print(f"Errore durante la scrittura del file: {e}")

def carica_biblioteca(nome_file: str) -> list[dict]:
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            libri_caricati = json.load(file)
            return libri_caricati
    except FileNotFoundError:
        print(f"Errore il {nome_file} non è stato trovato")
        return []
    except json.JSONDecoderError as e:
        print(f"Errore nel parsing JSON: {e}")
        return []

# Punto B – Filtro per genere

# 1. Definisci `filtra_per_genere(libri: list[dict], genere: str) -> list[dict]`:
#    Restituisce una nuova lista con solo i libri il cui campo `"genere"` corrisponde a quello passato.

def filtra_per_genere(libri: list[dict, genere: str]) -> list[dict]:
    libri_filtrati = []
    for libro in libri:
        if libro['genere'] == genere:
            libri_filtrati.append(libro)
    return libri_filtrati

# Punto C – Statistiche 

# 1. Definisci `calcola_media_anno(libri: list[dict]) -> float`:
#    Restituisce la media degli anni di pubblicazione come `float`.
#    Se la lista è vuota, restituisce `0.0`.

# 2. Definisci `trova_libro_piu_recente(libri: list[dict]) -> dict | None`:
#    Restituisce il dizionario del libro con l'anno più alto.
#    Se la lista è vuota, restituisce `None`.

def calcola_media_anno(libri: list[dict]) -> float:
    if libri == []
        return 0.0
    else:
        totale = 0.0
        for libro in libri:
            totale = totale + libro['anno']
        media = totale/(len(libri))
        return media

def trova_libro_piu_recente(libri: list[dict]) -> dict | None:
    if libri == []:
        return None
    else:
        libro_indice = +float("inf")
        for libro in libri:
            if libro['anno'] < libro_indice:
                libro_indice = libro
        return libro_indice

# Punto D – Conta libri per genere

# 1. Definisci `conta_per_genere(libri: list[dict]) -> dict[str, int]`:
#    Restituisce un dizionario dove le chiavi sono i generi e i valori sono il numero di libri per genere.

def conta_per_genere(libri: list[dict]) -> dict[str, int]:
    dizionario_conta_genere = {}
    for libro in libri:
        if libro['genere'] in dizionario_conta_genere:
            dizionario_conta_genere[libro['genere']] += 1
        else:
            dizionario_conta_genere[libro['genere']] = 1
    return dizionario_conta_genere

# Punto E – Bonus: Modifica anno di un libro 

# Definisci `modifica_anno_libro(libri: list[dict], titolo: str, nuovo_anno: int) -> tuple[bool, str, list[dict]]`:
# - Trova il libro con quel titolo (ricerca esatta) e aggiorna l'anno.
# - Restituisce una tupla `(success, messaggio, libri_modificati)` dove `success` è `True` se il libro è stato trovato e modificato, altrimenti `False`. La lista modificata è sempre restituita.

def ricerca_per_nome(libri):
    #     termine = input("Termine di ricerca: ").strip().lower()
    # if not termine:
    #     print("Errore: termine non valido")
    #     return

    # risultati = []
    # for libro in libri:
    #     nome_lower = libro["nome"].lower()
    #     if termine in nome_lower:
    #         risultati.append(libro)

    # if not risultati:
    #     print("Nessuno studente trovato.")
    #     return

    # print(f"Trovato(i) {len(risultati)} risultato(i):")
    # # for libro in libri:
    # #     print(f"{libro['nome']} - Voto: {libro['voto']}")

def modifica_anno_libro(libri: list[dict, titolo: str, nuovo_anno: int]) -> tuple[bool, str, list[dict]]:
    pass

# Nel `main()`:
# - Chiama `salva_biblioteca` per salvare su `"biblioteca.json"`.
# - Chiama `carica_biblioteca` e stampa quanti libri sono stati caricati.

# Esempio di output:
# File 'biblioteca.json' salvato con successo.
# Libri in archivio: 4

# Nel `main()`:
# - Usa i libri caricati nel Punto A.
# - Filtra per `"Fantascienza"` e stampa quanti ne hai trovati e i loro titoli.

# Esempio di output:
# Libri di Fantascienza: 2
# - 1984
# - Dune

# Nel `main()`:
# - Chiama entrambe le funzioni sui libri caricati e stampa i risultati.

# Esempio di output:
# Media anno di pubblicazione: 1963.5
# Libro più recente: Harry Potter (1997)

# Nel `main()`:
# - Chiama la funzione sui libri caricati.
# - Stampa il risultato ordinato per genere (alfabetico).

# Esempio di output:
# Libri per genere:
# Fantasy: 1
# Fantascienza: 2
# Romanzo: 1

# Nel `main()`, dopo il Punto D:
# - Chiedi all'utente un titolo e un nuovo anno.
# - Chiama `modifica_anno_libro` e stampa il messaggio.
# - Se la modifica è riuscita, richiama `salva_biblioteca` per salvare le modifiche su `"biblioteca.json"`.

# Esempio di interazione:
# Inserisci titolo da modificare: 1984
# Inserisci nuovo anno: 1950
# Libro '1984' aggiornato con anno 1950. Totale libri: 4

# Se il libro non esiste:
# Inserisci titolo da modificare: Titanic
# Libro 'Titanic' non trovato.

def main():
    libri = [
     {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
     {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
     {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
     {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
     ]
    nome_file = "biblioteca.json"
    salva_biblioteca(libri, nome_file)
    biblioteca_caricata = carica_biblioteca(nome_file)
    print(f"Libri in archivio: {len(biblioteca_caricata)}")
    if biblioteca_caricata:
        fantascienza = filtra_per_genere(biblioteca_caricata, "Fantascienza")
        print(f"Libri di Fantascienza: {len(fantascienza)}")
        for i in range(len(fantascienza)):
            print(fantascienza['titolo'])
        media_anno = calcola_media_anno(biblioteca_caricata)
        print(f"Media anno di pubblicazione: {media_anno}")
        libro_più_recente = trova_libro_piu_recente(biblioteca_caricata)
        print(f"Libro più recente: {libro_più_recente['titolo']} ({libro_più_recente['anno']})")
        generi_dizionario = conta_per_genere(biblioteca_caricata)
        print(f"(generi_dizionario)\n")
        titolo: str = str(input("Inserisci titolo da modificare: "))
        nuovo_anno: int = int(input("Inserisci anno da modificare: "))