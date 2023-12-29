from tkinter import *


class Field(Canvas):

    def __init__(self, w, h):
        super().__init__(width=w, height=h, background='black', highlightthickness=0)



class Snake:
    def __init__(self):
        pass        
    
    

if __name__ == '__main__':
    game = Tk()

    # Create field game
    fieldgame = Field(600, 620)
    fieldgame.pack()

    # Snake

    game.mainloop()





