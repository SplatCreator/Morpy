print("selem aleykoum, welcome sur Tic Tac Toe")
print(" ")

etages =["-","-","-",
         "-","-","-",
         "-","-","-"]
#afficher la pputin de grilleeeeee
def grille():
    print(etages[6] + " | " + etages[7] + " | " + etages[8])
    print("---------")
    print(etages[3] + " | " + etages[4] + " | " + etages[5])
    print("---------")
    print(etages[0] + " | " + etages[1] + " | " + etages[2])

def gagnant(etages):
    # colonne ligne diago check
    if etages[0] == etages[1] == etages[2] != "-":
        return True
    elif etages[3] == etages[4] == etages[5] != "-":
        return True
    elif etages[6] == etages[7] == etages[8] != "-":
        return True
    elif etages[0] == etages[3] == etages[6] != "-":
        return True
    elif etages[1] == etages[4] == etages[7] != "-":
        return True
    elif etages[2] == etages[5] == etages[8] != "-":
        return True
    elif etages[0] == etages[4] == etages[8] != "-":
        return True
    elif etages[2] == etages[4] == etages[6] != "-":
        return True
    return False

def rejouer(): #go rejouer le sang
    reponse = input("Voulez-vous rejouer ? (yes/no) : ").lower()
    if reponse in ["yes", "y", "oui"]:
        return True
    else:
        return False

Player1 = input("Choisissez votre symbole (X ou O) : ") 
if Player1 == "X":
    Player2 = "O"
else:
    Player1 = "O"
    Player2 = "X"

partie_en_cours = True 
while partie_en_cours:
    tour = 0
    etages = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    
    while True:
        grille()
        joueur_actuel = Player1 if tour % 2 == 0 else Player2
        print(f"C'est au tour de {joueur_actuel} de jouer.")
        
        choix = int(input("Choisissez une case (1,9) : ")) - 1
        if etages[choix] == "-":
            etages[choix] = joueur_actuel
            tour += 1 
        else:
            print("Case occupée, choisissez une autre case.")
            continue
        
        if gagnant(etages):
            grille()
            print(f"Bravo,{joueur_actuel} tu as gagné !")
            break
        elif "-" not in etages:
            grille()
            print("Match nul !")
            break
    if not rejouer():
        partie_en_cours = False
        