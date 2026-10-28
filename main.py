# on importe nos variables : hero, akatsuki, classement, TeamPlayer depuis db_init
from db_init import hero, akatsuki, classement, TeamPlayer, PseudoDB
# on importe la fonction StartFight de la logic de jeu de gameLogic
from gameLogic import UpdatePhase
import sys  

from gameData import hero_list, akatsuki_list, TeamPlayer_list





Menu = [
    "1 - lancer le jeu",
    "2 - afficher les scores",
    "3 - quitter"
]

def ShowMenu():
    for i in Menu:
        print(i)
        print("veuillez choisir une option")
    NavigateMenu()



def NavigateMenu():
    choice = IsValidChoice()
    if int(choice) == 1:
        StartGame()
    # if int(choice) == 2:
    #     # ShowRank()
    if int(choice) == 3:
        Leave()

    
def IsValidChoice():
    while True:
        PlayerChoice = input("Entrez votrez choix : ")
        if PlayerChoice.isdigit() and 1 <= int(PlayerChoice) <= 3:
            return int(PlayerChoice)
        else:
            print(f"le choix {PlayerChoice} n'est pas proposé, veuillez choisir de nouveau")
            
   
   

def StartGame():
    pseudo = ChoosePseudo(1, 10)
    SelectTeam()
    UpdatePhase()  
    
     
   
def ChoosePseudo(min_longueur, max_longeur):
    print(f"Entrez un pseudo entre {min_longueur} et {max_longeur}")
    while True:
        PseudoInput = input("Votre pseudo : ")
        Isvalid = IsPseudoValid(PseudoInput, min_longueur, max_longeur)
        if Isvalid:
            print(f"le pseudo choisi est : {PseudoInput} ") 
            PseudoDB.delete_one({}) # // + on supp le pseudo existant de la db
            PseudoDB.insert_one({ "pseudo": PseudoInput}) # // + ajout du pseudo dans la db
            print("pseudoAJouté")
            return PseudoInput 
            
                
def IsPseudoValid(PseudoInput, min_longueur, max_longeur):
        if not PseudoInput.isalpha(): # alpha pour voir si tout les charactere sont des lettre et pas des chiffres
            print("seuls les lettres sont accepté")
            return False
        if not (min_longueur <= len(PseudoInput) <= max_longeur):
            print(f"le pseudo doit etre compris entre {min_longueur}et {max_longeur} characteres ")
            return False
        return True
        
            
    
def SelectTeam():
    TeamPlayer_list.clear()
    remainingHero = 3
    while remainingHero > 0:
        succes = SelectHeroInList()  
        if succes:
            remainingHero -= 1
    print("votre equipe :")
    for i in TeamPlayer_list:
        print(i)
        
    
def SelectHeroInList():
    print("La liste des heros : ")
    for i in hero_list:
        
        print(i)
        
    HeroSelected = input("choissisez un hero : ")
    HeroToFind = IsHeroValid(HeroSelected)
    
    if HeroToFind:
        TeamPlayer_list.append(HeroToFind)
        hero_list.remove(HeroToFind)
        # // ! modifier cette partie pour mettre une comparaison entre teamPlayer et hero       
        print(f"le hero {HeroSelected} a été ajouté a votre team ")
        return True
    else:
        print("le hero n'existe pas")
        return False
        
    
def IsHeroValid(HeroSelected):
    for i in hero_list:
        if i.get("nom") == HeroSelected:
            return i.copy()
    return None
        
        
def Leave():
    sys.exit()
    

# // : NavigateMenu() 
    #Choix = // - IsValidChoice() 
    # if int(Choix) = 1 
        # // - StartGame()
    # if int(Choix) = 2
        # // - ShowRank()
    # if int(Choix) = 3
        # // - Leave()
   

# // : IsValidChoice()
    # PlayerChoice = input("votre choix =>")
    # if PlayerChoice.isdigit() and 1 <= PlayerChoice <= 3
        # return PlayerChoice
    #  # else 
        # return false et choisir de nouveau (avec un print comme quoi c'est pas un choix valide)


# //: Leave()
    # print ( vous allez quitter le jeu)
    # quit()
    
    
# //: ShowRank()
    # Utiliser la variable classement pour print le classement (les trois premier dans l'ordre decroissant avec pseudo et vague)
    # option pour revenir au menu ? ou se fait dircetement ( NavigateMenu())
    
# //: StartGame
    #// - pseudo = ChoosePseudo(min_longeur, max_longeur)
    #// - SelectTeam()
    #// - UpdatePhase() 
    # // + liaison a gameLogic

# // : ChoosePseudo(min_longeur, max_longeur)
    #print("Entrez votre pseudo entre {min_longeur} et {max_longeur}")
    #while true :
        # PseudoInput = input(votre nom =>)
        # if // - IsPseudoValide(PseudoInput, min_longeur, max_longeur)
            # on print (votre pseudo est => PSeudoInput)
            # // on ajoute notre pseudo a notre db dans la table classement 
            # on return pseudo
        # else 
            # on print de choisir un nom valide si faux 
    
# // : IsPseudoValide(PseudoInput, min_longeur, max_longeur)
    # on verifie s'il y a des chiffres avec .isnumeric
        # si Oui alors :
            # on print d'écrire avec des lettres et pas des chiffres
            # on return false 
        # si la lenght de PseudoInput est plus petite que min_longeur ou plus grand que max_longeur alors
            # on print que le pseudo doit etre compris entre {min_longeur} et {max_longeur}
            # on return False 
        # si tout est valide, on return true

    
    
# // : SelectTeam()
    # RemainingHero = 3
    # while RemainingHero > 0
        # RemainingHero -= 1
        # // - SelectHeroInList()   
    # // - ShowTeam()
        
        
        
# // : SelectHeroInList()
    # // - PrintAvailableHero()
    # while true
        # HeroSelected = input("Choisissez un hero")
        # HeroIsValid = // - IsHeroValid(HeroSelected) 
            # if HeroIsValid 
                # HeroToFind = chercher le héro dans la liste ( qui a déja été vérifier)
                # print ("{HeroSelected} a été ajouté à votre Groupe")
                # // -AddHeroToTeam(HeroSelected)
                # // -RemoveHeroFromTable(HeroSelected)
            # else 
                # print("le héro n'est pas dans liste ")
             
        
        
# // : PrintAvailableHero()
    # print (nombre de hero restant à choisir)
    # boucle pour chaque charactere dans ma liste de charactere 
        # print (character)
    
# // : IsHeroValid(HeroSelected)
    # HeroInDB = chercher la variable HeroSelected dans la db 
    # if HeroInDB 
        # return True
    # else 
        # return False  


# // : AddHeroToTeam(HeroSelected)
    # ajouter le hero a notre table TeamPlayer

# // : RemoveHeroFromTable(HeroSelected)
    # supp le héro de la table hero
    
        
# // : ShowTeam()
    # print (votre team est : {TeamPlayer})
    




ShowMenu()