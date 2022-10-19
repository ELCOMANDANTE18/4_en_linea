


class Game:
    
    def __init__(self):
        self.board = []
        self.j1 = 'X'
        self.j2 = 'O'
        self.turno1 = self.j1
        self.turno2 = self.j2
    
           
    def crear_tablero(self):
        self.board= [[0 for column in range(8)] for row in range(8)]     

    def crear_turno(self):
        if self.turno1 == self.j1:
            self.turno2 == self.j2
        else:
            self.turno1 == self.j2
        

    
    def colocar_pieza(self,row,col,):
        if self.board[row][col] == self.turno1:
            return self.j1
        else:
            self.board[row][col] == self.turno2
            return self.j2    

    
    def casilla_disponible(self,col,row):
        self.board[row][col] == 0
        return True
    
    def casilla_ocupada(self,row,col):
        if self.board[row][col] == self.j1:
            return False
        else:
            self.board[row][col] == self.j2
        
        return False
    
    def siguiente_casilla(self,col):
        for i in range(7, -1, -1):
            if self.board[i][col] == 0:
                return i

    
    def condicion_partida(self,col,row,coin):
        #Horizontal
        for i in range(col - 3):
            for j in range(row):
                if self.board[j][i] == coin and self.board[j][i+1] == coin and self.board[j][i+2] == coin and self.board[j][i+3] == coin:
                    return True

    def condicion_partida2(self,col,row,coin):
        #Vertical
        for i in range(col):
            for j in range(row - 3):
                if self.board[j][i] == coin and self.board[j+1][i] == coin and self.board[j+2][i] == coin and self.board[j+3][i] == coin:
                    return True
    
    def condicion_partida3(self,col,row,coin):                
        for i in range(col):
            for j in range(row - 3):
                if self.board[j][i] == coin and self.board[j+1][i+1] == coin and self.board[j+2][i+2] == coin and self.board[j+3][i+3] == coin:
                    return True
        
    def condicion_partida4(self,row,col,coin):    
        for i in range(col):
            for j in range(row - 3):
                if self.board[j][i] == coin and self.board[j-1][i-1] == coin and self.board[j-2][i-2] == coin and self.board[j-3][i-3] == coin:
                    return True


    def printTab(self):

        print("|", end="")
        for f in range(0, len(self.board[0])):
            print(f, end="|")
        print("")
        
      
        for fila in self.board:
            print('|', end='')
            for valor in fila:
                print(valor, end='')
                print('|', end='')
            print('') 
        
  
        print('+', end='')
        for x in range(1, len(self.board[0]) + 1):
            print('-', end='+')
        print('')   
    









        
        



        
        



   
    
    
    
        



     
   #Nivel de complejidad es proporcional a los for que tengamos     
 # Clase del 31 vemos los de los inputs y prints

#para aprobar esta materia: aprobar el parcial nos dan el test y nosotros lo resolvemos y el trabajo (entregar cuando este listo)  
