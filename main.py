# on importe nos variables : hero, akatsuki, classement, TeamPlayer depuis db_init
# on importe la fonction StartFight de la logic de jeu de gameLogic


# MENU = [
#           "1 -lancer le jeu",
#           "2 - afficher les scores"
#           "3 - Quitter",
# ]



#//: ShowMenu()
    # for i in MENU 
        # print(i)
    # Choisir une option"
    # // - NavigateMenu()
    
    
    
# // : NavigateMenu() 
    #Choix = // - ChoiceValid() 
    # if int(Choix) = 1 
        # // - StartGame()
    # if int(Choix) = 2
        # // - ShowRank()
    # if int(Choix) = 3
        # // - Leave()
   

# // : ChoiceValid()
    # ChoixJoueur = input("votre choix =>")
    # if ChoixJoueur.isdigit() and 1 <= choixJoueur <= 3
        # return ChoixJoueur
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
    

