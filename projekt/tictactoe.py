from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random





class Game:

    '''
    Konstruktor domyslny
    Args:
        root - glowna warstwa aplikacji okienkowe w tkinter

    '''
    def __init__(self,root):
        self.root = root
        self.root.config(bg = "white",width = '1000',height = '1000')
        self.krzyzyk = PhotoImage(file="x.png")
        self.kolko = PhotoImage(file="o.png")
        self.back = PhotoImage(file="back3.png")
        self.img = PhotoImage(width=266, height=266,file = "empty.png")
        self.whoIsNext = ""
        self.board = [["." for i in range(3)] for j in range(3)]
        self.player = ""
        self.computer = ""
        self.isOver = False
        self.scores = {'X':1,'O':-1,'tie':0}
        self.players = ["O","X"]
        self._newGame()
    
    '''
    Funkcja realizujaca wyswietlenie ekranu poczatkowego dla nowej gry
    '''
    def _newGame(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = "."
        self.root.title("TicTacToe")
        self.isOver = False
        self.root.resizable(width=False, height=False)
        self.root.geometry("800x800")
        
        # tworzymy tlo dla aplikacji
        canvas = Canvas(self.root,width = 800, height = 800)
        canvas.pack(fill= "both",expand = True)
        canvas.create_image(0,0,image = self.back,anchor="nw")
        
        oButton = Button(self.root, image=self.kolko,
                         command=lambda : self._initBoard("O"))
        xButton = Button(self.root, image=self.krzyzyk,
                         command= lambda : self._initBoard("X"))
        
        xbutton_window=canvas.create_window(200,500,anchor = "center",window = oButton)
        obutton_window=canvas.create_window(600,500,anchor = "center",window = xButton)

    '''
    Funkcja ktora realizuje akcje klikniecia w przyciski "xButton" i "oButton"
    
    Args:
        figure(string) - przekazujemy znak "O" lub "X" w zaleznosci od wybranej figury przez gracza.
    '''
    def _initBoard(self, figure):
        if figure == "X":
            self._clearRoot()
            self.scores = {'X':-1, 'O': 1, 'tie': 0}
            self.whoIsNext = random.choice(self.players)
            self.player = "X"
            self.computer = "O"
            self._generateBoard()
            if self.computer == self.whoIsNext:
                cell = random.choice(self.cells)
                self._putAI(cell)
        elif figure == "O":
            self._clearRoot()
            self.scores = {'X': 1, 'O': -1, 'tie': 0}
            self.player = "O"
            self.computer = "X"
            self.whoIsNext = random.choice(self.players)
            self._generateBoard()
            if self.computer == self.whoIsNext:
                cell = random.choice(self.cells)
                self._putAI(cell)




    '''
    Funkcja generujaca plansze 3x3. Zostaje utworzone 9 przyciskow, ktore sa odpowiednio obslugiwane.
    '''
    def _generateBoard(self):
        #czyscimy plansze robocza do sprawdzania
        for i in range(3):
            for j in range(3):
                self.board[i][j] == "."

        self.b1 = Button(self.root,text = "b1",image = self.img,command=lambda: self._click(self.b1) )
        self.b2 = Button(self.root,text = "b2", image = self.img,command=lambda: self._click(self.b2))
        self.b3 = Button(self.root,text = "b3",image = self.img,command=lambda:self._click(self.b3))
        self.b4 = Button(self.root,text = "b4",image = self.img,command=lambda:self._click(self.b4))
        self.b5 = Button(self.root,text = "b5",image = self.img,command=lambda:self._click(self.b5))
        self.b6 = Button(self.root,text = "b6", image = self.img,command=lambda:self._click(self.b6))
        self.b7 = Button(self.root,text = "b7", image = self.img,command=lambda:self._click(self.b7))
        self.b8 = Button(self.root,text = "b8", image = self.img,command=lambda:self._click(self.b8))
        self.b9 = Button(self.root,text = "b9", image = self.img,command=lambda:self._click(self.b9))
        self.cells = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]
        self.dict = {self.b1:"b1", self.b2: "b2", self.b3: "b3", self.b4: "b4", self.b5: "b5", self.b6: "b6", self.b7: "b7", self.b8: "b8", self.b9: "b9"}
        

        #ustawienie przyciskow w odpowiednich miejscach
        self.b1.grid(row=0,column=0)
        self.b2.grid(row=0,column=1)
        self.b3.grid(row=0,column=2)
        self.b4.grid(row=1,column=0)
        self.b5.grid(row=1,column=1)
        self.b6.grid(row=1,column=2)
        self.b7.grid(row=2,column=0)
        self.b8.grid(row=2,column=1)
        self.b9.grid(row=2,column=2)







    '''
    Funkcja czyszczaca interfejs z wszystkich widgetow
    '''
    def _clearRoot(self):
        for widget in self.root.winfo_children():
            widget.destroy()


    '''
    Funkcja umieszczajaca na planszy figure komputera

    Args:
        button - przycisk wyliczony przez algorytm minimax dla komputera
        na ktorego nalezy nalozyc odpowiednia figure.
    '''
    def _putAI(self,button):
        if (self.computer == "O"):
            button.config(image=self.kolko,width=266, height=266)
            button['command']=0
            self._updateBoard(button, self.computer)
            self._checkIfEnd(self.computer)
            self.whoIsNext = self.player

        if (self.computer == "X"):
            button.config(image=self.krzyzyk,width=266, height=266)
            button['command']=0
            self._updateBoard(button, self.computer)
            self._checkIfEnd(self.computer)
            self.whoIsNext = self.player



    '''
    Funkcja realizujaca obliczenie optymalnego ruchu dla komputera.
    Z poziomu tej funkcji wywowylany jest algorytm minimax oraz _putAI()

    '''
    def _best_move(self):
        bestScore = -99999
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ".":
                    self.board[i][j] = self.computer
                    score = self._minimax(0,False)
                    self.board[i][j] = "."
                    if score > bestScore:
                        bestScore = score
                        bestMove = [i,j]

        self.board[bestMove[0]][bestMove[1]] = self.computer
        if bestMove[0] == 0:
            if bestMove[1] == 0:
                self._putAI(self.b1)
            elif bestMove[1] == 1:
                self._putAI(self.b2)
            elif bestMove[1] == 2:
                self._putAI(self.b3)
        elif bestMove[0] == 1:
            if bestMove[1] == 0:
                self._putAI(self.b4)
            elif bestMove[1] == 1:
                self._putAI(self.b5)
            elif bestMove[1] == 2:
               self._putAI(self.b6)
        elif bestMove[0] == 2:
            if bestMove[1] == 0:
                self._putAI(self.b7)
            elif bestMove[1] == 1:
                self._putAI(self.b8)
            elif bestMove[1] == 2:
                self._putAI(self.b9)




    '''
    Funkcja realizujaca algorytm minimax

    Args:
        depth(int) - glebokosc drzewa gry
        isMaximazing(boolean) - True lub False w zaleznosci dla ktorego gracza wywolywana jest funkcja minimax
    '''
    def _minimax(self,depth,isMaximizing):
        result = self._checkWinner()
        if result != None:
            score = self.scores[result]
            return score

        if isMaximizing:
            bestScore = -9
            #sprawdzamy wolne miejsca
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ".":
                        self.board[i][j] = self.computer
                        score = self._minimax(depth+1,False)
                        self.board[i][j] = "."
                        bestScore = max(score,bestScore)
            return bestScore

        else:
            bestScore = 9
            # sprawdzamy wolne miejsca
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ".":
                        self.board[i][j] = self.player
                        score = self._minimax(depth + 1, True)
                        self.board[i][j] = "."
                        bestScore = min(score,bestScore)
            return bestScore


   
    '''
    obsluga postawienia kolka lub krzyzyka na planszy
    Args: 
      button: przekazujemy przycisk w ktorym nalezy umiescic odpowiednio grafike kolka lub krzyzyka
   
    '''
    def _click(self,button):
         if( self.player == "O"):
            button.config(image=self.kolko,width=266,height=266)
            button['command'] = 0
            self._updateBoard(button, self.player)
            self.whoIsNext = self.computer
            if( self._checkIfEnd(self.player)== True ):
                return

         elif( self.player == "X"):
            button.config(image=self.krzyzyk, width=266, height=266)
            button['command'] = 0
            self._updateBoard(button, self.player)
            self.whoIsNext = self.computer
            if( self._checkIfEnd(self.player) == True ):
                return


         if self.isOver == False:
             self._best_move()

    '''
    Funkcja sprawdzajaca warunki konca gry i wyswietlenie odpowiedniego komunikatu jezeli koniec gry nastapil

    Args:
        figure(string) - figura dla ktorej sprawdzany jest stan rozgrywki.
    '''
    def _checkIfEnd(self,figure):
        if( self.board[0][0] == figure and self.board[1][1] == figure and self.board[2][2] == figure or
            self.board[0][0] == figure and self.board[1][0] == figure and self.board[2][0] == figure or
            self.board[0][0] == figure and self.board[0][1] == figure and self.board[0][2] == figure or
            self.board[0][1] == figure and self.board[1][1] == figure and self.board[2][1] == figure or
            self.board[0][2] == figure and self.board[1][2] == figure and self.board[2][2] == figure or
            self.board[0][2] == figure and self.board[1][1] == figure and self.board[2][0] == figure or
            self.board[1][0] == figure and self.board[1][1] == figure and self.board[1][2] == figure or
            self.board[2][0] == figure and self.board[2][1] == figure and self.board[2][2] == figure):
            if self.computer == figure:
                info = "AI won!" 
                self.isOver = True
                messagebox.showinfo("Game over", info)
            if self.player == figure:
                info = "you won!"
                self.isOver = True
                messagebox.showinfo("Game over", info)
            
        elif( self.isOver == False ):
            for i in range(3):
                for j in range(3):
                    if( self.board[i][j] == "."):
                        return
            info = "tie "
            self.isOver = True
            messagebox.showinfo("Game over", info)

        if( self.isOver == True ):
            self._clearRoot()
            self._newGame()
            return True


    
    '''
    funkcja ktora aktualizuje stan pomocniczej planszy w formie listy dwuwymiarowej
    Args:
        button: przekazujemy wcisniety przycisk
        figure: przekazujemy kolko lub krzyzyk w celu wpisania do pomocniczej listy stringow
    '''
    def _updateBoard(self,button,figure):
        if( button == self.b1):
            self.board[0][0] = figure
        elif (button == self.b2):
            self.board[0][1] = figure
        elif (button == self.b3):
            self.board[0][2] = figure
        elif (button == self.b4):
            self.board[1][0] = figure
        elif (button ==self.b5):
            self.board[1][1] = figure
        elif (button == self.b6):
            self.board[1][2] = figure
        elif (button == self.b7):
            self.board[2][0] = figure
        elif (button == self.b8):
            self.board[2][1] = figure
        elif (button == self.b9):
            self.board[2][2] = figure


   
    '''
    Funkcja sprawdzajaca sam stan rozgrywki
    '''
    def _checkWinner(self):
        winner = None
            #horyzontalnie
        for i in range(3):
            if (self.board[i][0]== self.board[i][1]) and (self.board[i][0] == self.board[i][2] )and self.board[i][0] != ".":
                winner = self.board[i][0]
                # if winner == '.':
                    

            #vertykalnie
        for j in range(3):
             if (self.board[0][j] == self.board[1][j]) and (self.board[0][j] ==  self.board[2][j]) and self.board[0][j] != ".":
                winner = self.board[0][j]
                # if winner == '.':
                    
            #diagonalnie
        if (self.board[0][0] == self.board[1][1]) and (self.board[0][0] == self.board[2][2]) and self.board[0][0] != ".":
            winner = self.board[0][0]
            # if winner  == '.':
                

        if (self.board[2][0] == self.board[1][1]) and (self.board[2][0] == self.board[0][2]) and self.board[2][0] != ".":
            winner = self.board[2][0]
            # if winner  == '.':
                
        #sprawdzamy ile wolnych pol
        openSpots = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ".":
                    openSpots+=1

        if winner == None and openSpots == 0:
            return 'tie'
        else:
            return winner



'''
Glowna petla programu
'''
def main():
    root = tk.Tk()
    gui = Game(root)
    mainloop()

if __name__ == "__main__":
    main()














