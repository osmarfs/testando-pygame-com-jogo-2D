import pygame


class Database:
    def __init__(self):
        self._textures = {}
        self._sounds = {}

        self._data = database.Database()

    def getTexture(self,filename):
        if filename not in self._textures:
            self._textures[filename] = pygame.image.load(filename).convert_alpha()
        return self._textures[filename]

    def getData(self):
        return self._data