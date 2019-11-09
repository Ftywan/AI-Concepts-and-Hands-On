"""
tyfu_TTS_agent.py
This is a agent which can play Toro-Tile Straight game.

Tianyuan Fu
Student Number: 1974487
UW NetID: tyfu@uw.edu

"""

from TTS_State import TTS_State
import random
import time
from threading import Event, Thread
stop_event = Event()

USE_CUSTOM_STATIC_EVAL_FUNCTION = False
INITIAL_STATE = [
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
]
PLAYER_2_NICKNAME = "Tarnimoto"
K = 2
global max_location, max_value, min_location, min_value


# TODO: customized static evaluation function
class MY_TTS_State(TTS_State):
    def static_eval(self):
        if USE_CUSTOM_STATIC_EVAL_FUNCTION:
            return self.custom_static_eval()
        else:
            return self.basic_static_eval()

    def basic_static_eval(self):
        # raise Exception("basic_static_eval not yet implemented.")
        height = len(self.board)
        width = len(self.board[0])

        TWF = 0
        TBF = 0

        for i in range(height):
            for j in range(width):
                # check the surrounding 8 tiles
                if self.board[i][j] == "W":
                    # up
                    x = j
                    y = self.pad_y(i - 1)
                    if self.board[y][x] == " ":
                        TWF = TWF + 1
                    # down
                    x = j
                    y = self.pad_y(i + 1)
                    if self.board[y][x] == " ":
                        TWF = TWF + 1
                    # left
                    x = self.pad_x(j - 1)
                    y = i
                    if self.board[y][x] == " ":
                        TWF = TWF + 1
                    # right
                    x = self.pad_x(j + 1)
                    y = i
                    if self.board[y][x] == " ":
                        TWF = TWF + 1

                    # upleft
                    x = self.pad_x(j - 1)
                    y = self.pad_y(i - 1)
                    if self.board[y][x] == " ":
                        TWF = TWF + 1
                    # upright
                    x = self.pad_x(j + 1)
                    y = self.pad_y(i - 1)
                    if self.board[y][x] == " ":
                        TWF = TWF + 1
                    # downleft
                    x = self.pad_x(j - 1)
                    y = self.pad_y(i + 1)
                    if self.board[y][x] == " ":
                        TWF = TWF + 1
                    # downright
                    x = self.pad_x(j + 1)
                    y = self.pad_y(i + 1)
                    if self.board[y][x] == " ":
                        TWF = TWF + 1

                if self.board[i][j] == "B":
                    # up
                    x = j
                    y = self.pad_y(i - 1)
                    if self.board[y][x] == " ":
                        TBF = TBF + 1
                    # down
                    x = j
                    y = self.pad_y(i + 1)
                    if self.board[y][x] == " ":
                        TBF = TBF + 1
                    # left
                    x = self.pad_x(j - 1)
                    y = i
                    if self.board[y][x] == " ":
                        TBF = TBF + 1
                    # right
                    x = self.pad_x(j + 1)
                    y = i
                    if self.board[y][x] == " ":
                        TBF = TBF + 1

                    # upleft
                    x = self.pad_x(j - 1)
                    y = self.pad_y(i - 1)
                    if self.board[y][x] == " ":
                        TBF = TBF + 1
                    # upright
                    x = self.pad_x(j + 1)
                    y = self.pad_y(i - 1)
                    if self.board[y][x] == " ":
                        TBF = TBF + 1
                    # downleft
                    x = self.pad_x(j - 1)
                    y = self.pad_y(i + 1)
                    if self.board[y][x] == " ":
                        TBF = TBF + 1
                    # downright
                    x = self.pad_x(j + 1)
                    y = self.pad_y(i + 1)
                    if self.board[y][x] == " ":
                        TBF = TBF + 1
        return TWF - TBF

    def custom_static_eval(self):
        TWF = 0
        TBF = 0
        height = len(self.board)
        width = len(self.board[0])

        for i in range(height):
            for j in range(width):
                if self.board[i][j] == 'W':
                    TWF += self.w_value(i, j)
                if self.board[i][j] == 'B':
                    TBF += self.b_value(i, j)
        return TWF - TBF
    
    def w_value(self, i, j):
        board = self.board
        height = len(board)
        width = len(board[0])
        if board[i][j] == 'W':
            board[i][j] = ' '
            return 10 * self.w_value(i, (j + 1) % width) * self.w_value((i + 1) % height, j)\
                * self.w_value(i, (j - 1) % width) * self.w_value((i - 1) % height, j)\
                * self.w_value((i + 1) % height, (j + 1) % width) * self.w_value((i - 1) % height, (j + 1) % width)\
                * self.w_value((i + 1) % height, (j - 1) % width) * self.w_value((i - 1) % height, (j - 1) % width)
        else: 
            return 1
    
    def b_value(self, i, j):
        board = self.board
        height = len(board)
        width = len(board[0])
        if board[i][j] == 'W':
            board[i][j] = ' '
            return 10 * self.b_value(i, (j + 1) % width) * self.b_value((i + 1) % height, j)\
                * self.b_value(i, (j - 1) % width) * self.b_value((i - 1) % height, j)\
                * self.b_value((i + 1) % height, (j + 1) % width) * self.b_value((i - 1) % height, (j + 1) % width)\
                * self.b_value((i + 1) % height, (j - 1) % width) * self.b_value((i - 1) % height, (j - 1) % width)
        else: 
            return 1

    def pad_x(self, x):
        width = len(self.board[0])
        return x % width

    def pad_y(self, y):
        height = len(self.board)
        return y % height

    def move(self, point):
        new_state = self
        turn = self.whose_turn

        if turn == "B":
            new_state.whose_turn = "W"
            new_state.board[point[0]][point[1]] = "W"
        if turn == "W":
            new_state.whose_turn = "B"
            new_state.board[point[0]][point[1]] = "B"

        return new_state


# The following is a skeleton for the function called parameterized_minimax,
# which should be a top-level function in each agent file.
# A tester or an autograder may do something like
# import ABC_TTS_agent as player, call get_ready(),
# and then it will be able to call tryout using something like this:
# results = player.parameterized_minimax(**kwargs)
def parameterized_minimax(
    current_state=None, max_ply=2, use_alpha_beta=False, use_basic_static_eval=True
):
    current_state = MY_TTS_State(current_state.board)
    global n_state_expand, n_cutoff, n_static_eval
    n_state_expand = 0
    n_static_eval = 0
    n_cutoff = 0
    # All students, add code to replace these default
    # values with correct values from your agent (either here or below).

    provisional = minimax(current_state, use_alpha_beta, use_basic_static_eval, -float("inf"), float("inf"), max_ply)
    DATA = {}
    DATA['CURRENT_STATE_STATIC_VAL'] = provisional
    DATA['N_STATES_EXPANDED'] = n_state_expand
    DATA['N_STATIC_EVALS'] = n_static_eval
    DATA['N_CUTOFFS'] = n_cutoff
    # STUDENTS: You may create the rest of the body of this function here.
    # Actually return all results...
    return DATA

def minimax(current_state, use_alpha_beta, use_basic_static_eval,alpha, beta, ply_left):
    global n_cutoff, n_state_expand, n_static_eval
    current_state = MY_TTS_State(current_state.board)
    successors = get_all_successor_states(current_state)
    n_state_expand += 1

    if ply_left == 0 or len(successors) == 0:
        if use_basic_static_eval == True:
            current_value = current_state.static_eval()
        else:
            current_value = current_state.static_eval()
        n_static_eval += 1

        return current_value

    current_player = current_state.whose_turn
    if current_player == "W":
        provisional = -float("inf")
    else:
        provisional = float('inf')     
    
    for s in successors:
        s = MY_TTS_State(s.board)
        new_value = minimax(s, use_alpha_beta, use_basic_static_eval, alpha, beta, ply_left - 1)
        if current_player == "W":
            if new_value > provisional:
                provisional = new_value
            if use_alpha_beta:
                alpha = max(alpha, new_value)
                if alpha >= beta:
                    n_cutoff += 1
                    break
        else:
            if new_value < provisional:
                provisional = new_value
            if use_alpha_beta:
                beta = min(beta, new_value)
                if alpha >= beta:
                    n_cutoff += 1
                    break
    return provisional

def take_turn(current_state, last_utterance, time_limit):
    global max_value, max_location, min_value, min_location
    # Compute the new state for a move.
    # Start by copying the current state.
    new_state = MY_TTS_State(current_state.board)
    # Fix up whose turn it will be.
    who = current_state.whose_turn
    new_who = "B"
    if who == "B":
        new_who = "W"
    new_state.whose_turn = new_who    
    current_state = MY_TTS_State(current_state.board)

    # Place a new tile
    # location: a point tuple
    successors = get_all_successor_states(current_state)

    max_location = _find_next_vacancy(new_state.board)
    min_location = max_location
    max_value = parameterized_minimax(current_state.move(max_location))['CURRENT_STATE_STATIC_VAL']
    min_value = max_value

    action_tread = Thread(target=iddfs, args=(successors,stop_event))
    action_tread.start()
    action_tread.join(timeout=time_limit)

    stop_event.set()

    if new_who == "W":
        location = max_location
    if new_who == "B":
        location = min_location

    if location == False:
        return [[False, current_state], "I don't have any moves!"]
    new_state.board[location[0]][location[1]] = who

    # Construct a representation of the move that goes from the
    # currentState to the newState.
    move = location

    # Make up a new remark
    new_utterance = get_utterance()

    return [[move, new_state], new_utterance]

def iddfs(successors, stop_event):
    global max_value, max_location, min_value, min_location
    depth = 1
    
    while depth <= len(successors) and not stop_event.is_set():
        for s in successors:
            point = successors[s]
            next_state_data = parameterized_minimax(s, depth, True, False)
            if next_state_data["CURRENT_STATE_STATIC_VAL"] > max_value:
                max_location = point
                max_value = next_state_data["CURRENT_STATE_STATIC_VAL"]
            if next_state_data["CURRENT_STATE_STATIC_VAL"] < min_value:
                min_location = point
                min_value = next_state_data["CURRENT_STATE_STATIC_VAL"]
            depth += 1
    

def _find_next_vacancy(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == " ":
                return (i, j)
    return False


# input: a state object
# output: a dict which map the next possible state object to the point newly added
def get_all_successor_states(current_state):
    current_state = MY_TTS_State(current_state.board)
    successors = {}
    board = current_state.board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                new_state = current_state.move((i, j))
                successors[new_state] = (i, j)
    return successors


def get_utterance():
    utterance = [
        "I'll think harder in some future game. Here's my move",
        "Man! Good Move!",
        "Let me block you!",
        "Good! You didn't get what I mean!",
        "Haha! I think I'm gonna win!",
        "You know you are one of the best player I have ever seen!",
        "Some day you gonna beat me, but not today!",
        "Think carefully before making your move~ I get you some tricks.",
        "Seems you made a nice move",
        "Are you feeling in a trap?",
    ]
    return utterance[random.randint(0, len(utterance) - 1)]


def moniker():
    return "Medusa"  # Return your agent's short nickname here.


def who_am_i():
    return """My name is Medusa, created by Tianyuan Fu (tyfu). 
	I consider myself to be an aggressive line-blocker."""


def get_ready(initial_state, k, who_i_play, player2Nickname):
    # do any prep, like eval pre-calculation, here.
    INITIAL_STATE = initial_state
    K = k
    WHO_I_PLAY = who_i_play
    PLAYER_2_NICKNAME = player2Nickname
    return "OK"

