import sys
from math import radians, sin, cos
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE

pygame.init()
polygon_number = int(input("数字を入力してください"))
SURFACE = pygame.display.set_mode((720, 480))
FPSCLOCK = pygame.time.Clock()
angle = 180 * (polygon_number - 2) // polygon_number
circle = angle * polygon_number

def main():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
#                elif event.type == KEYDOWN:
#                    if event.key == K_SPACE:
#                        resturt()
            SURFACE.fill((0, 0, 0))
            
            pointlist = []
            for theta in range(0, circle, angle):
                rad = radians(theta)
                pointlist.append((cos(rad)*150 + 360, sin(rad)*150 + 240))

            pygame.draw.lines(SURFACE, (255, 255, 255), True, pointlist)

            pygame.display.update()
            FPSCLOCK.tick(3)
if __name__ == "__main__":
    main()





    

