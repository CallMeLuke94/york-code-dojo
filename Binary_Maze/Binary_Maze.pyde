from random import randint

def setup():
    size(700, 700)
    frameRate(0.5)

def draw():
    c = color(randint(0, 255), randint(0, 255), randint(0, 255))
    noLoop()
    background(c)
    strokeWeight(random(1, 3))
    stroke(255)

    cell = randint(2, 30)

    for i in range((width) / cell):
        for j in range((height) / cell):
            drawn = False
            if j == 0:
                line(i * cell, j * cell, (i + 1) * cell, j * cell)  # top line
                drawn = True
            if i == (width) / cell - 1:
                # right line
                line((i + 1) * cell, j * cell, (i + 1) * cell, (j + 1) * cell)
                drawn = True
            if not drawn:
                wall = randint(0, 1)
                if wall == 0:
                    line(i * cell, j * cell, (i + 1) * cell, j * cell)
                else:
                    line(
                        (i + 1) * cell, j * cell, (i + 1) * cell, (j + 1) * cell)

def keyPressed():
    print("Image Saved")

def mouseClicked():
    redraw()
