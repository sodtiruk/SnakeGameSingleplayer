from tkinter import *
from PIL import ImageTk

class Game(Canvas):

    def __init__(self, snake, food):
        super().__init__(width=600, height=620, background='black', highlightthickness=0)
        self.snake = snake
        self.food = food

        self.direction = 'Right'
        self.bind_all('<Key>', self.onKeyPress)

    def createObjectSnake(self):
        #create object and forloop for draw box body snake
        position = self.snake.getPostion()
        imageBody = self.snake.getImageBody()
        for x_pos, y_pos in position:
            self.create_image(x_pos, y_pos, image=imageBody, tags='snake')
            print(x_pos, y_pos) 

    def moveObjectSnake(self):
        position = self.snake.getPostion()        
        headx, heady = position[0]

        if self.direction == 'Right':
            newPosition = [(headx + 20, heady)] + position[:-1]
        if self.direction == 'Left':
            newPosition = [(headx - 20, heady)] + position[:-1]
        if self.direction == 'Up':
            newPosition = [(headx, heady - 20)] + position[:-1]
        if self.direction == 'Down':
            newPosition = [(headx, heady + 20)] + position[:-1]
        
        self.snake.setPostion(newPosition) 

        tagsIdSnakes = self.find_withtag('snake')
        print(tagsIdSnakes)

        #Draw body images snake move 
        for tagsIdSnakes, position in zip(tagsIdSnakes, newPosition):
            self.coords(tagsIdSnakes, position)

    def onKeyPress(self, e):
        direction = e.keysym
        self.direction = direction
        print(self.direction)

    def runGame(self):
        self.moveObjectSnake()
        self.after(500, self.runGame)


class Snake:
    def __init__(self):
        # position        head--------------------tail
        self.position = [(100,100), (80, 100), (60, 100)]
        self.imageBody = ImageTk.PhotoImage(file='assets/body.png')

    def getPostion(self):
        return self.position 

    def setPostion(self, newPosition):
        self.position = newPosition
        print(self.position)        

    def getImageBody(self):
        return self.imageBody

class Food():
    pass
    
   
if __name__ == '__main__':
    app = Tk()
    app.title("Snake Game")
    #create class snake and class food
    snake = Snake()
    food = Food()
    # Create field game
    game = Game(snake, food)
    game.createObjectSnake()
    game.runGame()

    game.pack()
    app.mainloop()

    



