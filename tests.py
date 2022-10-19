import unittest
from game import Game

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_crear_tablero(self):
         self.game.crear_tablero()
         self.assertEqual(self.game.board,[
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]])

    def test_crear_turno(self):
        self.game.crear_turno()
        self.assertEqual(self.game.turno1,'X')
        self.assertEqual(self.game.turno2,'O')

    def test_colocar_pieza(self):
        self.game.crear_tablero()
        self.game.colocar_pieza(7,5)
        self.assertEqual(self.game.board[7][5],0)
        


    def test_casilla_disponible(self):
        self.game.crear_tablero()
        self.game.casilla_disponible(7,5)
        self.assertEqual(self.game.board[7][5], 0)

    def test_casilla_ocupada(self):
        self.game.crear_tablero()
        self.game.casilla_ocupada(7,5)
        self.assertEqual(self.game.board[7][5],False)

    def test_siguiente_casilla(self):
        self.game.crear_tablero()
        self.game.siguiente_casilla(5)
        self.assertEqual(self.game.board[6][5],0)

    def test_condicion_ganado1(self):
        self.game.crear_tablero()
        self.game.condicion_partida(4,5,'O')
        self.assertEqual(self.game.board,[
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]])    

   
        
        
          
        
         
        
        

     

        


if __name__ == "__main__":
    unittest.main()
    