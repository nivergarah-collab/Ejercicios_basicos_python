import random

# Consiga Cisco


## Tablero
def display_board(board):
 print("+-------+-------+-------+")
 print("|       |       |       |")
 print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
 print("|       |       |       |")
 print("+-------+-------+-------+")
 print("|       |       |       |")
 print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
 print("|       |       |       |")
 print("+-------+-------+-------+")
 print("|       |       |       |")
 print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
 print("|       |       |       |")
 print("+-------+-------+-------+")

def make_list_of_free_fields(board):
 listalibre = []
 for i in board: 
  for s in i:
   if s == "x" or s == "O":
     continue
   else:
     a = board.index(i) 
     b = i.index(s)
     listalibre.append((a,b))
 return listalibre

## Movimiento
def enter_move(board, move):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
 move = move
 listalibre = make_list_of_free_fields(board)
 move, space_move, a,b = number_to_space(move)
 while space_move not in listalibre:
  move = int(input("Ingrese un movimiento valido\n"))
  move, space_move, a, b = number_to_space(move)
 board[a][b] = "x"
 return board

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
 maching_move = random.randrange(1,10)
 listalibre = make_list_of_free_fields(board)
 maching_move, space_move,a,b = maching_number_to_space(maching_move)
 while space_move not in listalibre:
  maching_move = random.randrange(1,10)
  maching_move, space_move,a,b = maching_number_to_space(maching_move)
 board[a][b] = "O"
 sing = "O"
 return board, sing

## Condicion

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    # existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu  ganas, o la maquina gana;
 result = lista_de_verificacion(board)
 sing = "X"
 if result == "Win":
  return 1, sign
 elif result == "continue":
  return 0, sing
 else: 
  print ("Error en bloque victory_for")





# Auxiliares mias

def number_to_space(number): 
 while number not in range(1,10):
   number = int(input("Ingrese un movimiento valido\n"))
 number = number
 if number == 1:
   move = (0,0)
   row = 0
   column = 0
 elif number == 2:
   move = (0,1)
   row = 0
   column = 1
 elif number == 3:
   move = (0,2)
   row = 0
   column = 2
 elif number == 4:
   move = (1,0)
   row = 1
   column = 0
 elif number == 5:
   move = (1,1)
   row = 1
   column = 1
 elif number == 6:
   move = (1,2)
   row = 1
   column = 2
 elif number == 7:
   move = (2,0)
   row = 2
   column = 0
 elif number == 8:
   move = (2,1)
   row = 2
   column = 1
 elif number == 9:
   move = (2,2)
   row = 2
   column = 2
 return number, move, row, column          

def maching_number_to_space(number): 
 if number == 1:
   move = (0,0)
   row = 0
   column = 0
 elif number == 2:
   move = (0,1)
   row = 0
   column = 1
 elif number == 3:
   move = (0,2)
   row = 0
   column = 2
 elif number == 4:
   move = (1,0)
   row = 1
   column = 0
 elif number == 5:
   move = (1,1)
   row = 1
   column = 1
 elif number == 6:
   move = (1,2)
   row = 1
   column = 2
 elif number == 7:
   move = (2,0)
   row = 2
   column = 0
 elif number == 8:
   move = (2,1)
   row = 2
   column = 1
 elif number == 9:
   move = (2,2)
   row = 2
   column = 2
 return number, move, row, column   

def lista_de_verificacion(board):
  op1 = board[0][0] == board[0][1] and board [0][2]  == board[0][1]
  op2 = board[1][0] == board[1][1] and board [1][2]  == board[1][1]
  op3 = board[2][0] == board[2][1] and board [2][2]  == board[2][1]
  op4 = board[0][0] == board[1][0] and board [2][0]  == board[1][0]
  op5 = board[0][1] == board[1][1] and board [2][1]  == board[1][1]
  op6 = board[0][2] == board[1][2] and board [2][2]  == board[1][2]
  op7 = board[0][0] == board[1][1] and board [2][2]  == board[1][1]
  op8 = board[0][2] == board[1][1] and board [2][0]  == board[1][1]
  verificacion = [op1, op2, op3, op4, op5, op6, op7, op8]
  if True in verificacion:
   return "Win"
  else: 
   return "continue"















