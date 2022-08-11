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
        self._position = None
        self._start = None
        self._end = None
        self._currentP = -1
        self._currentQ = -1
        self._state = False  # F: still playing, T: won and finished the game

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
        """
        set the current position of token p
        """
        self._currentP = num

    def set_current_q(self, num):
        """
        set the current position of token q
        """
        self._currentQ = num

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

    def get_completed(self):
        """
        gets the current state of the player: win if true
        Otherwise, return False
        """
        return self._state

    def get_token_p_step_count(self):
        """
        returns the total steps the token p has taken on the board
        """
        return self._currentP

    def get_token_q_step_count(self):
        """
        returns the total steps the token q has taken on the board
        """
        return self._currentQ

    def get_space_name(self, current):
        """
        returns the name of the space the token has landed on the board
        """
        if current == -1:
            return 'H'
        elif current == 0:
            return 'R'
        elif current == 'E':
            return 'E'
        elif current > 50:
            return self._position + (current % 50)
        else:
            return str(current)


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
        self._board = []
        self._home_squareA = []
        self._home_squareB = []
        self._home_squareC = []
        self._home_squareD = []

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

        # move token according to the turns list
        for turn in turns:
            flag = False
            stalk = False
            player = turn[0]
            player = self._list_players[player]
            num = turn

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

    def move_token(self, player, token, step):
        """
        takes three parameters: player, token, and moving step
        updates the token's total steps accordingly
        kicks out opponent's token as needed
        flags stalked if needed
        follows the priority rule
        """
        pass














players = ['A', 'B']
turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4),
         ('B', 6), ('B', 4), ('B', 1), ('B', 2),
         ('A', 6), ('A', 4), ('A', 6), ('A', 3),
         ('A', 5), ('A', 1), ('A', 5), ('A', 4)]
game = LudoGame()
current_tokens_space = game.play_game(players, turns)
