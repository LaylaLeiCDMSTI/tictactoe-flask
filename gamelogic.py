background = ""
players = ["x", "o"]
cells = [
    [background, background, background], 
    [background, background, background], 
    [background, background, background]
]
turn = False

def cellChange(turn, button_pressed):
    index = [(int)(button_pressed[0]), (int)(button_pressed[1])]
    if(turn):
        cells[index[0]][index[1]] = players[1]
    else:
        cells[index[0]][index[1]] = players[0]

def turnChange():
    global turn
    if turn:
        turn = False
    else:
        turn = True

def checkCells():
    for player in players:
        for x in cells:
            if x[0] == player and x[1] == player and x[2] == player:
                return player + ".True"
        for x in range(len(cells)):
            if cells[0][x] == player and cells[1][x] == player and cells[2][x] == player:
                return player + ".True"

        if cells[0][0] == player and cells[1][1] == player and cells[2][2] == player:
            return player + ".True"
        elif cells[2][0] == player and cells[1][1] == player and cells[0][2] == player:
            return player + ".True"
    
    rowCheck = 0
    for x in cells:
        if x[0] != background and x[1] != background and x[2] != background:
            rowCheck += 1
        else:
            return "false"
    if(rowCheck >= 3):
        return "tie.True"
def start():
    global cells
    cells = [
        [background, background, background], 
        [background, background, background], 
        [background, background, background]
    ]
    global turn
    turn = False