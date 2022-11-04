import random
import subprocess as subpcs

#Création des listes d'objets jouables
listshifoumi = ['pierre', 'rock', 'caillou', 'papier', 'feuille', 'paper', 'ciseaux', 'scissors']
listpapier = ['papier', 'feuille', 'paper']
listpierre = ['pierre', 'rock', 'caillou']

#Normalisation des valeurs
def val (a):
    if a in listpierre:
        b =  1
    elif a in listpapier:
        b = 2
    else:
        b = 3
    return b

ordinb = 0

#Choix du GameMode   

gamemode = input("in what gamemode do you wish to play in ?" '\n' "1) Singleplayer" '\n' "2) Multiplayer" '\n')

subpcs.run("clear")

if gamemode == "1":
    ordinb = random.randint(1,3)
    Player1 = (input('\n'"Player 1 : what will you play ?"'\n'))
    if Player1.lower() not in listshifoumi:
        raise NameError("wrong value")
elif gamemode == "2":

    #Récupérations des valeurs de jeux via le joueur et test préliminaires de correspondances
    Player1 = (input("Player 1 : what will you play ?"'\n'))
    if Player1.lower() not in listshifoumi:
        raise NameError("wrong value")

    subpcs.run("clear")

    Player2 = (input("Player 2 : what will you play ?"'\n'))
    if Player2.lower() not in listshifoumi:
        raise NameError("wrong value")

    subpcs.run("clear")
else:
    raise NameError("Wrong value")

#Passage des valeurs vérifiée en minuscules

Player1l = Player1.lower()
play1 = val(Player1l)

if gamemode == 2:
    Player2l = Player2.lower()
    play2 = val(Player2l)
else:
    play2 = ordinb


#Détermination du vainqueur
if (((play1 == 1) and (play2 == 3)) or ((play1 == 3) and (play2 == 2)) or ((play1 == 2) and (play2 == 1))):
    print("Player 1 wins")
elif (play1 == play2):
      print("Draw")
else:
      print("Player 2 wins")
