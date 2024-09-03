# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame, Characters, Combat_Engine, os

#Set constants
PLAYER_STRIKE = 0
ENEMY_STRIKE = 1
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
dt = 0

#Initialize engines as well as characters and display name
pygame.init()
Combat_Engine = Combat_Engine.Combat_Engine()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("JJRPG")

#Create 2 characters and perform a combat action
Enemy1 = Characters.NPC("Unferda Brandon",125, 50, 15)
Player = Characters.Player("Jack", 100, 50, 25)

print(Enemy1)
print(Player)

Combat_Engine.combat(Player, Enemy1, PLAYER_STRIKE)

print(Enemy1)




#Set up some rudimentary visuals
enemy_pos = pygame.Vector2(screen.get_width() - screen.get_width() / 4, screen.get_height() / 2)
player_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2)

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
player_hp = font.render(Player.get_health(), True, "white", "black")
enemy_hp = font.render(Enemy1.get_health(), True, "white", "black")
# create a rectangular object for the
# text surface object
player_hp_rect = player_hp.get_rect()
enemy_hp_rect = enemy_hp.get_rect()

# set the center of the rectangular object.
player_hp_rect.center = (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 - 75)
enemy_hp_rect.center = (SCREEN_WIDTH - SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 - 75)


#Pygame loop
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.circle(screen, "green", player_pos, 40)
    pygame.draw.circle(screen, "red", enemy_pos, 40)

    screen.blit(player_hp, player_hp_rect)
    screen.blit(enemy_hp, enemy_hp_rect)




    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()
