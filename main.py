import pyxel
import random
from math import sqrt

COLOR_ACTIVE = pyxel.COLOR_GREEN
COLOR_SLEEP = pyxel.COLOR_RED
STEP = 2
RADIUS = 5
WIDTH = 160
HEIGTH = 120
TITLE = "Robson Correia"
GAME_OVER = "GAME OVER!"
YOU_WIN = "YOU WIN!"

pyxel.game_over = False

class App:
    def __init__(self):

        pyxel.init(WIDTH, HEIGTH, TITLE)

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

    def you_win(arg, x1, x2, x3):
        return x1 == x2 == x3 == True

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.frame_count > 30 * 5:
            pyxel.game_over = True

        if pyxel.game_over:
            return

        if self.you_win(pyxel.sleep1, pyxel.sleep2, pyxel.sleep3):
            return

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

        pyxel.circ(pyxel.x1, pyxel.y1, RADIUS,
                   COLOR_SLEEP if pyxel.sleep1 else COLOR_ACTIVE)
        pyxel.circ(pyxel.x2, pyxel.y2, RADIUS,
                   COLOR_SLEEP if pyxel.sleep2 else COLOR_ACTIVE)
        pyxel.circ(pyxel.x3, pyxel.y3, RADIUS,
                   COLOR_SLEEP if pyxel.sleep3 else COLOR_ACTIVE)

        if self.you_win(pyxel.sleep1, pyxel.sleep2, pyxel.sleep3):
            x = (WIDTH // 2) - (len(YOU_WIN) // 2) * pyxel.FONT_WIDTH
            y = (HEIGTH // 2) - pyxel.FONT_HEIGHT
            pyxel.text(x, y, YOU_WIN, pyxel.frame_count % 16)
            return

        if pyxel.game_over:
            x = (WIDTH // 2) - (len(GAME_OVER) // 2) * pyxel.FONT_WIDTH
            y = (HEIGTH // 2) - pyxel.FONT_HEIGHT
            pyxel.text(x, y, GAME_OVER, pyxel.frame_count % 16)
            return

App()
