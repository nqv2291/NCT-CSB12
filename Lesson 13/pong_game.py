import pygame, sys, random


def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # keep ball moving inside the frame
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    
    # ball animations
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def ball_restart():
    global ball_speed_x, ball_speed_y

    ball.center = (screen_width/2, screen_height/2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))

def player_animation():
    player.y += player_speed

    # keep player moving inside the frame
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


# general setup
pygame.init()
clock = pygame.time.Clock()

# setup the main window
screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode( (screen_width, screen_height) )
pygame.display.set_caption("Pong game v1.0")

# game Rect
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 75, 10, 150)
opponent = pygame.Rect(10, screen_height/2 - 75, 10, 150)

# game colors
bg_color = pygame.Color("brown")
light_grey = (200, 200, 200)

# object speed
SPEED = 5
player_speed = 0
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))


while True:

    # handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += SPEED
            if event.key == pygame.K_UP:
                player_speed -= SPEED

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= SPEED
            if event.key == pygame.K_UP:
                player_speed += SPEED

    # game logic
    player_animation()
    ball_animation()

    
    # visuals
    screen.fill(bg_color)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    
    # updating the window
    pygame.display.flip()
    clock.tick(60)