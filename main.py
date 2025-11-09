import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame_ver = pygame.version.ver

def main():
    print(f"Starting Asteroids!") # with pygame version: {pygame_ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
