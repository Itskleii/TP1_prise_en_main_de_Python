jour = int(input('jour : '))
heure = int(input('heure : '))
minutes = int(input('minutes : '))

minutes_ecoulée = (jour-1) * 24 * 60 + heure * 60 + minutes
print('le temps écoulée est : ', minutes_ecoulée)