from main import app
from flask import jsonify
from enum import IntFlag

class Cell(IntFlag):
    N    = 1
    E    = 2
    S    = 4
    W    = 8
    BALL = 16
    BIT = 32

temp_level_data = {
    "Level": 1,
    "Unlocked": True,
    "Maze": [[(Cell.BALL),  (Cell.S),  (Cell.E),    (Cell.W),   0],
             [0,            (Cell.N),   0,          0,          (Cell.S)],
             [(Cell.E),     (Cell.W),   (Cell.S),   0,          (Cell.N)],
             [0,            (Cell.S),   (Cell.N),   0,          (Cell.S)],
             [0,            (Cell.N),   (Cell.E),   (Cell.W),   (Cell.N | Cell.BIT)]
             ],
    "num_row": 5,
    "num_col": 5
}

@app.route("/Test")
def hello():
    print("Hello!")
    return jsonify(temp_level_data)