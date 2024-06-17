import dice
from time import sleep


def roll(amount:int, sides:int):
    return dice.roll(f'{amount}d{sides}')

<<<<<<< HEAD
for idx, result in enumerate(roll(5,20)):
=======
for idx, result in enumerate(roll(6,6)):
>>>>>>> main
    print(f'Lanzamiento {idx+1} número obtenido {result}')
    sleep(5)


