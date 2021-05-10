global ticTacToeBoard
ticTacToeBoard = [" "," "," "," "," "," "," "," "," "]
global maxNumberOfRounds
maxNumberOfRounds = 9

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

    global gameOn
    possibleWinningCombinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    global xCount
    global OCount
    xCount = 0
    OCount = 0
    for combination in possibleWinningCombinations:
      xCount = 0
      OCount = 0
      for i in combination:
        if ticTacToeBoard[i-1] == 'X':
            xCount += 1
            if xCount == 3:
                print_board()
                print('X wins')
                gameOn = False
        else:
            xCount = 0
        
        if ticTacToeBoard[i-1] == 'O':
            OCount += 1
            if OCount == 3:
                print_board()
                print('O wins')
                gameOn = False
        else:
            OCount = 0

def play_game():
    print('1 Player or 2 Players ? Please enter 1 or 2.')
    answer = int(input())
    print('What do you want to choose? X or O')
    playerType = str(input())
    if answer == 1:
        play_game()
    elif answer == 2:
        start_game(playerType)
    else: 
        play_game()

def start_game(playerType):
    global gameOn
    global turn
    global keepTheSamePlayer
    global currentPlayer

    currentPlayer = playerType
    gameOn = True
    turn = 0
    keepTheSamePlayer = False

    while gameOn:
        print('Playing as ' + currentPlayer)
        print('Choose (1-9)')
        num = input()
        try:
            num = int(num)
        except ValueError as e:
            print("Please choose a number between (1-9)! Try it again")
            start_game(currentPlayer)
            
        if num >= 1 and num <= 10:
            if ticTacToeBoard[num-1] == " ":
                turn += 1
                ticTacToeBoard[num-1] = current_value()
                print_board()
                currentPlayer = change_player()
                check_if_there_is_a_winner()
            else:
                print(str(num) + " has already been occupied, Please enter another position.")
                start_game(currentPlayer)

            if turn == maxNumberOfRounds and gameOn is True:
                print('Its a tie, Game Over')
                gameOn = False
            if gameOn is False:
                print('Game Over')
                break
        else:
            continue


play_game()