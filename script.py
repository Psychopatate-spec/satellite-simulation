import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 800))
default_font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()  # Used to control frame rate

# --- PHYSICS SETUP ---
# Gravitational constant (adjusted for pixel scale)
G = 10 

# Satellite 1 (Heavy "Sun" at the center, it moves even thought it doesn't look like it's moving much because it's so heavy)
M1 = 10000
x1, y1 = 400.0, 400.0
vx1, vy1 = 0.0, 0.0

# Satellite 2 (Light "Planet" starting to the side)
M2 = 1
x2, y2 = 400.0, 200.0
# Giving it an initial sideways velocity so it orbits instead of falling straight in
vx2, vy2 = 20.0, 0.0

# Satellite 3 (Moon, even thought it doesn't really orbit around the planet in this simple model, it's just influenced by both)
M3 = 0.1
x3, y3 = 400.0, 220.0
vx3, vy3 = 22.0, 10.0

# --- ORBIT TRAILS ---
# Lists to store position history for drawing orbits
trail1 = [(int(x1), int(y1))]
trail2 = [(int(x2), int(y2))]
trail3 = [(int(x3), int(y3))]
max_trail_length = 500  # Limit trail length to prevent memory issues

running = True
paused = False
while running:
    # Maintain 120 frames per second. dt is time passed per frame (approx 0.0083 seconds)
    dt = clock.tick(120) / 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
    if paused:
        continue
                

    # 1. Calculate distance (R) and direction components between Sun (1) and Planet (2)
    dx = x1 - x2
    dy = y1 - y2
    R = math.sqrt(dx**2 + dy**2)

    # Prevent division by zero if they collide perfectly
    if R < 5: 
        R = 5

    # 2. Calculate Gravitational Force Magnitude
    # F = G * (M1 * M2) / R^2
    F = G * (M1 * M2) / (R**2)

    # 3. Break Force into X and Y components using trigonometry (cos = dx/R, sin = dy/R)
    Fx = F * (dx / R)
    Fy = F * (dy / R)

    # 4. Calculate Acceleration (a = F / m)
    # For Object 2, the force pulls TOWARD Object 1 (+Fx, +Fy)
    ax2 = Fx / M2
    ay2 = Fy / M2
    
    # For Object 1, the force pulls TOWARD Object 2 (-Fx, -Fy) -> Newton's 3rd Law
    ax1 = -Fx / M1
    ay1 = -Fy / M1

    # --- FORCES ON MOON (Satellite 3) ---
    # Moon is pulled by the Sun (Satellite 1)
    dx3_sun = x1 - x3
    dy3_sun = y1 - y3
    R3_sun = math.sqrt(dx3_sun**2 + dy3_sun**2)

    if R3_sun < 5:
        R3_sun = 5

    F3_sun = G * (M1 * M3) / (R3_sun**2)
    Fx3_sun = F3_sun * (dx3_sun / R3_sun)
    Fy3_sun = F3_sun * (dy3_sun / R3_sun)

    # Moon is also pulled by the Planet (Satellite 2)
    dx3_planet = x2 - x3
    dy3_planet = y2 - y3
    R3_planet = math.sqrt(dx3_planet**2 + dy3_planet**2)

    if R3_planet < 5:
        R3_planet = 5

    F3_planet = G * (M2 * M3) / (R3_planet**2)
    Fx3_planet = F3_planet * (dx3_planet / R3_planet)
    Fy3_planet = F3_planet * (dy3_planet / R3_planet)

    # Total acceleration on moon is sum of forces from both Sun and Planet
    ax3 = (Fx3_sun + Fx3_planet) / M3
    ay3 = (Fy3_sun + Fy3_planet) / M3

    # 5. Update Velocities (v = v + a * dt)
    vx1 += ax1 * dt
    vy1 += ay1 * dt
    vx2 += ax2 * dt
    vy2 += ay2 * dt
    vx3 += ax3 * dt
    vy3 += ay3 * dt

    # 6. Update Positions (x = x + v * dt)
    x1 += vx1 * dt
    y1 += vy1 * dt
    x2 += vx2 * dt
    y2 += vy2 * dt
    x3 += vx3 * dt
    y3 += vy3 * dt

    # --- UPDATE TRAILS ---
    trail1.append((int(x1), int(y1)))
    trail2.append((int(x2), int(y2)))
    trail3.append((int(x3), int(y3)))
    
    # Limit trail length
    if len(trail1) > max_trail_length:
        trail1.pop(0)
    if len(trail2) > max_trail_length:
        trail2.pop(0)
    if len(trail3) > max_trail_length:
        trail3.pop(0)

    # --- DRAWING ---
    screen.fill((0, 0, 0))

    # Draw orbit trails
    for pos in trail1:
        pygame.draw.circle(screen, (255, 215, 0), pos, 1)
    for pos in trail2:
        pygame.draw.circle(screen, (255, 255, 255), pos, 1)
    for pos in trail3:
        pygame.draw.circle(screen, (128, 128, 128), pos, 1)

    # Draw Heavy Object (Yellow)
    pygame.draw.circle(screen, (255, 215, 0), (int(x1), int(y1)), 15)
    # Draw Light Object (White)
    pygame.draw.circle(screen, (255, 255, 255), (int(x2), int(y2)), 7)
    # Draw Moon (Gray)
    pygame.draw.circle(screen, (128, 128, 128), (int(x3), int(y3)), 5)

    velocity1 = default_font.render("velocity 1: " + str(round(math.sqrt(vx2**2 + vy2**2))), True, (255, 255, 255))
    velocity2 = default_font.render("velocity 2: " + str(round(math.sqrt(vx3**2 + vy3**2))), True, (255, 255, 255))
    distance_text1 = default_font.render("distance 1: " + str(round(R)), True, (255, 255, 255))
    distance_text2 = default_font.render("distance 2: " + str(round(R3_planet)), True, (255, 255, 255))
    fps_text = default_font.render("FPS: " + str(int(clock.get_fps())), True, (255, 255, 255))
    screen.blit(fps_text, (10, 50))
    screen.blit(velocity1, (10, 10))
    screen.blit(velocity2, (10, 30))
    screen.blit(distance_text1, (10, 70))
    screen.blit(distance_text2, (10, 90))

    pygame.display.flip()

pygame.quit()