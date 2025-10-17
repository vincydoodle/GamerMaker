from pygame import *
import math

class SoftBody:
    def __init__(self, x, y, radius=50, points=12, stiffness=0.1, damping=0.9):
        self.center = [x, y]
        self.radius = radius
        self.damping = damping
        self.points = []
        angle_step = math.tau / points

        for i in range(points):
            angle = i * angle_step
            px = x + math.cos(angle) * radius
            py = y + math.sin(angle) * radius
            self.points.append({
                "pos": [px, py],
                "vel": [0, 0],
                "angle": angle
            })
        self.stiffness = stiffness

    def update(self):
        cx, cy = self.center
        for p in self.points:
            # spring toward circular rest position
            target_x = cx + math.cos(p["angle"]) * self.radius
            target_y = cy + math.sin(p["angle"]) * self.radius
            dx = target_x - p["pos"][0]
            dy = target_y - p["pos"][1]

            p["vel"][0] += dx * self.stiffness
            p["vel"][1] += dy * self.stiffness

            # damping makes it less chaotic
            p["vel"][0] *= self.damping
            p["vel"][1] *= self.damping

            p["pos"][0] += p["vel"][0]
            p["pos"][1] += p["vel"][1]

    def draw(self, surface):
        for i, p in enumerate(self.points):
            next_p = self.points[(i + 1) % len(self.points)]
            draw.line(surface, (200, 200, 255), p["pos"], next_p["pos"], 2)
        draw.circle(surface, (255, 100, 100), self.center, 3)
