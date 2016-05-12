from random import randint

class Cell:

    def __init__(self):
        self.top = True
        self.right = True
        self.visited = False
        self.depth = 0


def setup():
    size(700, 700)

def draw():
    scl = randint(6, 30)
    noLoop()
    background(0)
    stroke(255)
    cellCount = 0
    cells = []
    for i in range((width) / scl):
        column = []
        for j in range((height) / scl):
            column.append(Cell())
            cellCount += 1
        cells.append(column)
    X = randint(0, width / scl)
    Y = randint(0, height / scl)
    firstX = X
    firstY = Y
    cells[X][Y].visited = True
    cells[X][Y].depth = 1
    cellCount -= 1
    while cellCount > 0:
        dir = randint(1, 4)
        if (Y == 0 and dir == 1) or (X == 0 and dir == 4) or (Y == height / scl - 1 and dir == 3) or (X == width / scl - 1 and dir == 2):
            continue
        nextX = X
        nextY = Y
        if dir == 1:
            nextY = Y - 1
        elif dir == 2:
            nextX = X + 1
        elif dir == 3:
            nextY = Y + 1
        elif dir == 4:
            nextX = X - 1

        thisCell = cells[X][Y]
        nextCell = cells[nextX][nextY]
        if nextCell.visited == False:
            cells[nextX][nextY].visited = True
            cellCount -= 1
            if dir == 1:
                cells[X][Y].top = False
            elif dir == 2:
                cells[X][Y].right = False
            elif dir == 3:
                cells[nextX][nextY].top = False
            elif dir == 4:
                cells[nextX][nextY].right = False

        X = nextX
        Y = nextY

    queue = [(firstX, firstY)]
    while queue:
        X, Y = queue[0]
        queue = queue[1:]
        cell = cells[X][Y]
        if (not cell.top) and Y > 0 and cells[X][Y - 1].depth == 0:
            cells[X][Y - 1].depth = cell.depth + 1
            queue.append((X, Y - 1))
        if (not cell.right) and X < width / scl - 1 and cells[X + 1][Y].depth == 0:
            cells[X + 1][Y].depth = cell.depth + 1
            queue.append((X + 1, Y))
        if Y < height / scl - 1 and (not cells[X][Y + 1].top) and cells[X][Y + 1].depth == 0:
            cells[X][Y + 1].depth = cell.depth + 1
            queue.append((X, Y + 1))
        if X > 0 and (not cells[X - 1][Y].right) and cells[X - 1][Y].depth == 0:
            cells[X - 1][Y].depth = cell.depth + 1
            queue.append((X - 1, Y))

    depths = []
    for i in range((width) / scl):
        for j in range((height) / scl):
            depths.append(cells[i][j].depth)

    maxDepth = max(depths)
    newColour = randint(0, 360)

    for i in range((width) / scl):
        for j in range((height) / scl):
            colorMode(HSB, 360, 100, 300)
            noStroke()
            fill(newColour, 100, 300 - 300 * cells[i][j].depth / maxDepth)
            rect(i * scl + 1, j * scl + 1, scl, scl)
            colorMode(RGB)
            stroke(255)
            if cells[i][j].top:
                line(i * scl, j * scl, (i + 1) * scl, j * scl)
            if cells[i][j].right:
                line((i + 1) * scl, j * scl, (i + 1) * scl, (j + 1) * scl)

def keyPressed():
    save("MazeImage.png")
    print("Image Saved!")


def mouseClicked():
    redraw()
