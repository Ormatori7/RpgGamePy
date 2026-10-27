# on importe nos variables : hero, akatsuki, classement, TeamPlayer depuis db_init



# // : UpdatePhase()
    # CurrentEnnemy = // - ChooseRandomEnemy()
    #// - ShowCurrentEnnemy(CurrentEnnemy)
    #// - Fight(CurrentEnnemy)
    
    
    
# // : WaveIncrement()
    # on incremente la vague actuel de 1 ( en partant de 0 pour la premiere fois)
    # on return le resultat 
    
# // : ShowCurrentWave(CurrentWave)
    # on print la CurrentWave
    
# // : ChooseRandomEnemy()
    # on recupere la table akatsuki
    # on en choisi 1 avec du random
    # on return le perso choisi avec ses stats 
    
#// : ShowCurrentEnnemy(CurrentEnnemy)
    # on print le current ennemy que l'on va affronter 
    

#// : Fight(CurrentEnnemy)
    # check si au moins 1 hero a > 0 hp 
        # si oui alors 
            # CurrentWave = // - WaveIncrement()
            # // - ShowCurrentWave(CurrentWave)
            # // - HeroAttack(CurrentEnnemy)
            # // - EnnemyAttack(TeamPlayer)
        # si non alors 
            # // - EndScreen()
            # // - SaveScore()
    
    
    
# // : HeroAttack(CurrentEnnemy)
    # boucle foreach hero dans TeamPlayer (on ne compte pas ceux qui sont mort)
        # on recup les dégats du héro
        # on attaque le monstre
        # on verifie si le monstre est toujours en vie
            # si oui alors 
                # continue
            # si non alors
                # break
        
    
# // : CheckIfEnnemyAlive(CurrentEnnemy)
    # simple si CurrentEnnmy (vie) > 0
        # return True
    # sinon
        # return False
        
# // : EnnemyAttack(TeamPlayer)
    # for hero in TeamPlayer
        # on verifie que hero a health > 0
            # si c'est vrai 
            # le monstre attaque hero
            # on update la db avec le hero et sa nouvelle vie (dans TeamPlayer)
        # sinon
            # // - RemoveDeadHero()
            # on continue au prochain hero 
    
# // : RemoveDeadHero()
    # 
    
# // : MenuFin()
