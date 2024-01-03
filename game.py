from tkinter import *
from PIL import ImageTk

class Game(Canvas):

    def __init__(self, w, h):
        super().__init__(width=w, height=h, background='black', highlightthickness=0)

    def create_object(self, objects, position, tagname):
        #create object
        for x_pos, y_pos in position:
            self.create_image(x_pos, y_pos, image=objects, tags=tagname)


class Snake:
    def __init__(self):
        # position        head--------------------tail
        self.position = [(100,100), (80, 100), (60, 100)]
        self.snake = ImageTk.PhotoImage(file='assets/body.png')
    
    def getPostion(self):
        return self.position 

    def setPostion(self, x, y):
        pass
        

    
    def get_assets(self):
        return self.snake

    def create_object_snake(self):
        pass

if __name__ == '__main__':
    app = Tk()

    # Create field game
    game = Game(600, 620)

    # Snake
    snake = Snake() # First Snake
    object_snake = snake.get_assets()
    snake_position = snake.getPostion()
    game.create_object(objects=object_snake, position=snake_position, tagname='snake')
    

    game.pack()
    app.mainloop()





