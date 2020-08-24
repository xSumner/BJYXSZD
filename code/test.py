import os
import sys
import time
import pygame
import random


WIDTH = 400
HEIGHT = 400
NUMGRID = 8
GRIDSIZE = 36
XMARGIN = (WIDTH - GRIDSIZE * NUMGRID) // 2
YMARGIN = (HEIGHT - GRIDSIZE * NUMGRID) // 2
ROOTDIR = os.getcwd()
FPS = 30
screen.fill((255, 255, 220))
# 游戏界面的网格绘制
def drawGrids(self):
    for x in range(NUMGRID):
        for y in range(NUMGRID):
            rect = pygame.Rect((XMARGIN+x*GRIDSIZE, YMARGIN+y*GRIDSIZE, GRIDSIZE, GRIDSIZE))
            self.drawBlock(rect, color=(255, 165, 0), size=1
# 画矩形 block 框
def drawBlock(self, block, color=(255, 0, 0), size=2):
    pygame.draw.rect(self.screen, color, block, size)


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('博君一肖笑笑乐！')

