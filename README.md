# ☀️ Build Your Own Solar System with Pygame

Today I'll be teaching you how to build your own solar system using **Pygame Community Edition (pygame-ce)**.

This project demonstrates how to simulate gravity using **Newton's Law of Universal Gravitation** (sounds scary but it'll be find trust me) and create realistic-looking planetary motion.

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

- Python 3.14.5
- pygame-ce

So, because I'm using Python 3.14.5 and that Pygame isn't supported anymore, we'll use Pygame-ce, which stands for Pygame Community Edition. It does the same thing so dw. To install it, open your terminal and type this command:

```bash
pip install pygame-ce
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

First, we import pygame (and not pygame-ce), then we initialize it. We'll need a screen by 800 x 800 pixels. Then, we create a loop that checks if we quit the window, which will kill pygame. Finally, we fill the screen with a pitch black color, because, well, space is black. 

---

## Physics

Here comes the physics part of the simulation.
The core of our simulation is Newton's Law of Universal Gravitation:

```python
F = G * (M1 * M2) / R²
```

Where:

- F is the gravitational force
- G is the gravitational constant
- M1 and M2 are the masses
- R is the distance between them

Using Newton's Second Law:

```python
a = F / m
```

We can compute acceleration.

We then update velocity and position:

```python
v = v + a * dt
x = x + v * dt
```

Now that we understand the physics that make our planets move, we can move on to actually creating those planets.

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
F = G * (M1 * M2) / R ** 2
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

Split force into components (x and y axis, with the top-left of the screen being the origin):

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

And boom, you got 2 planets going around a sun. Cool no ?
You've now technically finished the tutorial, and the following steps are just extras that will make the project prettier. We'll be adding an orbit trail to our planets, and text that shows the velocity of our planets, their distance from the sun, and the FPS. 

---

## Step 3 — Orbit Trails

We will store the position of our planets (yes even the sun has a trajoctory, but because it's so massive, we don't get to actually notice it.) and then draw a point for each position our planets went to.

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

Boom, got a trajectory.

---

## Step 4 — HUD

First, we need a font.

```python
default_font = pygame.font.SysFont(None, 24)
```

Then, we will display our useful infos such as distance, velocity, and FPS.

```python
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
```

---

## Step 5 — Pause Functionality

To pause our simulation, we'll first need a variable "paused" :

```python
paused = False
```

To toggle pause, we'll check inside the while loop if the space bar is being pressed. If so, we change the "paused" variable:

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

Let's test this ! Inside of your terminal, change directory into your project's folder using the cd and ls commands to navigate your way through, and run this command:

```bash
python3 script.py
```

You should see a black screen with planets moving around. Cool no ? Feel free to mess around with the values of masses, initial velocity, or even the G constant, and see what happens !
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