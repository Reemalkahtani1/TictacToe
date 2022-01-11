import math
class tictactoe():
    board = [' ',' ',' ',
             ' ',' ',' ',
             ' ',' ',' ']  

    def isWin(self,player):
        if (self.board[0] == self.board[1] == self.board[2] == player
            or self.board[3] == self.board[4] == self.board[5] == player 
            or self.board[6] == self.board[7] == self.board[8] == player 
            or self.board[0] == self.board[4] == self.board[8] == player 
            or self.board[2] == self.board[4] == self.board[6] == player 
            or self.board[0] == self.board[3] == self.board[6] == player 
            or self.board[1] == self.board[4] == self.board[7] == player 
            or self.board[2] == self.board[5] == self.board[8] == player):
            return player
    
    def play(self,player):
        move = int(input("your move: "))
        if self.board[move] == ' ':
            self.board[move] = player

    def start(self):
        player = 'x'
        while True:
            player = 'x'
            move = self.bestMove()
            self.board[move] = 'x'
            self.showBoard()
            print()
            if self.isWin('x'):
                print("AI won")
                break

            if self.isTie():
                print("tie!")
                break

            player = 'o'
            self.play(player)
            self.showBoard()
            print()
            if self.isWin('o'):
                print("you won")
                break

            if self.isTie():
                print("tie!")
                break

    def showBoard(self):
        print(self.board[0],"|",self.board[1],"|",self.board[2])
        print("---------")
        print(self.board[3],"|",self.board[4],"|",self.board[5])
        print("---------")
        print(self.board[6],"|",self.board[7],"|",self.board[8])
    
    def score(self,player):
        if player == 'x':
            return 1
        if player == 'o':
            return -1
        if self.isTie():
            return 0

    def isTie(self):
        for i in range(9):
            if self.board[i] == ' ':
                return False
        return True

    def bestMove(self):
        bestScore = -math.inf
        move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'x'
                score = self.minmax( self.board , 0 ,False)
                self.board[i] = ' '
                if bestScore < score:
                    bestScore = score
                    move = i
        return move

    def minmax(self , board , depth , isMax):
        winner = None
        if isMax : 
            winner = self.isWin('x')
        else:
            winner = self.isWin('o')
        if winner != None:
            result = self.score(winner)
            return result

        if isMax: 
            bestScore = -math.inf

            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'x'
                    score = self.minmax(board, depth+1 ,False)
                    self.board[i] = ' '
                    if score > bestScore:
                        bestScore = score
            
            return bestScore

        else:
            bestScore = math.inf

            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'o'
                    score = self.minmax(board, depth+1 ,True)
                    self.board[i] = ' '
                    if score < bestScore:
                        bestScore = score
            
            return bestScore



# starting the game            
tic = tictactoe()
print(tic.isWin('x'))
tic.start()

