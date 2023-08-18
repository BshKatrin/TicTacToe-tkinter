
import tkinter as tk
from sys import exit

class TicTacToe:
    def __init__(self):
        self.width = 300
        self.height = 300
        self.array = [['_' for _ in range(3)] for _ in range(3)] #empty array [ [ _ , _ , _], [ _ , _ , _], [ _ , _ , _] ]
        self.letter = 'X'
        self.gameWon = False
        self.gameDraw = False
        self.gameExit = False

        self.window = tk.Tk()
        self.window.geometry(str(self.width)+'x'+str(self.height))
        self.window.grid()
        self.window.title("Tic-Tac-Toe")

        self.canvas = tk.Canvas(self.window, width = self.width, height = self.height)
        

    def drawFullBoard(self):
        for i in range(3):
            for j in range(3):
                if self.array[i][j] == 'O':
                    self.canvas.create_oval(100*j+20, 100*i+20, 100*(j+1)-20, 100*(i+1)-20)
                elif self.array[i][j] == 'X':
                    self.canvas.create_line(100*j+20, 100*i+20, 100*(j+1)-20, 100*(i+1)-20)
                    self.canvas.create_line(100*(j+1)-20, 100*i+20, 100*j+20, 100*(i+1)-20)

    def quit(self):
        self.window.destroy()
        self.gameExit = True
        exit(0)

    def createBoard(self):
            
            #Create empty board
            self.canvas.create_line(self.width/3, 0, self.width/3, self.height)
            self.canvas.create_line(self.width/3*2, 0, self.width/3*2, self.height)
            self.canvas.create_line(0, self.height/3, self.width, self.height/3)
            self.canvas.create_line(0, self.height/3*2, self.width, self.height/3*2)

            

            self.canvas.pack()
            #Create grid 3*3
            #self.window.columnconfigure(3, 1)
            #self.window.rowconfigure(3, 1)

    def createMenu(self):
        
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)

        self.textFrame = tk.Frame(self.window, width=self.width//3, height=self.height//3)
        self.textFrame.grid(row = 0, column=1)

        text = tk.Label(self.textFrame, text = "MENU")
        text.pack()

        self.buttonFrame = tk.Frame(self.window, width=self.width//3, height=self.height//3)
        self.buttonFrame.grid(row=1, column=1)  
        
        startButton = tk.Button(self.buttonFrame, text = "Play")
        startButton.pack(side=tk.TOP)
        startButton.bind('<Button-1>', self.startGame)

        exitButton = tk.Button(self.buttonFrame, text = "Exit", command = self.quit)
        exitButton.pack(side=tk.BOTTOM)
        

    def startGame(self, event):
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
        return "break" # check this one. Read docs on .bind and .unbind
    
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

        #columns
        for i in range(3):
            winnerFound = True
            for j in range(3):
                if self.array[i][j] != self.letter:
                    winnerFound = False
                    break
            if winnerFound : return True

        winnerFound = True
        #lines
        for j in range(3):
            winnerFound = True
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
        self.canvas.destroy()
        
        text = tk.Label(self.window, anchor = 'center', fg = 'white', text = "Game is over!", width = len("Game is over!"))
        text.pack()
        text.place(x = self.width//3, y = self.height//3)

        startAgainButton = tk.Button(self.window, text = 'Start Again')
        startAgainButton.pack()
        startAgainButton.place(x = self.width//3, y = self.height//3+30)



game = TicTacToe()
game.createMenu()


game.window.mainloop()
"""
while (not game.gameWon) and (not game.gameDraw):
    game.drawFullBoard()
    #game.printArray()
    print(f"gameWon : {game.gameWon}, gameDraw : {game.gameDraw}")
    game.window.update()
    game.window.update_idletasks()

if game.gameDraw or game.gameWon: 
    game.GameOver()
if game.gameExit : exit()
#game.window.mainloop()
#game.self.quit()
"""