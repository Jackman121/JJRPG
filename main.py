# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame, Enemy, Player, Combat_Engine, os

PLAYER_STRIKE = 0
ENEMY_STRIKE = 1
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

pygame.init()

pygame.display.set_caption("JJRPG")

Enemy1 = Enemy.Enemy("Unferda Brandon",100, 50, 15)
Player = Player.Player("Jack", 100, 50, 25)
Combat_Engine = Combat_Engine.Combat_Engine()

print(Enemy1)
print(Player)

Combat_Engine.combat(Player, Enemy1, PLAYER_STRIKE)

print(Enemy1)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

clock = pygame.time.Clock()
dt = 0

enemy_pos = pygame.Vector2(screen.get_width() - screen.get_width() / 4, screen.get_height() / 2)
player_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2)

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
text = font.render(Player.get_health(), True, "white", "black")

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 - 75)

#Pygame loop
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.circle(screen, "green", player_pos, 40)
    pygame.draw.circle(screen, "red", enemy_pos, 40)

    screen.blit(text, textRect)




    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()
