from tkinter import *
from PIL import ImageTk
from random import randint

class Game(Canvas):
    def __init__(self, snake, food):
        super().__init__(width=600, height=620, background='black', highlightthickness=0)
        self.snake = snake
        self.food = food

        self.direction = 'Right'
        self.bind_all('<Key>', self.onKeyPress)

    def createObjectSnake(self):
        #create object and forloop for draw box body snake
        position = self.snake.getPosition()
        imageBody = self.snake.getImageBody()
        for x_pos, y_pos in position:
            self.create_image(x_pos, y_pos, image=imageBody, tags='snake')

    def createObjectFood(self):
        position = self.food.getPosition()
        imageFood = self.food.getImageFood()
        #Draw food
        self.create_image(position, image=imageFood, tags="food")

    def moveObjectSnake(self):
        position = self.snake.getPosition()        
        headx, heady = position[0]

        if self.direction == 'Right':
            newPosition = [(headx + 20, heady)] + position[:-1]
        if self.direction == 'Left':
            newPosition = [(headx - 20, heady)] + position[:-1]
        if self.direction == 'Up':
            newPosition = [(headx, heady - 20)] + position[:-1]
        if self.direction == 'Down':
            newPosition = [(headx, heady + 20)] + position[:-1]

        self.snake.setPosition(newPosition) 
        self.drawSnakeMove(newPosition)

    def drawSnakeMove(self, newPosition): 
        tagsIdSnakes = self.find_withtag('snake')
        for tagsIdSnakes, position in zip(tagsIdSnakes, newPosition):
            self.coords(tagsIdSnakes, position)

    def snakeCollisionFood(self):
        headSnake = self.snake.getPosition()[0]
        foodPosition = self.food.getPosition()

        tagsIdFood = self.find_withtag('food')
        if headSnake == foodPosition:
            xPosFoodRandom = randint(1, 29) * 20
            yPosFoodRandom = randint(1, 29) * 20
            self.food.setPosition((xPosFoodRandom, yPosFoodRandom))
            self.coords(tagsIdFood, (xPosFoodRandom, yPosFoodRandom))
            self.addTailSnake()
    
    def snakeCollisionWall(self):
        headx, heady = self.snake.getPosition()[0]
        if headx < 20 or headx > 580 or heady < 20 or heady > 600:  
            self.startGameOver()

    def snakeCollisionBody(self):
        positionSnake = self.snake.getPosition()
        headSnake = positionSnake[0]
        bodySnake = positionSnake[1:]
        if headSnake in bodySnake:
            self.startGameOver()

    def startGameOver(self):
        #delete all images
        self.delete("all") 
        # reset position all
        self.snake.setPosition([(60, 200)])
        xPosFoodRandom = randint(1, 29) * 20
        yPosFoodRandom = randint(1, 29) * 20
        self.food.setPosition((xPosFoodRandom, yPosFoodRandom))
        self.direction = "Right"
        # draw image again
        self.createObjectSnake()
        self.createObjectFood()

    def addTailSnake(self):
        imageBodySnake = self.snake.getImageBody()
        snakePosition = self.snake.getPosition()
        tailSnakePosition = [snakePosition[-1]]
        newSnakePosition = snakePosition + tailSnakePosition 
        self.snake.setPosition(newSnakePosition)
        self.create_image(tailSnakePosition, image=imageBodySnake, tags='snake') 

    def runGame(self):
        self.moveObjectSnake()
        self.snakeCollisionWall()
        self.snakeCollisionBody()
        self.snakeCollisionFood()
        self.after(50, self.runGame)

    def onKeyPress(self, e):
        direction = e.keysym
        if ((direction == "Right" or direction == "Left") and (self.direction == "Up" or self.direction == "Down")):
            self.direction = direction
        elif ((direction == "Up" or direction == "Down") and (self.direction == "Left" or self.direction == "Right")):
            self.direction = direction

class Snake:
    def __init__(self):
        # position        head--------------------tail
        # self.position = [(100,100), (80, 100), (60, 100)]
        self.position = [(60, 200)]
        self.imageBody = ImageTk.PhotoImage(file="assets/body.png")

    def getPosition(self):
        return self.position 

    def setPosition(self, newPosition):
        self.position = newPosition

    def getImageBody(self):
        return self.imageBody

class Food():
    def __init__(self):
        xPosRandom = randint(1, 29) * 20
        yPosRandom = randint(1, 29) * 20
        self.position = (xPosRandom, yPosRandom) 
        self.imageFood = ImageTk.PhotoImage(file="assets/food.png")   
    
    def getPosition(self):
        return self.position
    
    def setPosition(self, newPosition):
        self.position = newPosition

    def getImageFood(self):
        return self.imageFood

if __name__ == '__main__':
    app = Tk()
    app.title("Snake Game")
    app.resizable(False, False) #Fixed Size
    #create class snake and class food
    snake = Snake()
    food = Food()
    # Create field game
    game = Game(snake, food)
    game.createObjectSnake()
    game.createObjectFood()
    game.runGame()


    game.pack()
    app.mainloop()
