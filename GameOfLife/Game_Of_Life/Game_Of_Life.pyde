import random

process = False

cellSize = 8  # runs slowly at smaller numbers

cells = []

def setup():
    frameRate(20)
    size(800, 700)
    background(100)
    stroke(255)

    for i in range(width / cellSize):
        cells.append([])
        for j in range(height / cellSize):
            cells[i].append({'x': i, 'y': j, 'live': random.choice([True, False]), 'newStatus': False})   # change False to random.choice([True, False]) for random seeding

    noStroke()
    #stroke(255, 0, 0)
    for row in cells:
        for cell in row:
            if cell['live'] == False:
                fill(0)
            else:
                fill(255)
            rect(cell['x'] * cellSize, cell['y'] * cellSize, cellSize, cellSize)


def draw():
    if process:
        rules()
    noStroke()
    #stroke(255, 0, 0)
    for row in cells:
        for cell in row:
            if cell['live'] == False:
                fill(0)
            else:
                fill(255)
            rect(cell['x'] * cellSize, cell['y'] * cellSize, cellSize, cellSize)


def rules():
    for row in cells:
        for cell in row:
            count = 0
            fromx = cell['x'] - 1
            tox = cell['x'] + 1
            fromy = cell['y'] - 1
            toy = cell['y'] + 1
            if cell['x'] == 0:
                fromx = 0
            if cell['y'] == 0:
                fromy = 0
            if cell['x'] >= (int(width / cellSize - 1)):
                tox = cell['x']
            if cell['y'] >= (int(height / cellSize - 1)):
                toy = cell['y']

            for i in range(fromx, tox + 1):
                for j in range(fromy, toy + 1):
                    if (cell['x'] == i and cell['y'] == j):
                        continue
                    if cells[i][j]['live']:
                        count += 1

            cell['newStatus'] = False
            if cell['live'] == True:
                if count < 2:
                    cell['newStatus'] = False
                elif count > 3:
                    cell['newStatus'] = False
                else:
                    cell['newStatus'] = True
            elif count == 3:
                cell['newStatus'] = True

    for row in cells:
        for cell in row:
            cell['live'] = cell['newStatus']


def mousePressed():
    x = int(mouseX / cellSize)
    y = int(mouseY / cellSize)
    cells[x][y]['live'] = not cells[x][y]['live']
    fill(255)
    rect(x * cellSize, y
                 * cellSize, cellSize, cellSize)

def keyPressed():
    global process
    process = not process
