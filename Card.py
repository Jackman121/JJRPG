import pygame

class Card:
    def __init__(self, name, cost, effect):
        self.name = name
        self.cost = cost
        self.effect = effect

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        image = self.image.convert_alpha()
        surface.blit(image, (self.rect.x, self.rect.y))

        return action