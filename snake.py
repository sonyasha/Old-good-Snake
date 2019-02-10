from turtle import Turtle, Screen
from tkinter import TclError

class Game():
    def __init__(self):
        self.win = Screen()
        self.win.bgcolor('pink')
        # self.win.setup(width=w, height=h, startx=None, starty=None)

        self.border = Border()
        width, height = self.win.window_width(), self.win.window_height()
        print(width, height)
        self.border.draw_self((width, height))

        self.turtle = Arrow()
        self.win.onkey(self.quit, 'q')
        self.win.onkey(self.arrow_left, 'Left')
        self.win.onkey(self.arrow_right, 'Right')
        self.win.onkey(self.arrow_up, 'Up')
        self.win.onkey(self.arrow_down, 'Down')
        self.win.listen()
        
        self.win.onclick(self.check_coord)
        
        self.increase_speed()
        self.move_arrow()

    def check_coord(self, x, y):
        print(x,y)

    def quit(self):
        self.win.bye()

    def move_arrow(self):
        self.turtle.move()
        self.win.ontimer(self.move_arrow, 50)

    def arrow_left(self):
        self.turtle.turn_left()

    def arrow_right(self):
        self.turtle.turn_right()

    def arrow_up(self):
        self.turtle.turn_up()

    def arrow_down(self):
        self.turtle.turn_down()

    def increase_speed(self):
        self.turtle.speedup()
        self.win.ontimer(self.increase_speed, 3000)

    def main(self):
        self.win.mainloop()

class Border(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color('blue')
        self.pensize(5)

    def draw_self(self, coord):
        # self.goto(-coord[1]/2+10, coord[0]/2-10)
        # self.pendown()
        # self.goto(coord[1]/2-20, coord[0]/2-10)
        # self.goto(coord[1]/2-20, -coord[0]/2+20)
        # self.goto(-coord[1]/2+10, -coord[0]/2+20)
        # self.goto(-coord[1]/2+10, coord[0]/2-10)
        self.goto(-320, 300)
        self.pendown()
        self.goto(310, 300)
        self.goto(310, -290)
        self.goto(-320, -290)
        self.goto(-320, 300)
        self.hideturtle()

class Arrow(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.penup()
        self.color('green')
        self.shape('turtle')
        self.speed(1)
        self.nextX = 1
        self.nextY = 0

    def move(self):
        self.forward(self.speed())
        if self.xcor() > 310:
            self.hideturtle()
            self.goto(-320, self.ycor())
            self.showturtle()
        elif self.xcor() < -320:
            self.hideturtle()
            self.goto(310, self.ycor())
            self.showturtle()
        elif self.ycor() > 300:
            self.hideturtle()
            self.goto(self.xcor(), -290)
            self.showturtle()
        elif self.ycor() < -290:
            self.hideturtle()
            self.goto(self.xcor(), 300)
            self.showturtle()

    def turn_right(self):
        self.setheading(0)
    
    def turn_left(self):
        self.setheading(180)

    def turn_up(self):
        self.setheading(90)

    def turn_down(self):
        self.setheading(270)

    def speedup(self):
        if self.speed() < 10:
            new_speed = int(self.speed())
            new_speed += 1
            self.speed(new_speed)

    def getx(self):
        return self.x

    def gety(self):
        return


def start():
    wn = Game()
    
    wn.main()

if __name__ == '__main__':
    start()