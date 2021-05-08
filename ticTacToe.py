global ticTacToeBoard
global gameOn
global turn

ticTacToeBoard = [" "," "," "," "," "," "," "," "," "]
#ticTacToeBoard = ["X","X","O","O","O","X","O","X","O"]
gameOn = True
turn = 0


def change_player():
    if currentPlayer == 'X':
        return 'O'
    else:
        return 'X'

def print_board():

  print(ticTacToeBoard[0] + "|" + ticTacToeBoard[1] + "|" + ticTacToeBoard[2])
  print("-+-+-")
  print(ticTacToeBoard[3] + "|" + ticTacToeBoard[4] + "|" + ticTacToeBoard[5])
  print("-+-+-")
  print(ticTacToeBoard[6] + "|" + ticTacToeBoard[7] + "|" + ticTacToeBoard[8])

def current_value():
    return currentPlayer

def check_if_there_is_a_winner():
    possibleWinningCombinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    xCount = 0
    OCount = 0
    for combination in possibleWinningCombinations:
      for i in combination:
        if ticTacToeBoard[i-1] == 'X':
            xCount += 1
            if xCount == 3:
                print('X wins')
                gameOn = false
        else:
            xCount = 0
        
        if ticTacToeBoard[i-1] == 'O':
            OCount += 1
            if OCount == 3:
                print('O wins')
                gameOn = false
        else:
            OCount = 0
        

def play_game():
  global currentPlayer
  currentPlayer = 'X'
  while gameOn:
    print('Playing as ' + currentPlayer)
    print('Choose (1-9)')
    num = int(input())
    if num >= 1 and num <= 10:
        ++turn
        ticTacToeBoard[num-1] = current_value()
        print_board()
        currentPlayer = change_player()
        check_if_there_is_a_winner()
  else:
    print('Game Over, its a tie')

play_game()

# check_if_there_is_a_winner()