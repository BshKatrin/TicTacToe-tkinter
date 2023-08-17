
import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.width = 300
        self.height = 300
        self.array = [['_' for _ in range(3)] for _ in range(3)] #empty array [ [ _ , _ , _], [ _ , _ , _], [ _ , _ , _] ]
        self.letter = 'X'
        self.gameWon = False
        self.gameDraw = True

    def mouseClick(self, event):
        print(f"x : {event.x}, y : {event.y}")

        col = event.x//100
        row = event.y//100
        if (self.array[row][col] == '_'):
            self.array[row][col] = self.letter
            self.gameWon = self.checkWinner()
            self.gameDraw = self.checkDraw()
            if self.letter == 'X' : self.letter = 'O'
            else : self.letter = 'X'
        #return event.x//100, event.y//100    
    
    def createBoard(self):
        self.window = tk.Tk()
        self.window.geometry(str(self.width)+'x'+str(self.height))
        self.window.grid()
        self.window.title("Tic-Tac-Toe")

        #Create empty board
        self.canvas = tk.Canvas(self.window, width = self.width, height = self.height)
        self.canvas.create_line(self.width/3, 0, self.width/3, self.height)
        self.canvas.create_line(self.width/3*2, 0, self.width/3*2, self.height)
        self.canvas.create_line(0, self.height/3, self.width, self.height/3)
        self.canvas.create_line(0, self.height/3*2, self.width, self.height/3*2)

        self.window.bind('<Button-1>', self.mouseClick)

        self.canvas.pack()
        #Create grid 3*3
        #self.window.columnconfigure(3, 1)
        #self.window.rowconfigure(3, 1)

    def drawFullBoard(self):
        for i in range(3):
            for j in range(3):
                if self.array[i][j] == 'O':
                    self.canvas.create_oval(100*j+20, 100*i+20, 100*(j+1)-20, 100*(i+1)-20)
                elif self.array[i][j] == 'X':
                    self.canvas.create_line(100*j+20, 100*i+20, 100*(j+1)-20, 100*(i+1)-20)
                    self.canvas.create_line(100*(j+1)-20, 100*i+20, 100*j+20, 100*(i+1)-20)

    def printArray(self):
        for i in range(3):
            for j in range(3):
                print(self.array[i][j], end = ' ')
            print("\n")
           

    #return True if letter is the winner, False if not
    def checkWinner(self):
        winnerFound = True
        
        #1st diagonal
        for i in range(3):
            if self.array[i][i] != self.letter:
                winnerFound = False
                break
        if winnerFound : return True

        winnerFound = True
        #lines
        for i in range(3):
            for j in range(3):
                if self.array[i][j] != self.letter:
                    winnerFound = False
                    break
            if winnerFound : return True

        winnerFound = True
        #columns
        for j in range(3):
            for i in range(3):
                if self.array[i][j] != self.letter:
                    winnerFound = False
                    break
            if winnerFound : return True


        winnerFound = True
        #2nd diagonal:
        for i in range(3):
            if self.array[i][2-i] != self.letter:
                winnerFound = False
                break
        
        return winnerFound
    
    #return True if Draw, False if not
    def checkDraw(self):
        for i in range(3):
            for j in range(3):
                if self.array[i][j] == '_':
                    return False
        return True
    
    def GameOver(self):

        self.window.unbind("<Button-1>")
        #self.canvas.delete('all')
        self.canvas.destroy()
        """
        text = tk.Text(self.window, text = "It's a draw!")
        text.place(x = 50, y = 50)
        text.pack()
        text.config(state = 'disabled')
        """
        text = tk.Label(self.window, anchor = 'center', fg = 'white', text = "Game is over!", width = len("Game is over!"))
        text.pack()
        text.place(x = self.width//3, y = self.height//3)

        startAgainButton = tk.Button(self.window, text = 'Start Again')
        startAgainButton.pack()
        startAgainButton.place(x = self.width//3, y = self.height//3+30)

game = TicTacToe()
game.createBoard()

while (not game.gameWon) and (not game.gameDraw):
    game.drawFullBoard()
    #game.printArray()
    print(f"gameWon : {game.gameWon}, gameDraw : {game.gameDraw}")
    game.window.update()
    game.window.update_idletasks()

if game.gameDraw or game.gameWon: 
    game.GameOver()

game.window.mainloop()