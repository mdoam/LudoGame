# Author: Mi Do
# GitHub username: mdoam
# Date: 07/31/2022
# Description: Ludo game


class Player:
    def __init__(self):
        self._position = None
        self._start = None
        self._end = None
        self._currentP = -1
        self._currentQ = -1
        self._state = False  # F: still playing, T: won and finished the game

    def set_position(self, pos):
        self._position = pos

    def set_start_end(self, pos):
        if pos == 'A':
            self._start = 1
            self._end = 50
        if pos == 'B':
            self._start = 15
            self._end = 8
        if pos == 'c':
            self._start = 29
            self._end = 22
        if pos == 'D':
            self._start = 43
            self._end = 36

    def set_current_p(self, num):
        self._currentP = num

    def set_current_q(self, num):
        self._currentQ = num

    def set_state(self):
        self._state = True

    def get_position(self):
        return self._position

    def get_completed(self):
        return self._state

    def get_token_p_step_count(self):
        return self._currentP

    def get_token_q_step_count(self):
        return self._currentQ

    def get_space_name(self, current):
        if current == -1:
            return 'H'
        if current == 0:
            return 'R'
        if current == 'E':
            return self._position
        if current in range(1, 8) or current in range(50, 57) or current in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']:
            return 'A'
        if current in range(8, 22) or current in ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']:
            return 'B'
        if current in range(22, 36) or current in ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']:
            return 'C'
        if current in range(36, 50) or current in ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']:
            return 'D'


class LudoGame:
    """
    represents the Ludo game as playing
    """
    def __init__(self):
        self._list_players = {}
        self._board = {}

    def play_game(self, players_area, turns1):
        # initializes player with given info
        for pos in players_area:
            player = Player()
            player.set_position(pos)
            player.set_start_end(pos)
            self._list_players[pos] = player

        # move token according to the turns list
        for turn in turns:
            flag = False
            stalk = False
            player = turn[0]
            player = self._list_players[player]
            num = turn













players = ['A', 'B']
turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4),
         ('B', 6), ('B', 4), ('B', 1), ('B', 2),
         ('A', 6), ('A', 4), ('A', 6), ('A', 3),
         ('A', 5), ('A', 1), ('A', 5), ('A', 4)]
game = LudoGame()
current_tokens_space = game.play_game(players, turns)
