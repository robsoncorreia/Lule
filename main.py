import pyxel
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
CIRCLES = 20
TIME = 2 * CIRCLES
BORDER = 20


pyxel.game_over = False


class Circle:
    def __init__(self, x, y, id):
        self.isClicked = False
        self.x = x
        self.y = y
        self.id = id

    def mouse_clicked(self, mouse_x, mouse_y):
        if (not self.isClicked):
            dist = sqrt((mouse_x - self.x) ** 2 +
                        (mouse_y - self.y) ** 2)
            self.isClicked = dist <= RADIUS
        return self.isClicked


circles = []


class App:
    def __init__(self):

        self.score = 0

        self.gameOver = False

        pyxel.init(WIDTH, HEIGTH, TITLE)
        pyxel.load("main.py.pyxres")

        for id in range(CIRCLES):
            circles.append(
                Circle(pyxel.rndi(BORDER, WIDTH - BORDER), pyxel.rndi(BORDER, HEIGTH - BORDER), id))

        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def reset(args):
        for circle in circles:
            circle.isClicked = False

    def you_win(args):
        for circle in circles:
            if (not circle.isClicked):
                return False
        return True

    def update(self):
        if pyxel.btnp(pyxel.KEY_R):
            self.reset()

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.frame_count > 30 * TIME:
            self.gameOver = True

        if self.gameOver:
            return

        if self.you_win():
            return

        for circle in circles:
            if not circle.isClicked:
                if not circle.x > WIDTH - BORDER:
                    circle.x += pyxel.rndi(-STEP, STEP)
                else:
                    circle.x = WIDTH - BORDER

                if not circle.x < BORDER:
                    circle.x += pyxel.rndi(-STEP, STEP)
                else:
                    circle.x = BORDER

                if not circle.y > HEIGTH - BORDER:
                    circle.y += pyxel.rndi(-STEP, STEP)
                else:
                    circle.y = HEIGTH - BORDER

                if not circle.y < BORDER:
                    circle.y += pyxel.rndi(-STEP, STEP)
                else:
                    circle.y = BORDER

        self.score = sum(1 for c in circles if c.isClicked == True)

    def draw_circle(self):
        for circle in circles:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                circle.mouse_clicked(pyxel.mouse_x, pyxel.mouse_y)

            pyxel.blt(circle.x, circle.y, 1,
                      0 if not circle.isClicked else 16,
                      0 if not circle.isClicked else 32, 8, 8)

    def draw(self):

        pyxel.cls(pyxel.COLOR_BLACK)

        self.draw_circle()

        if not self.gameOver:
            pyxel.text(
                0, 6, f'Time: {pyxel.frame_count % 16}', pyxel.frame_count % 16)
            pyxel.text(
                0, 0, f'Score: {self.score}', pyxel.frame_count % 16)

        if self.you_win():
            x = (WIDTH // 2) - (len(YOU_WIN) // 2) * pyxel.FONT_WIDTH
            y = (HEIGTH // 2) - pyxel.FONT_HEIGHT
            pyxel.text(x, y, YOU_WIN, pyxel.frame_count % 16)
            return

        if self.gameOver:
            x = (WIDTH // 2) - (len(GAME_OVER) // 2) * pyxel.FONT_WIDTH
            y = (HEIGTH // 2) - pyxel.FONT_HEIGHT
            pyxel.text(x, y, GAME_OVER, pyxel.frame_count % 16)
            return


App()
