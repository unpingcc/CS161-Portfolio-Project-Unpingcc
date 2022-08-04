# Name: Cassidy Unpingco
# Date: 6/4/2021
# Description: built a class called OrthokonBoard. The class initializes the game and controls the validity of movement
# and includes methods to flip pieces, update game status

class OrthokonBoard:
    """
    a board game that has 2 players playing on a 4x4 grid
    the class does not do everything needed to play the game.
    The class is only responsible for handling the rules concerning
    the board game.
    """

    def __init__(self):
        """
        initialize game rules
        """
        self._empty_board = [["", "", "", ""],
                           ["", "", "", ""],
                           ["", "", "", ""],
                           ["", "", "", ""]]
        self._current_state = "UNFINISHED"
        self._board_rep = [["R", "R", "R", "R"],
                           ["", "", "", ""],
                           ["", "", "", ""],
                           ["Y", "Y", "Y", "Y"]]

    def get_current_state(self):
        """
        returns current state of the game either "RED_WON", "YELLOW_WON", OR "UNFINISHED"
        """
        return self._current_state

    def get_direction(self, row1, col1, row2, col2):
        """
        returns direction of move to help verify it is allowed
        """
        # DOWN
        if col1 == col2 and row1 < row2:
            return "D"
        # UP
        if col1 == col2 and row1 > row2:
            return "U"
        # LEFT
        if row1 == row2 and col1 > col2:
            return "L"
        # RIGHT
        if row1 == row2 and col1 < col2:
            return "R"

        if abs(row2 - row1) == abs(col2 - col1):  # isDiagnol
            if row2 > row1 and col2 > col1:
                return "DR"
            elif row2 > row1 and col2 < col1:
                return "DL"
            elif row2 < row1 and col2 < col1:
                return "UL"
            elif row2 < row1 and col2 > col1:
                return "UR"

        return "INVALID"

    def direction_valid(self, direction):
        """
        returns direction
        """
        if direction == "INVALID":
            return False
        return True

    def make_move(self, row1, col1, row2, col2):
        """
        make move method should take four parameters
        """
        ch = self._board_rep[row1][col1]
        # If the game has already been won, or if the move is not valid, make_move should just return False.
        if self.get_current_state() != "UNFINISHED":
            return False
        elif row2 > 3 or col2 > 3 or row2 < 0 or col2 < 0:  # trying to move outside of edges
            return False
        elif self._board_rep[row2][col2] != "":
            return False
        else:
            # Otherwise, it should record the move, update the board and the current state, and return True.
            # To update the current state, you need to detect if this move causes a win for either player.
            # What direction is the move?
            # UP | DOWN | LEFT | RIGHT | UP_RIGHT | UP_LEFT | DOWN_RIGHT | DOWN_LEFT
            direction = self.get_direction(row1, col1, row2, col2)
            if not self.direction_valid(direction):
                return False
            self.attempt_record_move(row1, col1, direction)
            self.update_state(ch)
            return True

    def update_state(self, ch):
        """
        checks if there's a win and updates current state of the game either
        "RED_WON", "YELLOW_WON", OR leaves value set to "UNFINISHED"
        """
        # if no more red pieces then YELLOW_WON
        hasRedPieces = False
        for i in range(0, 4):
            for j in range(0, 4):
                if self._board_rep[i][j] == "R":
                    hasRedPieces = True
        if not hasRedPieces:
            self._current_state = "YELLOW_WON"

        # if no more yellow pieces then RED_WON
        hasYellowPieces = False
        for i in range(0, 4):
            for j in range(0, 4):
                if self._board_rep[i][j] == "Y":
                    hasYellowPieces = True
        if not hasYellowPieces:
            self._current_state = "RED_WON"

        # if red has no more moves possible then YELLOW_WON
        # this means that every potential move for R is blocked (he/she is surrounded by other pieces)
        if ch == "Y" and not self.has_a_move("R"):
            self._current_state = "YELLOW_WON"

        # if yellow has no more moves possible then RED_WON
        # this means that every potential move for Y is blocked (he/she is surrounded by other pieces)
        if ch == "R" and not self.has_a_move("Y"):
            self._current_state = "RED_WON"

    def has_a_move(self, ch):
        """
        check if opponent has any remaining moves
        """
        hasMove = False
        for row1 in range(0, 4):
            for col1 in range(0, 4):
                if self._board_rep[row1][col1] == ch:
                    # UP
                    new_row = row1 - 1
                    new_col = col1
                    if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][
                        new_col] == "":
                        hasMove = True
                    # DOWN
                    new_row = row1 + 1
                    new_col = col1
                    if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][
                        new_col] == "":
                        hasMove = True
                    # RIGHT
                    new_row = row1
                    new_col = col1 + 1
                    if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][
                        new_col] == "":
                        hasMove = True
                    # LEFT
                    new_row = row1
                    new_col = col1 - 1
                    if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][
                        new_col] == "":
                        hasMove = True
                    # UP_RIGHT
                    new_row = row1 - 1
                    new_col = col1 + 1
                    if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][
                        new_col] == "":
                        hasMove = True
                    # UP_LEFT
                    new_row = row1 - 1
                    new_col = col1 - 1
                    if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][
                        new_col] == "":
                        hasMove = True
                    # DOWN_RIGHT
                    new_row = row1 + 1
                    new_col = col1 + 1
                    if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][
                        new_col] == "":
                        hasMove = True
                    # DOWN_LEFT
                    new_row = row1 + 1
                    new_col = col1 - 1
                    if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][
                        new_col] == "":
                        hasMove = True
        return hasMove

    # attemps to move in direction until hits an obstacle
    # once hit an obstacle, record move of piece
    # update adjacent tiles if needed
    def attempt_record_move(self, row1, col1, direction):
        """
        attempt_record_move tries to make and record the move
        """
        ch = self._board_rep[row1][col1]
        self._board_rep[row1][col1] = ""
        # moving up
        if direction == "U":
            row1 = row1 - 1
            while self.is_inbounds(col1):
                if self.is_collision(row1 - 1, col1):
                    self._board_rep[row1][col1] = ch
                    if self.is_inbounds(row1 - 1):
                        self._board_rep[row1 - 1][col1] = ch
                    self.update_board(row1, col1, ch)
                    return True
                row1 = row1 - 1
        elif direction == "D":
            row1 = row1 + 1
            while self.is_inbounds(col1):
                if self.is_collision(row1 + 1, col1):
                    self._board_rep[row1][col1] = ch
                    if self.is_inbounds(row1 + 1):
                        self._board_rep[row1 + 1][col1] = ch
                    self.update_board(row1, col1, ch)
                    return True
                row1 = row1 + 1
        elif direction == "R":
            col1 = col1 + 1
            while self.is_inbounds(col1):
                if self.is_collision(row1, col1 + 1):
                    self._board_rep[row1][col1] = ch
                    if self.is_inbounds(col1 + 1):
                        self._board_rep[row1][col1 + 1] = ch
                    self.update_board(row1, col1, ch)
                    return True
                col1 = col1 + 1
        elif direction == "L":
            col1 = col1 - 1
            while self.is_inbounds(col1):
                if self.is_collision(row1, col1 - 1):
                    self._board_rep[row1][col1] = ch
                    if self.is_inbounds(col1 - 1):
                        self._board_rep[row1][col1 - 1] = ch
                    self.update_board(row1, col1, ch)
                    return True
                col1 = col1 - 1
        elif direction == "UR":
            row1 = row1 - 1
            col1 = col1 + 1
            while self.is_inbounds(col1):
                if self.is_collision(row1 - 1, col1 + 1):
                    self._board_rep[row1][col1] = ch
                    if self.is_inbounds(row1 - 1) and self.is_inbounds(col1 + 1):
                        self._board_rep[row1 - 1][col1 + 1] = ch
                    self.update_board(row1, col1, ch)
                    return True
                row1 = row1 - 1
                col1 = col1 + 1
        elif direction == "DR":
            row1 = row1 + 1
            col1 = col1 + 1
            while self.is_inbounds(col1):
                if self.is_collision(row1 + 1, col1 + 1):
                    self._board_rep[row1][col1] = ch
                    if self.is_inbounds(row1 + 1) and self.is_inbounds(col1 + 1):
                        self._board_rep[row1 + 1][col1 + 1] = ch
                    self.update_board(row1, col1, ch)
                    return True
                row1 = row1 + 1
                col1 = col1 + 1
        elif direction == "UL":
            row1 = row1 - 1
            col1 = col1 - 1
            while self.is_inbounds(col1):
                if self.is_collision(row1 - 1, col1 - 1):
                    self._board_rep[row1][col1] = ch
                    if self.is_inbounds(row1 - 1) and self.is_inbounds(col1 - 1):
                        self._board_rep[row1 - 1][col1 - 1] = ch
                    self.update_board(row1, col1, ch)
                    return True
                row1 = row1 - 1
                col1 = col1 - 1
        elif direction == "DL":
            row1 = row1 + 1
            col1 = col1 - 1
            while self.is_inbounds(col1):
                if self.is_collision(row1 + 1, col1 - 1):
                    self._board_rep[row1][col1] = ch
                    if self.is_inbounds(row1 + 1) and self.is_inbounds(col1 - 1):
                        self._board_rep[row1 + 1][col1 - 1] = ch
                    self.update_board(row1, col1, ch)
                    return True
                row1 = row1 + 1
                col1 = col1 - 1

    def is_inbounds(self, num):
        """
        checks if inbounds
        """
        return (num < 4 and num >= 0)

    def is_collision(self, row, col):
        """
        checks if there's a collision
        """
        if (row > 3 or row < 0) or (col > 3 or col < 0) or self._board_rep[row][col] != "":
            return True

    def update_board(self, row1, col1, ch):
        """
        updates board
        """
        # UP
        new_row = row1 - 1
        new_col = col1
        if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][new_col] != "":
            self._board_rep[new_row][new_col] = ch
        # DOWN
        new_row = row1 + 1
        new_col = col1
        if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][new_col] != "":
            self._board_rep[new_row][new_col] = ch
        # RIGHT
        new_row = row1
        new_col = col1 + 1
        if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][new_col] != "":
            self._board_rep[new_row][new_col] = ch
        # LEFT
        new_row = row1
        new_col = col1 - 1
        if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][new_col] != "":
            self._board_rep[new_row][new_col] = ch
        # UP_RIGHT
        new_row = row1 - 1
        new_col = col1 + 1
        if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][new_col] != "":
            self._board_rep[new_row][new_col] = ch
        # UP_LEFT
        new_row = row1 - 1
        new_col = col1 - 1
        if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][new_col] != "":
            self._board_rep[new_row][new_col] = ch
        # DOWN_RIGHT
        new_row = row1 + 1
        new_col = col1 + 1
        if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][new_col] != "":
            self._board_rep[new_row][new_col] = ch
        # DOWN_LEFT
        new_row = row1 + 1
        new_col = col1 - 1
        if self.is_inbounds(new_row) and self.is_inbounds(new_col) and self._board_rep[new_row][new_col] != "":
            self._board_rep[new_row][new_col] = ch

    def __printBoard__(self):
        """
        print board for testing purposes
        """
        print(self._board_rep[0])
        print(self._board_rep[1])
        print(self._board_rep[2])
        print(self._board_rep[3])

    def getPrintBoard(self):
        """
        print board for testing purposes
        """
        return self.__printBoard__()

