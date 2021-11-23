import random
import pygame
from pygame.math import Vector2

class planetes :
    def __init__(self):
        self.rayon =(random.randint(15, 30))
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position = Vector2(random.randint(0,1000), random.randint(0, 1000))
        self.vitesse = 10
        self.masse = 5
        self.gravite = 20

    def deplacer(self):
        pass

    def draw (self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)