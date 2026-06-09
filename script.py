import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()  # Used to control frame rate

# --- PHYSICS SETUP ---
# Gravitational constant (adjusted for pixel scale)
G = 10 

# Satellite 1 (Heavy "Sun" at the center)
M1 = 10000
x1, y1 = 400.0, 400.0
vx1, vy1 = 0.0, 0.0

# Satellite 2 (Light "Planet" starting to the side)
M2 = 1
x2, y2 = 400.0, 200.0
# Giving it an initial sideways velocity so it orbits instead of falling straight in
vx2, vy2 = 15.0, 5.0 

running = True
while running:
    # Maintain 60 frames per second. dt is time passed per frame (approx 0.016 seconds)
    dt = clock.tick(60) / 100 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. Calculate distance (R) and direction components
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

    # 5. Update Velocities (v = v + a * dt)
    vx1 += ax1 * dt
    vy1 += ay1 * dt
    vx2 += ax2 * dt
    vy2 += ay2 * dt

    # 6. Update Positions (x = x + v * dt)
    x1 += vx1 * dt
    y1 += vy1 * dt
    x2 += vx2 * dt
    y2 += vy2 * dt

    # --- DRAWING ---
    screen.fill((0, 0, 0))

    # Draw Heavy Object (Yellow)
    pygame.draw.circle(screen, (255, 215, 0), (int(x1), int(y1)), 15)
    # Draw Light Object (White)
    pygame.draw.circle(screen, (255, 255, 255), (int(x2), int(y2)), 7)

    pygame.display.flip()

pygame.quit()