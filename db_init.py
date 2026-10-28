import pymongo
from pymongo import MongoClient

# // ! --------------------Partie Settings BDD--------------
# // + connexion au serveur via le port 27017
client = MongoClient("localhost", 27017)

# // + accéder à la db nommé RpgGamePy
db = client["RpgGamePy"]

# // + création des variables pour accéder à nos collections créer au préalable 
hero = db.hero
akatsuki = db.akatsuki
classement = db.classement
TeamPlayer = db.TeamPlayer
PseudoDB = db.PseudoDB # commence vide pour stocker le pseudo

# // ! --------------------------------------------------

def db_init():
    deleteLIst()
    createList()
    
    
    
def deleteLIst():
    hero.delete_many({}) # on supp tt sans condition
    akatsuki.delete_many({})
    TeamPlayer.delete_many({})
    PseudoDB.delete_many({})
    print("la db est vide")
    
def createList():
    ListeHero = [
        {"id_ref": "1", "nom": "naruto", "atk": 15, "def": 10, "hp": 100},
        {"id_ref": "2", "nom": "kakashi", "atk": 15, "def": 10, "hp": 75},
        {"id_ref": "3", "nom": "sasuke", "atk": 20, "def": 5, "hp": 90},
        {"id_ref": "4", "nom": "jiraya", "atk": 15, "def": 0, "hp": 120},
        {"id_ref": "5", "nom": "hinata", "atk": 15, "def": 10, "hp": 150},
        {"id_ref": "6", "nom": "minato", "atk": 50, "def": 15, "hp": 80},
        {"id_ref": "7", "nom": "shikamaru", "atk": 25, "def": 5, "hp": 200},
        {"id_ref": "8", "nom": "choji", "atk": 15, "def": 8, "hp": 200},
        {"id_ref": "9", "nom": "gaara", "atk": 90, "def": 5, "hp": 25},
        {"id_ref": "10", "nom": "rocklee", "atk": 15, "def": 5, "hp": 50},
    ]
     
    ListeAkatsuki = [
        {"nom": "deidara", "atk": 10, "def": 5, "hp": 100},
        {"nom": "Nagato", "atk": 15, "def": 15, "hp": 120},
        {"nom": "sasori", "atk": 20, "def": 10, "hp": 150},
        {"nom": "kisame", "atk": 10, "def": 10, "hp": 100},
        {"nom": "itachi", "atk": 25, "def": 7, "hp": 130},
        {"nom": "obito", "atk": 25, "def": 8, "hp": 150},
    ]
    
    InsertList(ListeHero, ListeAkatsuki)
    
     
     
def InsertList(ListeHero, ListeAkatsuki):
    hero.insert_many(ListeHero)
    akatsuki.insert_many(ListeAkatsuki)
    print("Bdd initialisée")
    print(f"  - {len(ListeHero)} personnages ajoutés")
    print(f"  - {len(ListeAkatsuki)} ennemis ajoutés")



if __name__ == "__main__":
    db_init()




# fonction pour initialiser notre DB / ajouter héro et membre akatsuki via la fonction 
# // : DB_init()
    # // - DeleteList()    
    # // - CreateList()    
    # // - InsertList()
    # on print afin de savoir si ca a fonctionné 
    
# // : DeleteList() 
    # on supprime la liste héro
    # on supp la liste akatsuki 
    # on supp la liste pseudo
    # on supp la liste TeamPlayer
    
# // : CreateList()
    # on prépare nos données pour les héros dans une liste 
    # on prépare nos données pour les personnages de l'akatsuki dans une liste
    # on prépare nos données pour les personnages de notre TeamPlayer dans une liste 
    # on prepare nos données pour le stockage de notre pseudo 
    
# // : InsertList()
    # on ajouter la liste de héro dans la table héro (avec insert many)
    # on ajouter la liste de perso de l'akatsuki dans la table akatsuki (avec insert many)
    # on ajoute notre pseudo dans la table pseudo
    # on ajoute notre team dans la table TeamPlayer
    
