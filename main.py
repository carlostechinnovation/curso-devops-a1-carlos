import dice
from time import sleep
import os

MIVARIABLE = os.getenv('MIVARIABLE')  # para fase Test de Jenkins
if(not MIVARIABLE):
    print("Debes indicar un numero para MIVARIABLE (útil en Test de Jenkins)")
    exit(-1)

def roll(amount:int, sides:int):
    return dice.roll(f'{amount}d{sides}')

for idx, result in enumerate(roll(6,6)):
    print(f'Lanzamiento {idx+1} número obtenido {result}')
    sleep(5)


