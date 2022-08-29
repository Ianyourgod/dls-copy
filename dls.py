import pygame
from pygame.locals import *
pygame.init()

class inputs(pygame.sprite.Sprite):
    def __init__(self,x,y) -> None:
        super().__init__()
        self.image = pygame.image.load("imgs/notcopyedplsnosue.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (113, 75)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

DIM = (2050,1100)
wn = pygame.display.set_mode((DIM))
pygame.display.set_caption("Digital logic sim by Ianyourgod")
wn.fill((40,40,40))
pygame.draw.rect(
    wn,
    (20,20,20),
    (0,0,65,DIM[1])
    )

FPS_CLOCK = pygame.time.Clock()

inputsdict = {}
id = 0
inputsgroup = pygame.sprite.Group()


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if mousepos[0] < 66:
                inputsdict[id] = inputs(10,mousepos[1] - 75/2)
                inputsgroup.add(inputsdict[id])
    pygame.display.flip()
    inputsgroup.draw(wn)
    FPS_CLOCK.tick(60)
pygame.quit()