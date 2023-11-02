def berechne_note(note, wetter, betriebssystem):
    pass


import csv
import random


# Funktion zur Berechnung der angepassten Note
def berechne_note(wetter, betriebssystem):
    wetter_anpassung = {
        "wolkig": 0.0,
        "sonnig": -0.3,
        "regnerisch": +0.3,
        "stürmisch": +0.6,
    }

    os_anpassung = {
        "Linux": -1.0,
        "Windows": +0.3,
        "Mac": +1.0,
    }

    angepasste_note = 3.0  # Die Variable angepasste_note ist zu Beginn des Codes auf den Wert 3.0 gesetzt, um eine anfängliche oder Standardbewertung zu definieren. Dieser Wert dient als Grundlage, auf der die weiteren Anpassungen basieren

    if wetter in wetter_anpassung:
        angepasste_note += wetter_anpassung[wetter]
    if betriebssystem in os_anpassung:
        angepasste_note += os_anpassung[betriebssystem]

    return angepasste_note


# Einmalig nach dem aktuellen Wetter fragen.
wetter = input("Wie ist das Wetter heute? z.B.: 'wolkig', 'sonnig', 'regnerisch', 'stürmisch': ")

# Die Daten der Studierenden für die CSV-Datei definieren.
studentendaten = [
    ["Name", "Betriebssystem"],
    ["Student1", "Linux"],
    ["Student2", "Windows"],
    ["Student3", "Mac"],
]

# Erzeuge zufällige Noten für die Studierenden
for student in studentendaten[1:]:
    student.append(round(random.uniform(1.0, 5.0), 1))

# Den Dateinamen für die CSV-Datei angeben.
dateiname = "studentendaten.csv"

# Die Studentendaten in die CSV-Datei schreiben.
with open(dateiname, mode='w', newline='') as csvdatei:
    schreiber = csv.writer(csvdatei)
    schreiber.writerows(studentendaten)

print(f"CSV-Datei '{dateiname}' erfolgreich erstellt.")

# Die angepassten Noten berechnen und ausgeben.
for datensatz in studentendaten[1:]:
    name = datensatz[0]
    betriebssystem = datensatz[1]

    angepasste_note = berechne_note(wetter, betriebssystem)
    print(f"{name}: Die angepasste Note beträgt: {angepasste_note:.1f}")