
#print("Hauska tavata {uusi_kayttaja}!!") # ilman f ei toimi
#print(f"Hauska tavata {uusi_kayttaja}!!")

#pisteet = 200
#pisteet = 400
#print(pisteet)

#merkkijono = "Alex"
#merkkijono = '9'
#merkkijono = ''
#pisteet = 0

#print(f'Merkkijono: {merkkijono:20s} sijoitetaan tähän väliin')

#import math

#print(f'{"Vakio":6s} {"Arvo":6s}')
#print('-----------')
#print(f'{"Pii":s6}: {math.pi:6.2f}')







#'''Laskutoimituksia ovat yhteenlasku (+), vähennyslasku (-), kertolasku (*) ja jakolasku (/).
#Lisäksi on olemassa jakojäännösoperaatio (%), pelkän kokonaisosan palauttava jakolasku (//)
#sekä potenssiinkorotus (**).'''


#Laskukone

#luetaan käyttäjältä kaksi lukua jotka täytyy muistaa muuttaa
#lukuluvuksi eli "float" ja sijoitetaan muuttajiin

import math

a = float(input('Anna luku:\n'))
b = float(input('Anna toinen luku\n'))

yhteenlasku = a + b
vahennyslasku = a - b
kertolasku = a * b
potenssiinkorotus = a ** b
jakolasku = a / b
kokonaisosa = a // b
jakojaannos = a % b

print(f'Yhteenlasku: {yhteenlasku}')
print(f'Vähennyslasku: {vahennyslasku}')
print(f'Kertolasku: {kertolasku}')
print(f'Potenssiinkorotus: {potenssiinkorotus}')
print(f'Jakolasku: {jakolasku}')
print(f'Jakojäännös: {jakojaannos}')