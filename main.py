import pyxel
import random
from math import sqrt

COLOR = pyxel.COLOR_DARK_BLUE
STEP = 2
RADIUS = 5


class App:
    def __init__(self):

        pyxel.init(160, 120, title="Robson Correia")

        pyxel.sleep1 = False
        pyxel.sleep2 = False
        pyxel.sleep3 = False

        pyxel.x1 = random.uniform(20, 140)
        pyxel.x2 = random.uniform(20, 140)
        pyxel.x3 = random.uniform(20, 140)
        pyxel.y1 = random.uniform(20, 100)
        pyxel.y2 = random.uniform(20, 100)
        pyxel.y3 = random.uniform(20, 100)

        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def in_circle(arg, x, y, cx, cy):
        dist = sqrt((x - cx) ** 2 + (y - cy) ** 2)
        return dist <= RADIUS

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x1, pyxel.y1):
                pyxel.sleep1 = True
            if self.in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x2, pyxel.y2):
                pyxel.sleep2 = True
            if self.in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x3, pyxel.y3):
                pyxel.sleep3 = True

        if not pyxel.sleep1:
            pyxel.x1 = pyxel.x1 + random.uniform(-STEP, STEP)
            pyxel.y1 = pyxel.y1 + random.uniform(-STEP, STEP)

        if not pyxel.sleep2:
            pyxel.x2 = pyxel.x2 + random.uniform(-STEP, STEP)
            pyxel.y2 = pyxel.y2 + random.uniform(-STEP, STEP)

        if not pyxel.sleep3:
            pyxel.x3 = pyxel.x3 + random.uniform(-STEP, STEP)
            pyxel.y3 = pyxel.y3 + random.uniform(-STEP, STEP)

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        pyxel.circ(pyxel.x1, pyxel.y1, RADIUS, COLOR)
        pyxel.circ(pyxel.x2, pyxel.y2, RADIUS, COLOR)
        pyxel.circ(pyxel.x3, pyxel.y3, RADIUS, COLOR)


App()
