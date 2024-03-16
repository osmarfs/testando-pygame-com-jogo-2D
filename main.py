import pygame
from baú.player import Player
import baú.database


pygame.init()


janela = pygame.display.set_mode([840, 600])
pygame.display.set_caption("Testando pygame")
clock = pygame.time.Clock()
on = True
dt = 0
baú.Database.getData()
#player
playerGroup = pygame.sprite.Group()
player = Player(playerGroup)


while on:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    janela.fill([25,25,25])

    playerGroup.update()
    playerGroup.draw(janela)

    pygame.display.update()
