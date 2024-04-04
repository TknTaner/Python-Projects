print("Was willst du Kochen? 1: Rührei 2: Gekochte Eier 3: Sandwich")
recipe = int(input("Eingabe: "))

if recipe == 1:
    print("""Um Rührei zu machen, zerschlage die gewünschte Menge an Eiern in ein Glas oder eine Schale und verrühre sie.
Anschließend gibst du Öl oder Butter in eine Pfanne, lässt sie kurz warm werden und gibst die Eier rein.
Die Eier immer ein bisschen verrühren und nach Geschmack würzen, zum Beispiel mit Salz oder Pfeffer.""")
elif recipe == 2:
    print("""Lege die Eier in einen Topf und fülle diesen so mit Wasser, dass die Eier bedeckt sind.
Stelle den Topf auf den Herd und warte bis das Wasser kocht. Wenn das Wasser kocht startest du einen Timer.
Für weichgekochte Eier warte 5 Minuten, für hart gekochte Eier 7 Minuten und nehme die Eier dann aus dem Topf.""")
elif recipe == 3:
    print("""Nimm zwei Scheiben Toast und belege eine davon mit zum Beispiel Käse und Salami.
Leg die andere Hälfte oben drauf und gib das ganze für 30-45 Sekunden in die Mikrowelle.""")
elif recipe > 3 or recipe < 0 or recipe == 0:
    input("Ungültige Eingabe, bitte Starte das Programm neu.")
if recipe < 4 and recipe > 0:
    input("Guten Appetit!")