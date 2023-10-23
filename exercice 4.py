minute = int(input())
heure = minute // 60
minute = minute - (heure*60)
jour = heure // 24
heure = heure - ( jour *24)
print("il s'est passé", jour,"jours et", heure,"heures depuis le debut du mois")
