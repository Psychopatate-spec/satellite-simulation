# Satellite Simulator

This is a simple satellite simulator built with `pygame-ce`.

## Installation

Use Python 3.14 or newer and install `pygame-ce` with pip:

```bash
pip install pygame-ce
```

## Running

Create a Python file such as `main.py` and run it:

```bash
python main.py
```

## Tutorial

1. Import `pygame` and initialize it.
2. Create a window and set the frame rate.
3. Define a satellite position and an orbit radius.
4. Update the satellite angle each frame and draw the orbit and satellite.
5. Handle the quit event.

### Example code

```python
import pygame
import math

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

angle = 0.0
orbit_center = (400, 300)
orbit_radius = 200
speed = 0.01

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    angle += speed
    x = orbit_center[0] + math.cos(angle) * orbit_radius
    y = orbit_center[1] + math.sin(angle) * orbit_radius

    screen.fill((0, 0, 20))
    pygame.draw.circle(screen, (50, 50, 100), orbit_center, orbit_radius, 1)
    pygame.draw.circle(screen, (255, 255, 0), orbit_center, 5)
    pygame.draw.circle(screen, (200, 200, 255), (int(x), int(y)), 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

## Notes

- `pygame-ce` is the current package for newer Python versions.
- `pygame` is no longer supported for Python 3.14 and newer.
- Adjust `speed`, `orbit_radius`, and colors to customize the simulation.
