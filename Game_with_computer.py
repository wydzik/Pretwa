from Game import State

class Game_with_computer():
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

        self.interaction = [] #tablica dwuelementowa, 1 element- wybrany pion na planszy, 2 obiekt- puste pole

        self.board_state = {  #stan pola na planszy: 3 mozliwosci (RED, GREEN, EMPTY)
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

        self.red_turn = True
        self.go_deeper = True
        self.red_wins = False
        self.green_wins = False

        self.can_move_to = {
            1: [2, 6, 7],
            2: [1, 3, 8],
            3: [2, 4, 9],
            4: [3, 5, 10],
            5: [4, 6, 11],
            6: [1, 5, 12],
            7: [1, 12, 8, 13],
            8: [2, 7, 9, 14],
            9: [3, 8, 10, 15],
            10: [4, 9, 11, 16],
            11: [5, 10, 12, 17],
            12: [6, 11, 7, 18],
            13: [7, 18, 14, 19],
            14: [8, 13, 15, 19],
            15: [9, 14, 16, 19],
            16: [10, 15, 17, 19],
            17: [11, 16, 18, 19],
            18: [12, 17, 13, 19],
            19: [13, 14, 15, 16, 17, 18]}

        self.can_hit = {
            1: [5, 3, 13],
            2: [6, 4, 14],
            3: [1, 5, 15],
            4: [2, 6, 16],
            5: [3, 1, 17],
            6: [4, 2, 18],
            7: [11, 9, 19],
            8: [12, 10, 19],
            9: [7, 11, 19],
            10: [8, 12, 19],
            11: [9, 7, 19],
            12: [10, 8, 19],
            13: [17, 15, 1, 16],
            14: [18, 16, 2, 17],
            15: [13, 17, 3, 18],
            16: [14, 18, 4, 13],
            17: [15, 13, 5, 14],
            18: [16, 14, 6, 15],
            19: [7, 8, 9, 10, 11, 12]
        }

    def has_common(self, a, b):
        for x in a:
            for y in b:
                if x == y:
                    return x
        return False

    def check_if_clickable(self, mouse_pos):  # zwraca nr pola, ktore kliknal user
        for i in range(1, 20, 1):
            x_min = self.coordinates[i][0]
            x_max = self.coordinates[i][0]+50
            y_min = self.coordinates[i][1]
            y_max = self.coordinates[i][1]+50
            # print(x_min,x_max,y_min,y_max)
            # print(mouse_pos)
            if (mouse_pos[0] >= x_min) \
                    and (mouse_pos[0] <= x_max) \
                    and (mouse_pos[1] >= y_min) \
                    and (mouse_pos[1] <= y_max):
                return i

    def check_pawn_hits(self, my_state, opponent_state, my_position):
        """Sprawdza czy konkretny pionek może wykonać bicie"""
        for y in self.can_hit[my_position]:

            if self.board_state[y] == State.EMPTY:

                next_step = y
                position = my_position
                hit = self.has_common(self.can_move_to[position], self.can_move_to[next_step])
                if self.board_state[hit] == opponent_state:
                    return True
        return False

    def check_any_hits(self, my_state, opponent_state):
        """Sprawdza, czy gracz może wykonać jakiekolwiek bicie w tym ruchu"""
        for x in self.board_state:

            if self.board_state[x] == my_state:

                for y in self.can_hit[x]:

                    if self.board_state[y] == State.EMPTY:

                        next_step = y
                        position = x
                        hit = self.has_common(self.can_move_to[position], self.can_move_to[next_step])

                        if self.board_state[hit] == opponent_state:
                            return True
        return False

    def return_hits_list(self, my_state, opponent_state):
        list_full=[]
        """Sprawdza, czy gracz może wykonać jakiekolwiek bicie w tym ruchu"""
        for x in self.board_state:

            if self.board_state[x] == my_state:

                for y in self.can_hit[x]:

                    if self.board_state[y] == State.EMPTY:

                        next_step = y
                        position = x
                        hit = self.has_common(self.can_move_to[position], self.can_move_to[next_step])

                        if self.board_state[hit] == opponent_state:
                            list = [position,hit,y] #z position mozna zbic pionek na pozycji hit i przejsc na pozycje y
                            print(position)
                            list_full.append(list)
        return list_full

    def add_to_interaction(self, pos):

        if self.red_turn:

            if (len(self.interaction)) == 0 and self.board_state[pos] == State.RED: # pierwsze klikniete pole przez usera nie moze byc puste

                self.interaction.append(pos)

            elif (len(self.interaction)) == 1 and self.board_state[pos] != State.EMPTY:  # próba ruchu na zajęte miejsce

                self.interaction.clear()

            elif (len(self.interaction)) == 1 and self.board_state[pos] == State.EMPTY:  # prawidłowy ruch

                self.interaction.append(pos)
                if self.check_any_hits(State.RED, State.GREEN):

                    if self.interaction[1] in self.can_move_to[self.interaction[0]]:  # ruch bez bicia

                        self.interaction.clear()

                    elif (self.interaction[1] not in self.can_move_to[self.interaction[0]])\
                            and ((self.interaction[1] in self.can_hit[self.interaction[0]])
                                 and (self.board_state[self.has_common(self.can_move_to[self.interaction[0]],
                                                                       self.can_move_to[self.interaction[1]])] == State.GREEN)):

                        x = self.has_common(self.can_move_to[self.interaction[0]], self.can_move_to[self.interaction[1]])
                        self.board_state[x] = State.EMPTY
                        self.board_state[self.interaction[1]] = self.board_state[self.interaction[0]]
                        self.board_state[self.interaction[0]] = State.EMPTY
                        if self.check_pawn_hits(State.RED,State.GREEN,self.interaction[1]):
                            self.interaction.clear()
                        else:
                            self.red_turn = False
                            self.interaction.clear()
                            print("Green turn")
                    else:
                        self.interaction.clear()
                else:
                    if self.interaction[1] in self.can_move_to[self.interaction[0]]:  # ruch bez bicia

                        self.board_state[self.interaction[1]] = self.board_state[self.interaction[0]]
                        self.board_state[self.interaction[0]] = State.EMPTY
                        self.red_turn = False
                        self.interaction.clear()
                        print("Green turn")

                    elif (self.interaction[1] not in self.can_move_to[self.interaction[0]]) \
                            and ((self.interaction[1] in self.can_hit[self.interaction[0]])
                                 and (self.board_state[self.has_common(self.can_move_to[self.interaction[0]],
                                                                       self.can_move_to[
                                                                           self.interaction[1]])] == State.GREEN)):

                        x = self.has_common(self.can_move_to[self.interaction[0]],
                                            self.can_move_to[self.interaction[1]])
                        self.board_state[x] = State.EMPTY
                        self.board_state[self.interaction[1]] = self.board_state[self.interaction[0]]
                        self.board_state[self.interaction[0]] = State.EMPTY
                        self.computer_move()

                        if self.check_pawn_hits(State.RED, State.GREEN, self.interaction[1]):
                            self.interaction.clear()
                        else:
                            self.red_turn = False
                            print("Green turn")
                    else:
                        self.interaction.clear()
                counter=0
                for x in self.board_state:
                    if self.board_state[x] == State.GREEN:
                        counter += 1
                if counter <= 3:
                    self.red_wins = True

        elif not self.red_turn: #computer - green
            self.computer_move()
            counter = 0
            for x in self.board_state:
                if self.board_state[x] == State.RED:
                    counter += 1
            if counter <= 3:
                self.green_wins = True

    def computer_move(self):
        computer_pawns=[]
        for i in range(1, 20, 1):
            if (self.board_state[i]) == State.GREEN:
                computer_pawns.append(i)
        if self.check_any_hits(State.GREEN, State.RED):
            reds_to_hit=self.return_hits_list(State.GREEN,State.RED)
            print(reds_to_hit)
            self.board_state[reds_to_hit[0][0]]=State.EMPTY
            self.board_state[reds_to_hit[0][1]]=State.EMPTY
            self.board_state[reds_to_hit[0][2]]=State.GREEN
            self.red_turn=True
        else:
            list_of_possible_moves=[]
            for x in computer_pawns:
                list_of_pos=self.can_move_to[x]
                for i in list_of_pos:
                    if self.board_state[i]==State.EMPTY:
                        start_end=[x,i]
                        list_of_possible_moves.append(start_end)
            self.board_state[list_of_possible_moves[0][0]]=State.EMPTY
            self.board_state[list_of_possible_moves[0][1]]=State.GREEN
            self.red_turn=True


















