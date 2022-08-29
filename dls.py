import pygame
from pygame.locals import *
pygame.init()

class inputs(pygame.sprite.Sprite):
    def __init__(self,x,y,width=113,height=75) -> None:
        super().__init__()
        self.image = pygame.image.load("imgs/offinput.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width,self.height = width,height
    def swap(self):
        if self.image == pygame.image.load("imgs/offinput.png").convert_alpha():
            self.image = pygame.image.load("imgs/oninput.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        else:
            self.image = pygame.image.load("imgs/oninput.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            

DIM = (1000,750)
wn = pygame.display.set_mode(DIM, pygame.RESIZABLE)
pygame.display.set_caption("Digital logic sim by Ianyourgod")

FPS_CLOCK = pygame.time.Clock()

inputsdict = {}
id = 0
inputsgroup = pygame.sprite.Group()

running = True
while running:
    w, h = pygame.display.get_surface().get_size()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in inputsgroup if s.rect.collidepoint(mousepos)]
            for i in clicked_sprites:
                i.swap()
            if mousepos[0] < 66:
                inputsdict[id] = inputs(10,mousepos[1] - 75/2,70,50)
                inputsgroup.add(inputsdict[id])
    pygame.display.flip()
    wn.fill((70,70,70))
    pygame.draw.rect(wn, (40,40,40), pygame.Rect(0, 0, 65, h))
    inputsgroup.draw(wn)
    FPS_CLOCK.tick(60)
pygame.quit()