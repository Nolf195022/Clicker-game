import pygame as pg
import sys
pg.init()
WIDTH, HEIGHT = 600,900
WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Clicker Game")
WHITE = (255,255,255)
BLACK = (0,0,0)
border_margin = 40
font_style = pg.font.get_default_font()

def default_window():
    WIN.fill(BLACK)
    pg.draw.rect(WIN, WHITE,(border_margin/2,border_margin/2,WIDTH-border_margin,HEIGHT-border_margin), width=3)
    pg.draw.rect(WIN, BLACK,(border_margin/2,border_margin/2,WIDTH-border_margin,HEIGHT-border_margin))

def draw_text(text, size, x, y):
    font  =pg.font.Font(font_style,size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    WIN.blit(text_surface,text_rect)

class Button():
    def __init__(self, bgcolor, textcolor,x,y,width,height, text=''):
        self.bgcolor = bgcolor
        self.textcolor = textcolor
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pg.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pg.draw.rect(win, self.bgcolor, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pg.font.Font(font_style, 30)
            text = font.render(self.text, 1, self.textcolor)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def game():
    default_window()
    draw_text('à faire', 30, WIDTH/2, 200)
    run = True
    FPS = 60
    clock = pg.time.Clock()
    while run :
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()
        pg.display.update()

def mainmenu():
    default_window()
    draw_text("CLICKER GAME", 30, WIDTH/2, 200)
    play_button = Button(BLACK,WHITE, WIDTH/2-100,500,200,50, text='PLAY')
    play_button.draw(WIN, WHITE)
    run = True
    while run :
        for event in pg.event.get():
            pos = pg.mouse.get_pos()
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if play_button.isOver(pos):
                    game()
            if event.type == pg.MOUSEMOTION:
                if play_button.isOver(pos):
                    play_button.bgcolor = WHITE
                    play_button.textcolor = BLACK
                    play_button.draw(WIN, WHITE)
                else:
                    play_button.bgcolor = BLACK
                    play_button.textcolor = WHITE
                    play_button.draw(WIN, WHITE)
        pg.display.update()
        
mainmenu()
            

