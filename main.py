from game import Game
from game import *


    
def play():
    juego = Game()
    juego.crear_tablero()
    try:
        while True:
            juego.printTab()
            juego.crear_turno()
            op = int(input('Donde desea poner su ficha?? 1 - 7: '))
            juego.colocar_ficha(op)
            if juego.ganador != None:
                juego.printTab()
                juego.Has_ganado()
                return again()
    except Exception as e:
            print(f'Error!: {e}')   

def again():
    eleccion = input("Revancha? [s/n] ")
    if eleccion == "s":
        play()
    elif eleccion == "n":
                return False

if __name__=='__main__':
    play()   