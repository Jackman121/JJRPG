# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame, Characters, Combat_Engine, os, button

#Set constants
PLAYER_STRIKE = 0
ENEMY_STRIKE = 1
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
dt = 0
BLACK = (0,0,0)

#Initialize engines as well as characters and display name
pygame.init()
Combat_Engine = Combat_Engine.Combat_Engine()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("JJRPG")
attackBOOTON_sprites_sheet = pygame.image.load("./Assets/attackBOOTONS.png").convert_alpha()
war_background = pygame.image.load("./Assets/War_Background.png").convert_alpha()
war_background = pygame.transform.scale(war_background, (SCREEN_WIDTH, SCREEN_HEIGHT))




#Function to cut a single sprite from a sheet
def get_sprite(sprite_sheet, width, height,scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sprite_sheet,(0,0), (0,0,width,height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image

attackBOOTON = get_sprite(attackBOOTON_sprites_sheet,188, 192, 0.2, BLACK)

#Create 2 characters and perform a combat action
Enemy1 = Characters.NPC("Unferda Brandon",125, 50, 15)
Player = Characters.Player("Jack", 100, 50, 25)


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
player_hp = font.render(Player.get_health(), True, "white")
enemy_hp = font.render(Enemy1.get_health(), True, "white")
# create a rectangular object for the
# text surface object
player_hp_rect = player_hp.get_rect()
enemy_hp_rect = enemy_hp.get_rect()

# set the center of the rectangular object.
player_hp_rect.center = (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 - 75)
enemy_hp_rect.center = (SCREEN_WIDTH - SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 - 75)

#Make attack button
attack_button = button.Button(SCREEN_WIDTH / 4 + 35, SCREEN_HEIGHT / 2 - 50, attackBOOTON, 1)


#Pygame loop
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(war_background, war_background.get_rect())

    #screen.blit(attackBOOTON,(SCREEN_WIDTH / 4 + 35, SCREEN_HEIGHT / 2 - 50))
    if attack_button.draw(screen):
        Combat_Engine.combat(Player, Enemy1, PLAYER_STRIKE)
        print(Enemy1.get_health())
        enemy_hp = font.render(Enemy1.get_health(), True, "white")
        #enemy_hp_rect = enemy_hp.get_rect()
        #enemy_hp_rect.center = (SCREEN_WIDTH - SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2 - 75)


    pygame.draw.circle(screen, "green", player_pos, 40)
    pygame.draw.circle(screen, "red", enemy_pos, 40)

    screen.blit(player_hp, player_hp_rect)
    screen.blit(enemy_hp, enemy_hp_rect)




    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
