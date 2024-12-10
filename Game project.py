pygame
import sys
import math
import random

pygame.init()

SCREEN_WIDTH = 1050
SCREEN_HEIGHT = 950
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('game')

background_img = pygame.image.load('spacebg.png').convert()

novasprite_img = pygame.image.load('novasprite.png').convert_alpha()
player_rect = novasprite_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

star_img = pygame.image.load('star.png').convert_alpha()
asteroid_img = pygame.image.load('asteroid.png').convert_alpha()

titlecard_img = pygame.image.load('titleimage.png').convert()
titlecard_rect = titlecard_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

spacebar_img = pygame.image.load('spacebar.png').convert_alpha()
spacebar_rect = spacebar_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))

# Load and resize clicksprite.png
clicksprite_img = pygame.image.load('clicksprite.png').convert_alpha()
clicksprite_img = pygame.transform.scale(clicksprite_img, (150, 150))  
harold_img = pygame.image.load('harold.png').convert_alpha()

# Flag to indicate whether to show sprites on title screen
show_sprites_on_title_screen = True

player_speed = 5
jump_strength = 10
wiggle_amplitude = 3  # Amplitude of player wiggle effect
wiggle_frequency = 0.1  # Frequency of player wiggle effect
wiggle_angle = 0  # Initialize player wiggle angle

stars = []  # List to hold star positions
projectiles = []  # List to hold projectile positions
projectile_speed = 4

score = 0
font = pygame.font.Font(None, 36)

# Modify the size of the collision rectangle for projectiles
PROJECTILE_HITBOX_SIZE = 3


def jump():
    global is_jumping
    if not is_jumping:
        is_jumping = True
        player_rect.y -= jump_strength

def spawn_star():
    star_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 300)  # Spawn stars outside the screen
    star_y = random.randint(20, SCREEN_HEIGHT - 20)
    stars.append(pygame.Rect(star_x, star_y, star_img.get_width(), star_img.get_height()))

def spawn_projectile():
    projectile_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 300)  # Spawn projectiles outside the screen
    projectile_y = random.randint(50, SCREEN_HEIGHT - 50)
    projectiles.append(pygame.Rect(projectile_x, projectile_y, PROJECTILE_HITBOX_SIZE, PROJECTILE_HITBOX_SIZE))

def spawn_background_objects():
    # Spawn the background objects once when the game starts
    background_objects = [clicksprite_img, harold_img]
    for obj in background_objects:
        obj_x = random.randint(0, SCREEN_WIDTH)
        obj_y = random.randint(0, SCREEN_HEIGHT)
        screen.blit(obj, (obj_x, obj_y))

def move_projectiles():
    for projectile in projectiles:
        projectile.x -= projectile_speed

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def restart_game():
    global player_rect, stars, projectiles, score
    player_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    stars = []
    projectiles = []
    score = 0
    spawn_star()
    spawn_projectile()

clock = pygame.time.Clock()

spawn_star()  # Initial star spawn
spawn_projectile()  # Initial projectile spawn

game_over = False
menu_active = True  # Flag to indicate if the menu is active

fade_alpha = 255  # Initial alpha value for fading
spacebar_wiggle_amplitude = 10  # Larger amplitude for a more noticeable glide
spacebar_wiggle_frequency = 0.03  # Smaller increment for smoother movement
spacebar_wiggle_angle = 0  # Initialize wiggle angle

# Fixed position for the spacebar image
spacebar_fixed_y = SCREEN_HEIGHT // 2 + 150  # Static Y-coordinate for spacebar image

while menu_active:
    # Draw the titlecard
    screen.blit(titlecard_img, titlecard_rect)

    # Apply fade effect for titlecard image
    titlecard_img.set_alpha(fade_alpha)

    # Draw spacebar image at a fixed position
    screen.blit(spacebar_img, (spacebar_rect.x, spacebar_fixed_y))

    # Update the screen
    pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu_active = False

    # Gradually decrease alpha for fade effect
    fade_alpha -= 5
    if fade_alpha < 0:
        fade_alpha = 0



while not game_over:
    screen.blit(background_img, (0, 0))
    
    # Apply wiggle effect to the player
    wiggle_offset = wiggle_amplitude * math.sin(wiggle_angle)
    player_rect.y += wiggle_offset
    wiggle_angle += wiggle_frequency
    
    screen.blit(novasprite_img, player_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect.x -= player_speed
    if keys[pygame.K_d]:
        player_rect.x += player_speed
    if keys[pygame.K_w]:
        player_rect.y -= player_speed
    if keys[pygame.K_s]:
        player_rect.y += player_speed
    
    # Ensure player stays within screen boundaries
    if player_rect.top < 0:
        player_rect.top = 0
    elif player_rect.bottom > SCREEN_HEIGHT:
        player_rect.bottom = SCREEN_HEIGHT

    # Move and draw stars
    for star in stars:
        screen.blit(star_img, star)
        star.x -= player_speed
        if star.colliderect(player_rect):
            stars.remove(star)
            score += 1
            spawn_star()

    # Move and draw projectiles
    move_projectiles()
    for projectile in projectiles:
        screen.blit(asteroid_img, projectile)
        if projectile.colliderect(player_rect.inflate(-5, -5)):  # Decrease the size of player_rect for less sensitivity
            game_over = True


    # Remove off-screen stars and projectiles
    stars = [star for star in stars if star.x + star.width > 0]
    projectiles = [projectile for projectile in projectiles if projectile.x + projectile.width > 0]

    # Draw score
    draw_text(f"Score: {score}", font, (255, 255, 255), screen, 10, 10)

    if random.randint(0, 100) < 1:  # Adjust the probability to control the frequency
        spawn_projectile()
    if random.randint(0, 100) < 1:  # Adjust the probability to control the frequency
        spawn_star()

    pygame.display.update()
    clock.tick(60)

# Game over loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                restart_game()
                game_over = False
                break

    draw_text("Game Over!", font, (255, 255, 255), screen, SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2)
    
    pygame.display.update()
    clock.tick(60)
