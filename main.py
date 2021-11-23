import random
import pygame
from pygame.math import Vector2
import core
from soleil import soleil
from planetes import planetes

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [1000, 1000]

    core.memory("Tablesoleil", [])
    core.memory("Soleil", soleil())
    core.memory("Tableplanetes", [])
    core.memory("Planetes", planetes())

    for i in range(1):
        core.memory("Tablesoleil").append(soleil())
    for i in range(10):
        core.memory("Tableplanetes").append(planetes())



    print("Setup END-----------")


def run():
    print("running")
    core.cleanScreen()

    core.printMemory()
    for i in core.memory("Tablesoleil"):
        i.draw(core.screen)

    core.printMemory()
    core.memory("Soleil").draw(core.screen)

    core.printMemory()
    for i in core.memory("Tableplanetes"):
        i.draw(core.screen)

    core.printMemory()
    core.memory("Planetes").draw(core.screen)
core.main(setup, run)
