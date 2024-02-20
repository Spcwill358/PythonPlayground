import pygame
import time
import random

# Defines the size of the Game Screen in pixels
WIDTH = 1000
HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("NAME OF GAME HERE") # Set the title here

# Main game loop
def main():
    gameRunning = True

    while gameRunning:
        # Checks if user presses the X button at top-right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
                break

    pygame.quit()

if __name__ == "__main__":
    main()