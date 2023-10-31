
# Aufgabenteil (a)

def berechne_note(wetter, betriebssystem, note):
    #Wetterbedingungen als Einfluss
    if wetter == "sonnig":
        note =- 0.3
    if wetter == "regnerisch":
        note =+ 0.3
    if wetter == "stürmisch":
        note =+ 0.6

    #Betriebssystem als Einfluss
    if betriebssystem == "Linux":
        note =- 1.0
    if betriebssystem == "Windows":
        note =+ 0.3
    if betriebssystem == "Mac":
        note =+ 1.0

    return note

#________________________________________________________________
#Aufgabenteil (b)

import csv

wetter = input("Wie ist das Wetter heute so? (Auswahl zwischen: sonnig, wolkig, regnerisch, stürmisch): ")
csv_datei = input("Bitte geben Sie den Dateinamen der CSV-Datei ein: ")

try:
    with open(csv_datei, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

        for row in csv_reader:
            name, note, bs = row
            note = float(note)
            neue_note = berechne_note(wetter, bs, note)
            print(f"{name}: Neue Note - {neue_note:.1f}")

except FileNotFoundError:
    print(f"Die Datei {csv_datei} wurde nicht gefunden, überprüfe nochmal deine Eingabe.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {str(e)}")

#________________________________________________________________________
#Aufgabenteil(c)
#Die Abgabe der Studierenden an sich zu benoten ist eigentlich auch viel zu viel Arbeit.
#Streicht die ursprüngliche Note aus der csv Datei und schreibt das Programm so um,
#dass die ursprüngliche Note einfach gewürfelt wird.  Das Wetter und das
#Betriebssystem haben weiterhin die gleiche Auswirkung wie bisher.


import csv
import random

wetter = input("Wie ist das Wetter heute so? (Auswahl zwischen: sonnig, wolkig, regnerisch, stürmisch): ")
csv_datei = input("Bitte geben Sie den Dateinamen der CSV-Datei ein: ")
output_csv_datei = "result_" + csv_datei

try:
    with open(csv_datei, 'r') as input_datei, open(output_csv_datei, 'w', newline='') as output_datei:
        csv_reader = csv.reader(input_datei)
        header = next(csv_reader)

        rows = []
        csv_writer = csv.writer(output_datei)
        csv_writer.writerow(header)

        for row in csv_reader:
            name, _, bs = row  # Die eigentliche Note wird nicht aus der CSV-Datei gelesen
            ursprungs_note = random.uniform(1, 5)
            result_note = berechne_note(wetter, bs, ursprungs_note)
            csv_writer.writerow([name, result_note, bs])
            rows.append([name, result_note, bs])

    print(f"Die Ergebnisse wurden in die Datei '{output_csv_datei}' geschrieben.")

except FileNotFoundError:
    print(f"Die Datei {csv_datei} wurde nicht gefunden, check deine Eingabe nochmal.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {str(e)}")