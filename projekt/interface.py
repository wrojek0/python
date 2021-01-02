from tkinter import *
from tkinter.font import Font
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import time
import math
import random
import tkinter




class Menu:

    def __init__(self,root):
        self.root = root
        self.root.config(bg = "white",width = '1000',height = '1000')
        self.krzyzyk = PhotoImage(file="krzyzyk.png")
        self.kolko = PhotoImage(file="kolko.png")
        self.img = PhotoImage(width=266, height=266)
        self.whoIsNext = ""
        self.board = [["." for i in range(3)] for j in range(3)]
        self.player = ""
        self.computer = ""
        self.isOver = False
        self.scores = {'X':1,'O':-1,'tie':0}
        self.players = ["O","X"]
        # self.font = Font(family = "Algerian",weight = "bold",size = 10)
        self.newGame()



    #jezeli wybierzemy krzyzyk generujemy z tej metody
    def initBoardFromX(self):
        self.clearRoot()
        self.scores = {'X':-1, 'O': 1, 'tie': 0}
        self.whoIsNext = random.choice(self.players)
        self.player = "X"
        self.computer = "O"
        self.generateBoard()
        if self.computer == self.whoIsNext:
            cell = random.choice(self.cells)
            self.putAI(cell, self.dict[cell])


    #jezeli wybierzemy kolko generujemy z tej metody
    def initBoardFromO(self):
        self.clearRoot()
        self.scores = {'X': 1, 'O': -1, 'tie': 0}
        self.player = "O"
        self.computer = "X"
        self.whoIsNext = random.choice(self.players)
        self.generateBoard()
        if self.computer == self.whoIsNext:
            cell = random.choice(self.cells)
            self.putAI(cell,self.dict[cell])





    #wygenerowanie przyciskow na planszy do gry
    def generateBoard(self):
        #czyscimy plansze robocza do sprawdzania
        for i in range(3):
            for j in range(3):
                self.board[i][j] == "."


        self.b1 = Button(self.root,text = "b1", bg="AntiqueWhite1", fg="AntiqueWhite1",image = self.img,command=lambda: self.click(self.b1,"b1") )
        self.b2 = Button(self.root,text = "b2", bg="AntiqueWhite1", fg="AntiqueWhite1",image = self.img,command=lambda: self.click(self.b2,"b2"))
        self.b3 = Button(self.root,text = "b3", bg="AntiqueWhite1", fg="AntiqueWhite1",image = self.img,command=lambda:self.click(self.b3,"b3"))
        self.b4 = Button(self.root,text = "b4", bg="AntiqueWhite1", fg="AntiqueWhite1",image = self.img,command=lambda:self.click(self.b4,"b4"))
        self.b5 = Button(self.root,text = "b5", bg="AntiqueWhite1", fg="AntiqueWhite1",image = self.img,command=lambda:self.click(self.b5,"b5"))
        self.b6 = Button(self.root,text = "b6", bg="AntiqueWhite1", fg="AntiqueWhite1",image = self.img,command=lambda:self.click(self.b6,"b6"))
        self.b7 = Button(self.root,text = "b7", bg="AntiqueWhite1", fg="AntiqueWhite1",image = self.img,command=lambda:self.click(self.b7,"b7"))
        self.b8 = Button(self.root,text = "b8", bg="AntiqueWhite1", fg="AntiqueWhite1",image = self.img,command=lambda:self.click(self.b8,"b8"))
        self.b9 = Button(self.root,text = "b9", bg="AntiqueWhite1", fg="AntiqueWhite1",image = self.img,command=lambda:self.click(self.b9,"b9"))
        self.turn = "TURN: "+ str(self.whoIsNext)
        
        self.cells = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]
        self.dict = {self.b1:"b1", self.b2: "b2", self.b3: "b3", self.b4: "b4", self.b5: "b5", self.b6: "b6", self.b7: "b7", self.b8: "b8", self.b9: "b9"}
        self.b1.grid(row=0,column=0)
        self.b2.grid(row=0,column=1)
        self.b3.grid(row=0,column=2)
        self.b4.grid(row=1,column=0)
        self.b5.grid(row=1,column=1)
        self.b6.grid(row=1,column=2)
        self.b7.grid(row=2,column=0)
        self.b8.grid(row=2,column=1)
        self.b9.grid(row=2,column=2)







    #wyczyszczenie interfejsu
    def clearRoot(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def putAI(self,button,whichOne):
        if (self.computer == "O"):
            button.config(image=self.kolko, state=DISABLED, width=266, height=266)
            self.updateBoard(whichOne, self.computer)
            self.checkIfEnd(self.computer)
            self.whoIsNext = self.player

        if (self.computer == "X"):
            button.config(image=self.krzyzyk, state=DISABLED, width=266, height=266)
            self.updateBoard(whichOne, self.computer)
            self.checkIfEnd(self.computer)
            self.whoIsNext = self.player




    def best_move(self):
        bestScore = -99999
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ".":
                    self.board[i][j] = self.computer
                    score = self.minimax(0,False)
                    self.board[i][j] = "."
                    if score > bestScore:
                        bestScore = score
                        bestMove = [i,j]

        

        self.board[bestMove[0]][bestMove[1]] = self.computer
        if bestMove[0] == 0:
            if bestMove[1] == 0:
                self.putAI(self.b1,"b1")
            elif bestMove[1] == 1:
                self.putAI(self.b2,"b2")
            elif bestMove[1] == 2:
                self.putAI(self.b3,"b3")

        elif bestMove[0] == 1:
            if bestMove[1] == 0:
                self.putAI(self.b4,"b4")
            elif bestMove[1] == 1:
                self.putAI(self.b5,"b5")
            elif bestMove[1] == 2:
               self.putAI(self.b6,"b6")

        elif bestMove[0] == 2:
            if bestMove[1] == 0:
                self.putAI(self.b7,"b7")
            elif bestMove[1] == 1:
                self.putAI(self.b8, "b8")
            elif bestMove[1] == 2:
                self.putAI(self.b9, "b9")




    #algorytm minmax
    def minimax(self,depth,isMaximizing):
        result = self.checkWinner()
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
                        score = self.minimax(depth+1,False)
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
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = "."
                        bestScore = min(score,bestScore)
            return bestScore


    #obsluga postawienia kolka lub krzyzyka na planszy
    def click(self,button,whichOne):
         if( self.player == "O"):
            button.config(image=self.kolko,state=DISABLED,width=266,height=266)
            self.updateBoard(whichOne, self.player)
            self.whoIsNext = self.computer
            if( self.checkIfEnd(self.player)== True ):
                return


         elif( self.player == "X"):
            button.config(image=self.krzyzyk, state=DISABLED, width=266, height=266)
            self.updateBoard(whichOne, self.player)
            self.whoIsNext = self.computer
            if( self.checkIfEnd(self.player) == True ):
                return


         if self.isOver == False:
             self.best_move()



    #wygenerowanie interfejsu wybrania kolka lub krzyzyka
    def newGame(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = "."
        self.root.title("TicTacToe")
        self.isOver = False
        self.root.resizable(width=False, height=False)
        self.root.geometry("800x800")
        self.root.config(bg="AntiqueWhite1")
        myFont = Font(family="Cooper Black", size=30, weight="bold", slant="italic")
        # tworzymy tlo dla aplikacji
        label = Label(self.root, text="Choose figure", bg="AntiqueWhite1", fg="black", font=myFont, width=30)
        label.place(anchor='nw')
        oButton = Button(self.root, bg="AntiqueWhite1", fg="AntiqueWhite1", image=self.kolko, width=350, height=350,
                         command=self.initBoardFromO)
        xButton = Button(self.root, bg="AntiqueWhite1", fg="AntiqueWhite1", image=self.krzyzyk, width=350, height=350,
                         command=self.initBoardFromX)
        oButton.pack(side=LEFT)
        xButton.pack(side=RIGHT)


    def checkIfEnd(self,figure):
        if( self.board[0][0] == figure and self.board[1][1] == figure and self.board[2][2] == figure or
            self.board[0][0] == figure and self.board[1][0] == figure and self.board[2][0] == figure or
            self.board[0][0] == figure and self.board[0][1] == figure and self.board[0][2] == figure or
            self.board[0][1] == figure and self.board[1][1] == figure and self.board[2][1] == figure or
            self.board[0][2] == figure and self.board[1][2] == figure and self.board[2][2] == figure or
            self.board[0][2] == figure and self.board[1][1] == figure and self.board[2][0] == figure or
            self.board[1][0] == figure and self.board[1][1] == figure and self.board[1][2] == figure or
            self.board[2][0] == figure and self.board[2][1] == figure and self.board[2][2] == figure):
            info = "wygral " + str(figure)
            self.isOver = True
            messagebox.showinfo("Koniec gry", info)
        elif( self.isOver == False ):
            for i in range(3):
                for j in range(3):
                    if( self.board[i][j] == "."):
                        return
            info = "remis "
            self.isOver = True
            messagebox.showinfo("Koniec gry", info)

        if( self.isOver == True ):
            self.clearRoot()
            self.newGame()
            return True


    #Do refaktoryzacji!!!!!!!!
    def updateBoard(self,button,figure):
        if( button == "b1"):
            self.board[0][0] = figure
        elif (button == "b2"):
            self.board[0][1] = figure
        elif (button == "b3"):
            self.board[0][2] = figure
        elif (button == "b4"):
            self.board[1][0] = figure
        elif (button == "b5"):
            self.board[1][1] = figure
        elif (button == "b6"):
            self.board[1][2] = figure
        elif (button == "b7"):
            self.board[2][0] = figure
        elif (button == "b8"):
            self.board[2][1] = figure
        elif (button == "b9"):
            self.board[2][2] = figure

        # for i in range(3):
        #     print(self.board[i],"\n")
        # print("\n\n")

    def checkWinner(self):
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




def main():
    root = Tk()
    gui = Menu(root)
    mainloop()

if __name__ == "__main__":
    main()














