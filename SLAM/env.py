import math 
import pygame

class buildEnvironment:
    def __init__(self, MapDimension):
        pygame.init()
        self.pointCloud = []
        self.externalMap = pygame.image.load("floor.png")
        self.maph, self.mapw = MapDimension
        self.MapWindowName = 'RRT path planning'
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.mapw, self.maph))
        self.map.blit(self.externalMap, (0, 0))

        self.black = (0, 0, 0)
        self.gray = (70, 70, 70)
        self.Blue = (0, 0, 255)
        self.Green = (0, 255, 0)
        self.Red = (255, 0, 0)
        self.white = (255, 255, 255)
    
    def AD2pos(self, distance, angle, robotPosition):
        x = int(robotPosition[0] + distance * math.cos(angle))
        y = int(robotPosition[1] - distance * math.sin(angle))
        return x, y
    
    def dataStorage(self, data):
        for element in data:
            point = self.AD2pos(element[0], element[1], element[2])
            if point not in self.pointCloud:
                self.pointCloud.append(point)

    def show_sensordata(self):
        self.infomap = self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at((int(point[0]), int(point[1])), (255, 0, 0))
