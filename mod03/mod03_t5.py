
import math

leivi = float(input('Anna leiviskät:'))
naula = float(input('Anna naulat:'))
luoti = float(input('Anna luodit:'))

naula = leivi * 20 + naula
luoti = naula * 32 + luoti

#print('Koko massa luoteina:', luoti)

gramma = luoti * 13,3

print(f'Massa nykymittojen mukaan: {gramma // 1000} kiloa ja {gramma % 1000} grammaa')