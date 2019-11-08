'''
tyfu_TTS_agent.py
This is a agent which can play Toro-Tile Straight game.

Tianyuan Fu
Student Number: 1974487
UW NetID: tyfu@uw.edu

'''

from TTS_State import TTS_State

USE_CUSTOM_STATIC_EVAL_FUNCTION = False

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
        if self.board[i][j] == 'W':
          # up
          x = j
          y = self.pad_y(i - 1)
          if self.board[y][x] == ' ':
            TWF = TWF + 1
          # down
          x = j
          y = self.pad_y(i + 1)
          if self.board[y][x] == ' ':
            TWF = TWF + 1
          # left
          x = self.pad_x(j - 1)
          y = i
          if self.board[y][x] == ' ':
            TWF = TWF + 1
          # right
          x = self.pad_x(j + 1)
          y = i
          if self.board[y][x] == ' ':
            TWF = TWF + 1
          
          # upleft
          x = self.pad_x(j - 1)
          y = self.pad_y(i - 1)
          if self.board[y][x] == ' ':
            TWF = TWF + 1
          # upright
          x = self.pad_x(j + 1)
          y = self.pad_y(i - 1)
          if self.board[y][x] == ' ':
            TWF = TWF + 1
          # downleft
          x = self.pad_x(j - 1)
          y = self.pad_y(i + 1)
          if self.board[y][x] == ' ':
            TWF = TWF + 1
          # downright
          x = self.pad_x(j + 1)
          y = self.pad_y(i + 1)
          if self.board[y][x] == ' ':
            TWF = TWF + 1

        if self.board[i][j] == 'B':
          # up
          x = j
          y = self.pad_y(i - 1)
          if self.board[y][x] == ' ':
            TBF = TBF + 1
          # down
          x = j
          y = self.pad_y(i + 1)
          if self.board[y][x] == ' ':
            TBF = TBF + 1
          # left
          x = self.pad_x(j - 1)
          y = i
          if self.board[y][x] == ' ':
            TBF = TBF + 1
          # right
          x = self.pad_x(j + 1)
          y = i
          if self.board[y][x] == ' ':
            TBF = TBF + 1
          
          # upleft
          x = self.pad_x(j - 1)
          y = self.pad_y(i - 1)
          if self.board[y][x] == ' ':
            TBF = TBF + 1
          # upright
          x = self.pad_x(j + 1)
          y = self.pad_y(i - 1)
          if self.board[y][x] == ' ':
            TBF = TBF + 1
          # downleft
          x = self.pad_x(j - 1)
          y = self.pad_y(i + 1)
          if self.board[y][x] == ' ':
            TBF = TBF + 1
          # downright
          x = self.pad_x(j + 1)
          y = self.pad_y(i + 1)
          if self.board[y][x] == ' ':
            TBF = TBF + 1
    return TWF - TBF

  def custom_static_eval(self):
    # raise Exception("custom_static_eval not yet implemented.")
    height = len(self.board)
    width = len(self.board[0])

    TWF = 0
    TBF = 0

    for i in range(height):
      for j in range(width):
        # check the surrounding 8 tiles
        if self.board[i][j] == 'W':
          # up
          x = j
          y = self.pad_y(i - 1)
          if self.board[y][x] == 'W':
            TWF = TWF + 1
          # down
          x = j
          y = self.pad_y(i + 1)
          if self.board[y][x] == 'W':
            TWF = TWF + 1
          # left
          x = self.pad_x(j - 1)
          y = i
          if self.board[y][x] == 'W':
            TWF = TWF + 1
          # right
          x = self.pad_x(j + 1)
          y = i
          if self.board[y][x] == 'W':
            TWF = TWF + 1
          
          # upleft
          x = self.pad_x(j - 1)
          y = self.pad_y(i - 1)
          if self.board[y][x] == 'W':
            TWF = TWF + 1
          # upright
          x = self.pad_x(j + 1)
          y = self.pad_y(i - 1)
          if self.board[y][x] == 'W':
            TWF = TWF + 1
          # downleft
          x = self.pad_x(j - 1)
          y = self.pad_y(i + 1)
          if self.board[y][x] == 'W':
            TWF = TWF + 1
          # downright
          x = self.pad_x(j + 1)
          y = self.pad_y(i + 1)
          if self.board[y][x] == 'W':
            TWF = TWF + 1

        if self.board[i][j] == 'B':
          # up
          x = j
          y = self.pad_y(i - 1)
          if self.board[y][x] == 'B':
            TBF = TBF + 1
          # down
          x = j
          y = self.pad_y(i + 1)
          if self.board[y][x] == 'B':
            TBF = TBF + 1
          # left
          x = self.pad_x(j - 1)
          y = i
          if self.board[y][x] == 'B':
            TBF = TBF + 1
          # right
          x = self.pad_x(j + 1)
          y = i
          if self.board[y][x] == 'B':
            TBF = TBF + 1
          
          # upleft
          x = self.pad_x(j - 1)
          y = self.pad_y(i - 1)
          if self.board[y][x] == 'B':
            TBF = TBF + 1
          # upright
          x = self.pad_x(j + 1)
          y = self.pad_y(i - 1)
          if self.board[y][x] == 'B':
            TBF = TBF + 1
          # downleft
          x = self.pad_x(j - 1)
          y = self.pad_y(i + 1)
          if self.board[y][x] == 'B':
            TBF = TBF + 1
          # downright
          x = self.pad_x(j + 1)
          y = self.pad_y(i + 1)
          if self.board[y][x] == 'B':
            TBF = TBF + 1
    return TWF - TBF

  def pad_x(self, x):
    width = len(self.board[0])
    return x % width
  
  def pad_y(self, y):
    height = len(self.board)
    return y % height

  def move(self, point):
    new_board = self.board
    current_turn = self.whose_turn
    
    if current_turn == 'BLACK':
      new_turn = 'WHITE'
      new_board[point[0]][point[1]] = 'W'
    if current_turn == 'WHITE':
      new_turn = 'BLACK'
      new_board[point[0]][point[1]] = 'B'

    return TTS_State.__init__(new_board, new_turn)

# The following is a skeleton for the function called parameterized_minimax,
# which should be a top-level function in each agent file.
# A tester or an autograder may do something like
# import ABC_TTS_agent as player, call get_ready(),
# and then it will be able to call tryout using something like this:
# results = player.parameterized_minimax(**kwargs)

def parameterized_minimax(
       current_state=None,
       max_ply=2,
       alpha_beta=False, 
       use_custom_static_eval_function=False):

  # All students, add code to replace these default
  # values with correct values from your agent (either here or below).
  DATA = {}
  # DATA['CURRENT_STATE_STATIC_VAL'] = -1000.0
  # DATA['N_STATES_EXPANDED'] = 0
  # DATA['N_STATIC_EVALS'] = 0
  # DATA['N_CUTOFFS'] = 0

  # STUDENTS: You may create the rest of the body of this function here.
  if max_ply == 0:
    if use_custom_static_eval_function == True:
      DATA['CURRENT_STATE_STATIC_VAL'] = MY_TTS_State.custom_static_eval(current_state)
    else:
      DATA['CURRENT_STATE_STATIC_VAL'] = MY_TTS_State.static_eval(current_state)

    DATA['N_STATES_EXPANDED'] = 1
    DATA['N_STATIC_EVALS'] = 1
    DATA['N_CUTOFFS'] = 0
    return DATA

  else:
    if use_custom_static_eval_function == True:
      DATA['CURRENT_STATE_STATIC_VAL'] = MY_TTS_State.custom_static_eval(current_state)
    else:
      DATA['CURRENT_STATE_STATIC_VAL'] = MY_TTS_State.static_eval(current_state)
    successors = get_all_successor_states(current_state)
    for s in successors:
      new_data = parameterized_minimax(s, max_ply - 1, alpha_beta, use_custom_static_eval_function)
      if (s.whose_turn == 'WHITE' and new_data['CURRENT_STATE_STATIC_VAL'] > DATA['CURRENT_STATE_STATIC_VAL']) \
        or (s.whose_turn == 'BLACK' and new_data['CURRENT_STATE_STATIC_VAL'] < DATA['CURRENT_STATE_STATIC_VAL']):
        DATA['CURRENT_STATE_STATIC_VAL'] = new_data['CURRENT_STATE_STATIC_VAL']
      DATA['N_STATES_EXPANDED'] = DATA['N_STATES_EXPANDED'] + new_data['N_STATES_EXPANDED']
      DATA['N_STATIC_EVALS'] = DATA['N_STATIC_EVALS'] + new_data['N_STATIC_EVALS']
      DATA['N_CUTOFFS'] = DATA['N_CUTOFFS'] + new_data['N_CUTOFFS']

  # Actually return all results...
  return(DATA)

def take_turn(current_state, last_utterance, time_limit):

    # Compute the new state for a move.
    # Start by copying the current state.
    new_state = MY_TTS_State(current_state.board)
    # Fix up whose turn it will be.
    who = current_state.whose_turn
    new_who = 'B'  
    if who=='B': new_who = 'W'  
    new_state.whose_turn = new_who
    
    # Place a new tile
    location = _find_next_vacancy(new_state.board)
    if location==False: return [[False, current_state], "I don't have any moves!"]
    new_state.board[location[0]][location[1]] = who

    # Construct a representation of the move that goes from the
    # currentState to the newState.
    move = location

    # Make up a new remark
    new_utterance = "I'll think harder in some future game. Here's my move"

    return [[move, new_state], new_utterance]

def _find_next_vacancy(b):
    for i in range(len(b)):
      for j in range(len(b[0])):
        if b[i][j]==' ': return (i,j)
    return False

def get_all_successor_states(current_state):
  successors = []
  board = current_state.board
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == ' ':
        successors.append(MY_TTS_State.move(current_state, (i, j)))
  return successors

def moniker():
    return "Medusa" # Return your agent's short nickname here.

def who_am_i():
    return """My name is Medusa, created by Tianyuan Fu (tyfu). 
    I consider myself to be an aggressive line-blocker."""

def get_ready(initial_state, k, who_i_play, player2Nickname):
    # do any prep, like eval pre-calculation, here.
    return "OK"
