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
                #   #   #   #
    # "Maze": [[0,0,0,0,0,1,0,0,0],
    #          [0,0,1,0,0,0,0,0,0],  #Row for walls
    #          [0,0,0,0,0,0,0,0,0],
    #          [0,0,0,0,0,0,0,0,1],  #Row for walls
    #          [0,1,0,0,0,0,0,0,0],
    #          [0,0,0,0,1,0,0,0,0],  #Row for walls
    #          [0,0,0,0,0,0,0,0,0],
    #          [0,0,1,0,0,0,0,0,1],  #Row for walls
    #          [0,0,0,0,0,1,0,0,2]
    #          ],
    "Maze": [[(Cell.N | Cell.W | Cell.BALL),    (Cell.N | Cell.S),  (Cell.N, Cell.E),   (Cell.N, Cell.W),   (Cell.N, Cell.E)],
             [(Cell.W),                         (Cell.N),           0,                  0,                  (Cell.S | Cell.E)],
             [(Cell.W | Cell.E),                (Cell.W),           (Cell.S),           0,                  (Cell.N | Cell.E)],
             [(Cell.W),                         (Cell.S),           (Cell.N),           0,                  (Cell.S, Cell.E)],
             [(Cell.W | Cell.S),                (Cell.N | Cell.S),  (Cell.S | Cell.E),  (Cell.S | Cell.W),  (Cell.N | Cell.S | Cell.E | Cell.BIT)]
             ],
    "num_row": 5,
    "num_col": 5
}

@app.route("/Test")
def hello():
    print("Hello!")
    return jsonify(temp_level_data)