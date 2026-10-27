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
PseudoDB = db.pseudo # commence vide pour stocker le pseudo

# // ! --------------------------------------------------

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
    
