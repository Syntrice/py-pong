import pygame as pg
import color

class Application():
    
    def __init__(self, win_caption, win_size=(700, 500)):
        #initialize pygame library
        pg.init()

        # open a new window
        self.WIN_SIZE = win_size # set window size
        self.screen = pg.display.set_mode(self.WIN_SIZE) # returns a surface object
        pg.display.set_caption(win_caption) # set window caption

        # clock controls how fast screen updates
        self.clock = pg.time.Clock()
        
    def check_events(self):
        for event in pg.event.get(): # user did something
                if event.type == pg.QUIT: # user clicked close
                    pg.quit()

    def render(self):
        self.screen.fill(color.BLACK)
        pg.draw.line(self.screen, color.WHITE, [349,0],[349,500], 5)
        pg.display.flip()
    
    def run(self):
        while True:
            self.check_events()
            self.render()


if __name__ == '__main__':
    app = Application("Pong")
    app.run()
