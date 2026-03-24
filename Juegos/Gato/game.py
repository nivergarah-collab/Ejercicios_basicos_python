import Utils as U
master = 0
empate = 0
## starting board
a,b,c,d,e,f,g,h,i = 1,2,3,4,5,6,7,8,9
e = "O"
board = [[a,b,c],[d,e,f],[g,h,i]]

## INICIO ##
while master == 0 and empate != 4: 
 U.display_board(board)
 move = int(input("What its your move?\n"))
 board = U.enter_move(board, move)
 # U.display_board(board)
 status, sign = U.victory_for(board, 'x')
 if status == 1:
  print("Felicidades!!!! Has GANADO!")
  master += 1
 else: 
  U.draw_move(board)
  status, sign = U.victory_for(board, 'x')
  if status == 1:
   U.display_board(board)
   print("LOSE :(   Mas suerte para la proxima!")
   master += 1 
  else:
   empate += 1
   if empate == 4: 
    U.display_board(board)
    print("Empate")
    master += 1
   
