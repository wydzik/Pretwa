




class Minmax():
    def __init__(self, level, board_state, hit_list, move_list,parent):
        self.level = level
        self.board_state = board_state
        self.hit_list = hit_list
        self.move_list = move_list
        self.parent = parent


    def remove_hit_from_list(self):
        self.hit_list.remove(self.hit_list[0])

    def remove_move_from_list(self):
        self.move_list.remove(self.move_list[0])
