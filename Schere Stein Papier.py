import random

options = ("Stein", "Papier", "Schere")

running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Was nimmst du (Stein, Schere, Papier): ")

    print(f"Spieler: {player}")
    print(F"Computer: {computer}")

    if player == computer:
        print("Unentschieden")
        
    elif player == "Stein" and computer == "Schere":
        print("Du hast gewonnen! :)")
    elif player == "Papier" and computer == "Stein":
        print("Du hast gewonnen! :)")
    elif player == "Schere" and computer == "Papier":
        print("Du hast gewonnen! :)")
    else:
        print("Du hast verloren! :(")

        
