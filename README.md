# ☀️ Build Your Own Solar System with Pygame

A beginner-friendly orbital mechanics simulator built using **Pygame Community Edition (pygame-ce)**.

This project demonstrates how to simulate gravity using **Newton's Law of Universal Gravitation** and create realistic-looking planetary motion.

---

## Features

- Newtonian gravity
- Real-time orbital simulation
- Multiple celestial bodies
- Orbit trails
- HUD displaying velocity, distance and FPS
- Pause functionality

---

## Preview

![Preview](/preview.png)

---

## Requirements

- Python 3.10+
- pygame-ce

Install pygame-ce:

```bash
pip install pygame-ce
```

---

## Project Structure

```text
.
├── README.md
└── script.py
```

---

## Create a Window

Before simulating gravity, we need a window where everything will be displayed.

```python
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Solar System Simulator")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
```

---

## Physics

The core of our simulation is Newton's Law of Universal Gravitation:

```text
F = G * (M1 * M2) / R²
```

Where:

- F is the gravitational force
- G is the gravitational constant
- M1 and M2 are the masses
- R is the distance between them

Using Newton's Second Law:

```text
a = F / m
```

We can compute acceleration.

We then update velocity and position:

```text
v = v + a * dt
x = x + v * dt
```

---

## Step 1 — Creating our first planet

Before we can simulate gravity, we need something that gravity can actually act on.

Let's create two objects:

- A massive Sun
- A much lighter Planet

```python
M1 = 10000
x1, y1 = 400.0, 400.0
vx1, vy1 = 0.0, 0.0

M2 = 1
x2, y2 = 400.0, 200.0
vx2, vy2 = 15.0, 0.0
```

Let's break this down.
M1 and M2 represent the masses of our objects.
The larger the mass, the stronger the gravitational attraction.
x and y represent the position of the object on the screen.
Since our window is 800x800 pixels, (400, 400) places the Sun roughly at the center.
Finally, vx and vy represent velocity.
Think of velocity as the object's current movement speed.
A positive vx means the object moves to the right.
A positive vy means the object moves downward.
We give the Planet an initial horizontal velocity because if we don't, it will simply fall straight into the Sun.

## Understanding Gravity

Imagine you're floating in space.
If a tiny pebble is nearby, you won't feel much attraction.
If a planet is nearby, you'll feel a much stronger pull.

Gravity depends on two things:

1. How massive the objects are.
2. How far apart they are.

The more massive the objects, the stronger the attraction.
The farther apart they are, the weaker the attraction.

Newton summarized this relationship with the equation:

```python
F = G * (M1 * M2) / R²
```

Don't worry if this looks scary.
The computer will handle the math for us.
The important idea is:

Bigger masses = stronger pull
Greater distance = weaker pull

Compute the distance:

```python
dx = x1 - x2
dy = y1 - y2

R = math.sqrt(dx**2 + dy**2)

if R < 5:
    R = 5
```

Compute gravitational force:

```python
F = G * (M1 * M2) / (R**2)
```

Split force into components:

```python
Fx = F * (dx / R)
Fy = F * (dy / R)
```

Compute accelerations:

```python
ax2 = Fx / M2
ay2 = Fy / M2

ax1 = -Fx / M1
ay1 = -Fy / M1
```

Update velocities:

```python
vx1 += ax1 * dt
vy1 += ay1 * dt

vx2 += ax2 * dt
vy2 += ay2 * dt
```

Update positions:

```python
x1 += vx1 * dt
y1 += vy1 * dt

x2 += vx2 * dt
y2 += vy2 * dt
```

---

## Step 2 — Add a Moon

Add a third object:

```python
M3 = 0.1

x3, y3 = 400.0, 220.0

vx3, vy3 = 20.0, 10.0
```

The Moon is affected by both the Sun and the Planet.

Calculate both forces separately and add them together.

---

## Step 3 — Orbit Trails

Store previous positions:

```python
trail1 = [(int(x1), int(y1))]
trail2 = [(int(x2), int(y2))]
trail3 = [(int(x3), int(y3))]
```

Update trails:

```python
trail1.append((int(x1), int(y1)))
trail2.append((int(x2), int(y2)))
trail3.append((int(x3), int(y3)))
```

Draw trails:

```python
for pos in trail1:
    pygame.draw.circle(screen, (255, 215, 0), pos, 1)
```

---

## Step 4 — HUD

Create a font:

```python
default_font = pygame.font.SysFont(None, 24)
```

Display information:

```python
fps_text = default_font.render(
    f"FPS: {int(clock.get_fps())}",
    True,
    (255,255,255)
)
```

---

## Step 5 — Pause Functionality

Create a pause variable:

```python
paused = False
```

Toggle pause:

```python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_SPACE:
        paused = not paused
```

Skip updates when paused:

```python
if paused:
    continue
```

---

## Running

```bash
python3 script.py
```

---

## What You'll Learn

This project introduces:

- Newtonian mechanics
- Vectors
- Gravity simulation
- Numerical integration
- Real-time rendering
- Game loops
- Physics programming

---

## License

MIT License