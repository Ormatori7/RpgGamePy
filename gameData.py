
from db_init import hero, akatsuki, classement, TeamPlayer, PseudoDB



hero_list = list(hero.find({}, {"_id": 0}))
akatsuki_list = list(akatsuki.find({}, {"_id": 0}))
TeamPlayer_list = []