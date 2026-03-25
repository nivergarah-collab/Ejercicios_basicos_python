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
 move = move
 listalibre = make_list_of_free_fields(board)
 move, space_move, a,b = number_to_space(move)
 while space_move not in listalibre:
  move = int(input("Ingrese un movimiento valido\n"))
  move, space_move, a, b = number_to_space(move)
 board[a][b] = "x"
 return board

def draw_move(board):
 maching_move = random.randrange(1,10)
 listalibre = make_list_of_free_fields(board)
 maching_move, space_move,a,b = number_to_space(maching_move)
 while space_move not in listalibre:
  maching_move = random.randrange(1,10)
  maching_move, space_move,a,b = number_to_space(maching_move)
 board[a][b] = "O"
 sing = "O"
 return board, sing


def number_to_space(number):
 while number not in range(1,10):
  number = int(input("Ingrese opcion valida\n"))
 number -= 1
 opciones = [(0,0), (0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)] 
 move = opciones[number]
 row = opciones[number][0]
 column = opciones[number][1]
 number += 1
 return number, move, row, column


## Condicion

def victory_for(board, sign):
 result = lista_de_verificacion(board)
 sign = sign
 if result == "Win" and sign == "X":
  display_board(board)
  print("Felicidades!!!! Has GANADO!")
  return 1
  
 elif result == "Win" and sign == "O":
  display_board(board)
  print("LOSE :(   Mas suerte para la proxima!")
  return 1
 else: 
  result == "continue"
  return 0

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