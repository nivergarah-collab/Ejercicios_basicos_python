import Utils as U

## starting board
a,b,c,d,e,f,g,h,i = 1,2,3,4,5,6,7,8,9
e = "O"
board = [[a,b,c],[d,e,f],[g,h,i]]


## INICIO ##

master = 0
while master == 0: 
 # userTurn
 U.display_board(board)
 move = int(input("What its your move?\n"))
 board = U.enter_move(board, move)
 status = U.victory_for(board, 'X')
 if status == 1:
  master += 1
 else: 
  #machingTurn
  U.draw_move(board)
  status = U.victory_for(board, 'O')
  if status == 1:
   master += 1 

   
