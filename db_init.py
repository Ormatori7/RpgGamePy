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
TeamPlayer = db.equipeJoueur

# // ! --------------------------------------------------

# fonction pour initialiser notre DB / ajouter héro et membre akatsuki via la fonction 
# // : DB_init()
    # // - DeleteList()    
    # // - CreateList()    
    # // - InsertCharacter()
    # on print afin de savoir si ca a fonctionné 
    
# // : DeleteList() 
    # on supprime d'abord les liste des héro/akatsuki s'ils s'y sont déja
    
# // : CreateList()
    # on prépare nos données pour les héros dans une liste de dictionnaire 
    # on prépare nos données pour les personnages de l'akatsuki dans une liste de dictionnaire 
    
# // : InsertCharacter()
    # on ajouter la liste de héro dans la table héro (avec insert many)
    # on ajouter la liste de perso de l'akatsuki dans la table akatsuki (avec insert many)
    
