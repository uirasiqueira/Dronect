import pygame

def init():
    pygame.init()
    window = pygame.display.set_mode((400,400))

def getKey(KeyName):
    ans = False
    for eve in pygame.event.get(): pass
    KeyInput = pygame.key.get_pressed()
    mykey = getattr(pygame, 'K_{}'.format(KeyName))
    if KeyInput[mykey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getkey('LEFT'):
        print('Left key pressed')
    if getkey('RIGHT'):
        print('Right key pressed')

if __name__ == '__main__':
    init()
    while True:
        main()