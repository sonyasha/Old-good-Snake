import turtle

class Window():
    def __init__(self):
        self.win = turtle.Screen()
        self.win.bgcolor('pink')
        self.onclick(self.quit, 'q')
        self.win.listen()


    def main(self):
        self.win.mainloop()

    def quit(self):
        self.win.bye()


