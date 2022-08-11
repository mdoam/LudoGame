# Author: Mi Do
# GitHub username: mdoam
# Date: 07/31/2022
# Description: Ludo game


class Player:
    """
    represents the player who plays the Ludo game with two token p and q
    records the following information about the player:
    - home yard position ('A', 'B', 'C', 'D')
    - the current position of each token
    - the ready to move and final position before entering the home squares
    - the state of the player: win or lose
    and methods to get, set, or update these private variables
    """
    def __init__(self):
        """
        initializes the private data members
        """
        self._position = None  # A, B, C, or D
        self._start = None
        self._end = None
        self._currentP = 'H'
        self._currentQ = 'H'
        self._state = False  # F: still playing, T: won and finished the game
        self._stepP = -1
        self._stepQ = -1

    def set_position(self, pos):
        """
        sets player home yard position
        """
        self._position = pos

    def set_start_end(self, pos):
        """
        sets the ready and end position before reach home squares
        """
        if pos == 'A':
            self._start = 1
            self._end = 50
        elif pos == 'B':
            self._start = 15
            self._end = 8
        elif pos == 'C':
            self._start = 29
            self._end = 22
        else:
            self._start = 43
            self._end = 36

    def set_step_p(self, step):
        """
        set the total step of token p
        """
        self._stepP += step
        if self._stepP > 57:
            diff = self._stepP - 57
            self._stepP = 57 - diff

    def set_step_q(self, step):
        """
        set the total step of token p
        """
        self._stepQ += step
        if self._stepQ > 57:
            diff = self._stepQ - 57
            self._stepQ = 57 - diff

    def set_current_p(self, num):
        """
        set the current position of token p
        """
        self._currentP = self.get_space_name(num)

    def set_current_q(self, num):
        """
        set the current position of token q
        """
        self._currentQ = self.get_space_name(num)

    def set_state(self):
        """
        sets the state for the player: True if win
        Otherwise False
        """
        self._state = True

    def get_position(self):
        """
        gets the home yard position
        """
        return self._position

    def get_start(self):
        """
        gets the start position
        """
        return self._start

    def get_end(self):
        """
        gets the end position
        """
        return self._end

    def get_completed(self):
        """
        gets the current state of the player: win if true
        Otherwise, return False
        """
        return self._state

    def get_token_p_current(self):
        """
        returns the current position of token P
        """
        return self._currentP

    def get_token_q_current(self):
        """
        returns the current position of token P
        """
        return self._currentQ

    def get_token_p_step_count(self):
        """
        returns the total steps the token p has taken on the board
        """
        return self._stepP

    def get_token_q_step_count(self):
        """
        returns the total steps the token q has taken on the board
        """
        return self._stepQ

    def get_space_name(self, current):
        """
        returns the name of the space the token has landed on the board
        """
        if current == -1:
            return 'H'
        elif current == 0:
            return 'R'
        elif current == 57:
            return 'E'
        elif current > 50:
            return str(self._position) + str(current % 50)
        else:
            return (current + self._start - 1) % 56


class LudoGame:
    """
    represents the Ludo game as playing
    contains information about the players and the state of the board
    """
    def __init__(self):
        """
        initializes the private data members
        """
        self._list_players = {}
        self._board = [0] * 57

    def play_game(self, players_area, turns1):
        """
        takes two parameters players' list with their positions and players' turns
        creates players' objects from the given position
        update the player's steps and the board state based on the turn list
        returns a list of string with current steps of all token for each player after the turn list
        """
        # initializes player with given info
        for pos in players_area:
            player = Player()
            player.set_position(pos)
            player.set_start_end(pos)
            self._list_players[pos] = player

        # move token according to the turn list
        for turn in turns1:
            # who's turn with roll
            who = turn[0]
            player = self._list_players[who]
            roll = turn[1]

            step_p = player.get_token_p_step_count()
            step_q = player.get_token_q_step_count()

            # if roll = 6, let token out if still in home yard
            if roll == 6:
                if step_p == -1:
                    step_p += 1
                    player.set_step_p(1)
                    player.set_current_p(step_p)

                    continue
                elif step_q == -1:
                    step_q += 1
                    player.set_step_q(1)
                    player.set_current_q(step_q)

                    continue

            # otherwise
            if step_p + roll == 57:
                self.move_token(player, 'p', roll)
            elif step_q + roll == 57:
                self.move_token(player, 'q', roll)
            elif self._board[step_p + roll] != 0 and step_p + roll != step_q:
                self.move_token(player, 'p', roll)
            elif self._board[step_q + roll] != 0 and step_q + roll != step_p:
                self.move_token(player, 'q', roll)
            else:
                if step_p == -1:
                    self.move_token(player, 'q', roll)
                elif step_q == -1:
                    self.move_token(player, 'p', roll)
                elif step_p < step_q:
                    self.move_token(player, 'p', roll)
                elif step_p > step_q:
                    self.move_token(player, 'q', roll)
                else:
                    self.move_token(player, 'p', roll)
                    self.move_token(player, 'q', roll)

        return_list = []
        for player in self._list_players:
            player = self._list_players[player]
            return_list.append(str(player.get_token_p_current()))
            return_list.append(str(player.get_token_q_current()))
        return return_list

    def get_player_by_position(self, pos):
        """
        takes player's position
        returns the player object
        if not found, returns "Player not found!"
        """
        if pos in self._list_players:
            return self._list_players[pos]
        else:
            return "Player not found!"

    def get_board(self):
        return self._board

    def move_token(self, player, token, step):
        """
        takes three parameters: player, token, and moving step
        updates the token's total steps accordingly
        kicks out opponent's token as needed
        flags stalked if needed
        follows the priority rule
        """
        if token == 'p':
            old_board = (player.get_token_p_step_count() + player.get_start()) % 56
            self._board[old_board] = 0
            player.set_step_p(step)
            player.set_current_p(player.get_token_p_step_count())
            total_step = player.get_token_p_step_count()
            current_board = (total_step + player.get_start()) % 56
            if self._board[current_board] == 0:
                self._board[current_board] = [{player.get_position(): token}]

        else:
            old_board = (player.get_token_q_step_count() + player.get_start()) % 56
            self._board[old_board] = 0
            player.set_step_q(step)
            player.set_current_q(player.get_token_q_step_count())
            total_step = player.get_token_q_step_count()
            current_board = (total_step + player.get_start()) % 56
            if self._board[current_board] == 0:
                self._board[current_board] = {player.get_position(): token}


