import pygame

pygame.init()

win = pygame.display.set_mode((500,480)) #Setea la pantalla de inicio, win significa window
pygame.display.set_caption("Mi Primer Juego") #Permite ponerle un titulo al juego

walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 10
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def reddrawGameWindow():
    global walkCount
    win.blit(bg,(0,0)) #Setea la foto del background
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        win.blit(char,(x,y))

    pygame.display.update() #Esto me permite que se refresque la pantalla y me aparezca el rectangulo que recien genere.


run = True
while run:  #MAINLOOP
    clock.tick(60)
    pygame.time.delay(80)
    for event in pygame.event.get(): #Esto me consigue una lista de todos los eventos que sucedan, desde mover el mouse hasta apretar una tecla
        if event.type == pygame.QUIT: #QUIT es si aprete el boton de cerrar en la esquina
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and  x > vel: #Pregunta si la tecla apretada fue flecha a la izquierda y no se sale de la pantalla
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel: #Pregunta si la tecla apretada fue flecha a la derecha
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >=-10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    reddrawGameWindow()





pygame.quit()
