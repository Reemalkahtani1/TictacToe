# Tic Tac Toe
This is a Python implementation of the classic game Tic Tac Toe, also known as Noughts and Crosses.

## How to Play
The game is played on a 3x3 grid. Each player takes turns marking a space on the grid with their symbol, either X or O. The goal is to get three of your symbols in a row, either horizontally, vertically, or diagonally.

## Code Explanation
The tictactoe class represents the game. The game board is stored as a list of 9 strings, initially empty.

board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']
         
The showBoard method prints the current state of the board to the console.

The play method allows a player to make a move by entering the number of the space they want to mark.

The isWin method checks if a player has won the game. If so, it returns the winning player (either X or O).

The isTie method checks if the game has ended in a tie (all spaces on the board are filled and no player has won).

The bestMove method uses the minimax algorithm to find the best move for the AI player (X).

The minmax method recursively evaluates all possible moves and returns the score for the current player.

The start method starts the game and alternates between the AI player and the human player until the game is won or tied.

## How to Run
To play the game, simply create an instance of the tictactoe class and call the start method.
tic = tictactoe()
tic.start()

## Requirements
The code requires the math module to be imported.
