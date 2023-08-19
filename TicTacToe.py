import tkinter as tk
from sys import exit

class TicTacToe:
    def __init__(self):
        self.width = 300
        self.height = 300
        
        self.letter = 'X'
        self.gameWon = False
        self.gameDraw = False

        self.window = tk.Tk()
        self.window.geometry(str(self.width)+'x'+str(self.height))
        self.window.grid()
        self.window.title("Tic-Tac-Toe")

        #window configuration to use .grid later
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)

    #set an 2D array to keep track of the game
    def setEmptyArray(self):
        #empty array [ [ _ , _ , _], [ _ , _ , _], [ _ , _ , _] ]
        self.array = [['_' for _ in range(3)] for _ in range(3)]

    #print an array in console
    def printArray(self):
        for i in range(3):
            for j in range(3):
                print(self.array[i][j], end = ' ')
            print("\n")
    
    #Draw a menu on a window
    def createMenu(self):
        
        self.textFrame = tk.Frame(self.window, width=self.width//3, height=self.height//3)
        self.textFrame.grid(row = 0, column=0, columnspan=3)

        text = tk.Label(self.textFrame, text = "MENU", font=('Arial',40))
        text.pack(side='bottom')

        self.buttonFrame = tk.Frame(self.window, width=self.width//3, height=self.height//3)
        self.buttonFrame.grid(row=1, column=1)  
        
        startButton = tk.Button(self.buttonFrame, text = "Play")
        startButton.pack(side=tk.TOP)
        startButton.bind('<Button-1>', self.startGame)

        exitButton = tk.Button(self.buttonFrame, text = "Exit", command = self.quit)
        exitButton.pack(side=tk.BOTTOM)
        
    #Draw empty board 
    def createBoard(self):
            
            #Create empty board
            self.canvas.create_line(self.width/3, 0, self.width/3, self.height)
            self.canvas.create_line(self.width/3*2, 0, self.width/3*2, self.height)
            self.canvas.create_line(0, self.height/3, self.width, self.height/3)
            self.canvas.create_line(0, self.height/3*2, self.width, self.height/3*2)

            self.canvas.pack()

    #Draw empty board filled with X and O. Data from X and O positions is taken from array
    def drawFullBoard(self):
        for i in range(3):
            for j in range(3):
                if self.array[i][j] == 'O':
                    self.canvas.create_oval(100*j+20, 100*i+20, 100*(j+1)-20, 100*(i+1)-20)
                elif self.array[i][j] == 'X':
                    self.canvas.create_line(100*j+20, 100*i+20, 100*(j+1)-20, 100*(i+1)-20)
                    self.canvas.create_line(100*(j+1)-20, 100*i+20, 100*j+20, 100*(i+1)-20)

    #Keep track of a mouse click on a window. Place X and O in array. Change player's letter
    def mouseClick(self, event):
        col = event.x//100
        row = event.y//100
        if (self.array[row][col] == '_'):
            self.array[row][col] = self.letter
            self.gameWon = self.checkWinner()
            self.gameDraw = self.checkDraw()
            if self.letter == 'X' : self.letter = 'O'
            else : self.letter = 'X'
        # check this one. Read docs on .bind and .unbind
        # Used for full unbind 
        return "break" 
    
    #To use for exit buttons
    def quit(self):
        self.window.destroy()
        exit(0)

    # Start to play TicTacToe
    def startGame(self, event):
        self.setEmptyArray()

        self.canvas = tk.Canvas(self.window, width = self.width, height = self.height)

        self.gameDraw = False
        self.gameWon = False

        self.textFrame.destroy()
        self.buttonFrame.destroy()

        self.window.bind('<Button-1>', self.mouseClick)

        self.createBoard()
        while (not self.gameDraw) and (not self.gameWon):
            self.canvas.delete('all')
            self.drawFullBoard()
            self.createBoard()
            #self.drawFullBoard()
            self.window.update()
            self.window.update_idletasks()
            print(f"game is won : {self.gameWon}, draw : {self.gameDraw}")
            self.printArray()
        
        self.drawFullBoard()
    
        self.window.unbind('<Button-1>')

        self.gameOverScreen()

    # True if there is a Winner, False if not
    def checkWinner(self):
        winnerFound = True
        
        #check 1st diagonal
        for i in range(3):
            if self.array[i][i] != self.letter:
                winnerFound = False
                break
        if winnerFound : return True

        #check columns
        for i in range(3):
            winnerFound = True
            for j in range(3):
                if self.array[i][j] != self.letter:
                    winnerFound = False
                    break
            if winnerFound : return True

        winnerFound = True
        #check lines
        for j in range(3):
            winnerFound = True
            for i in range(3):
                if self.array[i][j] != self.letter:
                    winnerFound = False
                    break
            if winnerFound : return True


        winnerFound = True
        #check 2nd diagonal:
        for i in range(3):
            if self.array[i][2-i] != self.letter:
                winnerFound = False
                break
        
        return winnerFound
    
    # True if there is a draw, False if not
    def checkDraw(self):
        for i in range(3):
            for j in range(3):
                if self.array[i][j] == '_':
                    return False
        return True

    # Draw this if there is a winner or a draw
    def gameOverScreen(self):
        self.canvas.delete('all')
        self.canvas.destroy()
        #self.window.mainloop()

        self.textFrame = tk.Frame(self.window, width = self.width//3, height = self.height//3)
        self.textFrame.grid(row=0, column=1)
        message = "It is a draw!" if self.gameDraw else f"The winner is {'X' if self.letter == 'O' else 'O'}"
        text = tk.Label(self.textFrame, text=message)
        text.pack()
        
        self.buttonFrame = tk.Frame(self.window, width=self.width//3, height=self.height//3)
        self.buttonFrame.grid(row=1, column=1)
        startAgainButton = tk.Button(self.buttonFrame, text="Start again")
        startAgainButton.pack(side=tk.TOP)
        
        startAgainButton.bind('<Button-1>', self.startGame)
        exitButton = tk.Button(self.buttonFrame, text="Exit", command=self.quit)
        exitButton.pack(side=tk.BOTTOM)

# Start the game

game = TicTacToe()
game.createMenu()

game.window.mainloop()
