from enum import Enum

class State(Enum):
    RED='red'
    GREEN='green'
    EMPTY='empty'

class Game():
    def __init__(self):

        self.coordinates = {    #pola na planszy ponumerowane od 1 do 19
            1: (275, -25),
            2: (530, 125),
            3: (530, 425),
            4: (275, 575),
            5: (20, 425),
            6: (20, 125),
            7: (275, 75),
            8: (445, 175),
            9: (445, 375),
            10: (275, 475),
            11: (105, 375),
            12: (105, 175),
            13: (275, 175),
            14: (355, 225),
            15: (355, 325),
            16: (275, 375),
            17: (190, 325),
            18: (190, 225),
            19: (275, 275)}


        self.board_state={  #stan pola na planszy: 3 mozliwosci (RED, GREEN, EMPTY)
            1: State.RED,
            2: State.RED,
            3: State.RED,
            4: State.GREEN,
            5: State.GREEN,
            6: State.GREEN,
            7: State.RED,
            8: State.RED,
            9: State.RED,
            10: State.GREEN,
            11: State.GREEN,
            12: State.GREEN,
            13: State.RED,
            14: State.RED,
            15: State.RED,
            16: State.GREEN,
            17: State.GREEN,
            18: State.GREEN,
            19: State.EMPTY}

    def check_if_clickable(self,mouse_pos): #zwraca nr pola, ktore kliknal user
        for i in range(1,20,1):
            x_min=self.coordinates[i][0]
            x_max=self.coordinates[i][0]+50
            y_min=self.coordinates[i][1]
            y_max=self.coordinates[i][1]+50
            # print(x_min,x_max,y_min,y_max)
            # print(mouse_pos)
            if (mouse_pos[0]>=x_min) and (mouse_pos[0]<=x_max) and (mouse_pos[1]>=y_min) and (mouse_pos[1]<=y_max):
                return i













