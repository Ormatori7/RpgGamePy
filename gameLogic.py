# on importe nos variables : hero, akatsuki, classement, TeamPlayer depuis db_init
from db_init import hero, akatsuki, classement, TeamPlayer, PseudoDB


def UpdatePhase():
    currentEnemy = ChooseRandomEnemy()
    Fight(currentEnemy)
    
    
def ChooseRandomEnemy():
    cursor = akatsuki.aggregate([{"$sample": {"size": 1}}, {"$project": {"_id": 0, "id": 0}},])
    RandomEnemy = list(cursor)
    print(f" le membre de l'akatsuki est {RandomEnemy}")
    return RandomEnemy



def Fight(currentEnemy):
    StillStanding = TeamStillAlive()
    if StillStanding:
        print("on continue le combat")
        CurrentWave = WaveIncrement()
        # // - ShowCurrentWave(CurrentWave)
        # // - HeroAttack(CurrentEnnemy)
        # // - EnnemyAttack(TeamPlayer)
    else:
        print("fin du combat")
        #endscreen
        #score()
    
    
def TeamStillAlive():
    for i in TeamPlayer.find():
        if i.get("hp", 0) > 0:
            return True
        return False
    
    
    
def WaveIncrement():
    wave = 1
    
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
    # check si au moins 1 hero a > 0 hp ( au niveau de la db) 
    # TeamStillAlive = // - TeamStillAlive()
        # si oui alors 
            # CurrentWave = // - WaveIncrement()
            # // - ShowCurrentWave(CurrentWave)
            # // - HeroAttack(CurrentEnnemy)
            # // - EnnemyAttack(TeamPlayer)
        # si non alors 
            # // - EndScreen()
            # // - SaveScore()
    
    
    
# // : TeamStillAlive()
    # for each hero in table hero
        # regarder si au moins 1 hero a vie > 0
            # si oui alors :
                # return true (au moins 1 héro en vie)
            # si non alors
                # return false (tout les heros sont mort)
    
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
    # si CurrentEnnmy (vie) > 0
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
            # on continue au prochain hero 
            # // ! besoin d'une logique pour si all hero dead alors on s'arrete 
    

    
# // : EndScreen()
    # afficher la vague et le pseudo
    

# // : SaveScore()
    # enregistrer dans la db dans la partie classement le nombre de vague et le nom   