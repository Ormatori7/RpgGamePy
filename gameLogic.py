# on importe nos variables : hero, akatsuki, classement, TeamPlayer depuis db_init
from db_init import hero, akatsuki, classement, TeamPlayer, PseudoDB
from gameData import hero_list, akatsuki_list, TeamPlayer_list
import random


def UpdatePhase():
    currentEnemy = ChooseRandomEnemy()
    Fight(currentEnemy)
    
    
def ChooseRandomEnemy():
    
    if akatsuki_list: # si liste pas vide alors 
        enemy = random.choice(akatsuki_list).copy()
        print(f" le membre de l'akatsuki est {enemy}")
        return enemy
    return None 



def Fight(currentEnemy):
    print(f"l'ennemi est {currentEnemy}") # // ! test pour l'instant
    # CurrentWave = WaveIncrement()
    while TeamStillAlive() and currentEnemy.get("hp", 0) > 0:
        HeroAttack(currentEnemy)
        if currentEnemy.get("hp", 0) > 0:
            # // ! EnnemyAttack(TeamPlayer)
            pass
    if TeamStillAlive():
        print("l'equipe a gagner")
        #endscreen
        #score()
    else:
        print("l'ennemi a gagner ")
        
    
    
def TeamStillAlive():
    for i in TeamPlayer_list:
        if IsHeroStillAlive(i):
            return True
    return False
       
    
def IsHeroStillAlive(CurrentHero):
    if CurrentHero.get("hp", 0) > 0:
        return True
    return False
        

def WaveIncrement(currentWave):
    currentWave += 1
    ShowCurrentWave(currentWave)
    return currentWave


def ShowCurrentWave(Wave):
    print(f"la vague actuel est la vague {Wave}")
    
    
def HeroAttack(currentEnemy):
    for i in TeamPlayer_list:
        CanAttack = IsHeroStillAlive(i)
        if CanAttack:
            damageToDeal = i.get("atk", 0) # renvoie 0 si n'existe pas
            print(f"le hero {i} attaque de {damageToDeal} dégats !!")
            EnemyTakeDamage(damageToDeal, currentEnemy)
                
        else:
            print("le hero est mort, il ne peut donc pas attaquer")
            
    EnenyAttack()
        
    
def EnemyTakeDamage(Damage, Enemy):
    EnemyHealth = Enemy.get("hp", 0)
    EnemyDefense = Enemy.get("def", 0)
    
    DamageTaken = Damage - EnemyDefense
    if DamageTaken < 0:
        DamageTaken = 0
    
    Enemy["hp"] = EnemyHealth - DamageTaken    
    if Enemy["hp"] < 0:
        Enemy["hp"] = 0
    print(f"l'ennemi a encore {Enemy["hp"]} de vie")
        
    return Enemy

    
    
def EnemyAttack():
    # fusion de la logique hero/ennemi plus tard
    # // ! terminer l'implémentation de l'ennemi afin de verifier s'il est vivant 
    canAttack = EnemyStillAlive()
    if canAttack:
        damageToDeal = akatsuki_list.get("atk", 0)
        HeroTakeDamage(damageToDeal)
    
def EnemyStillAlive(enemy):  
    if enemy.get("hp", 0) > 0:
        return True
    return False  
    pass

def HeroTakeDamage(damageToDeal):
    pass

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
    
# // ! modifer liste et pas bdd