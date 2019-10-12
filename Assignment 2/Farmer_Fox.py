'''

Farmer_Fox.py
by Tianyuan Fu
UWNetID: tyfu
Student number: 1974487

Assignment 2, in CSE 415, Autumn 2019.
 
This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.


'''

# <METADATA>
SOLUZION_VERSION = "1.0"
PROBLEM_NAME = "FFCG"
PROBLEM_VERSION = "1.0"
PROBLEM_AUTHORS = ['Tianyuan FU']
PROBLEM_CREATION_DATE = "09-Oct-2018"
PROBLEM_DESC=\
'''
This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
A farmer has to get his fox, chicken and grain across the river.
The boat can only hold the farmer and one item.
The fox cannot be left alone with the chicken.
The chicken cannot be left alone with the grain.
'''
# </METADATA>
# <COMMON_DATA>
# index in the array
FARMER = 0
FOX = 1
CHICKEN = 2
GRAIN = 3
LEFT = 0
RIGHT = 1
PARTNER_DIC = {None: 'no other person',
				1: 'the fox',
				2: 'the chicken',
				3: 'the grain'}
# </COMMON_DATA>

# <COMMON_CODE>
class State():
	def __init__(self, d = None):
		if d == None:
			d = {
				'people': [LEFT, LEFT, LEFT, LEFT],
				'boat': LEFT
				}
		self.d = d 

	def __eq__(self, s2):
		for prop in ['people', 'boat']:
			if self.d[prop] != s2.d[prop]:
				return False
		return True
	
	def __str__(self):
		# produce a textual description of a state.
		# status of people
		p = self.d['people']
		if p[FARMER] == LEFT:
			side = 'left'
		else: 
			side = 'right'
		txt = '\nThe farmer is on the ' + side
		
		if p[FOX] == LEFT: side = 'left'
		else: side = 'right'
		txt += '\nThe fox is on the ' + side

		if p[CHICKEN] == LEFT: side = 'left'
		else: side = 'right'
		txt += '\nThe chicken is on the ' + side
		
		if p[GRAIN] == LEFT: side = 'left'
		else: side = 'right'
		txt += '\nThe grain is on the ' + side

		# status of boat
		if self.d['boat'] == RIGHT: side = 'right'
		else: side = 'left'
		txt += '\nThe boat is on the ' + side + '.\n'

		return txt

	def __hash__(self):
		return (self.__str__()).__hash__()

	def copy(self):
		# Performs an appropriately deep copy of a state,
		# for use by operators in creating new states.
		news = State({})
		news.d['people']=[self.d['people'][each_ffcg] for each_ffcg in [FARMER, FOX, CHICKEN, GRAIN]]
		news.d['boat'] = self.d['boat']
		return news 

	# @param together is the index of the person the farmer want to take with
	# the farmer does not take anyone by default
	def can_move(self, together = None):
		news = self.copy()
		# tests whether it is legal to move the boat take 1 farmer and 1 other
		side = news.d['boat']
		p = news.d['people']

		# before moving
		if together != None:
			# the person should be on the same side with the boat
			if p[together] != side: return False
			if together not in [FOX, CHICKEN, GRAIN]: return False

		# after moving
		side = 1 - side
		p[0] = 1 - p[0]
		if together != None:
			p[together] = 1 - p[together]
		# chicken should not be along with grain / fox
		if sum(p) == 2:
			if p[CHICKEN] == p[FOX] or p[CHICKEN] == p[GRAIN]:
				return False
		return True
		
	def move(self, together = None):
		# Assume the paramater for making the movement is legal. 
		news = self.copy()
		# side = news.d['boat']
		p = news.d['people']
		# farmer
		p[FARMER] = 1 - p[FARMER]
		# boat
		# side = 1 - side
		news.d['boat'] = 1 - news.d['boat']
		if together != None:
			p[together] = 1 - p[together]
		return news

def goal_test(s):
	p = s.d['people']
	return (sum(p) == 4)

def goal_message(s):
	return 'Congratulations on successfully guiding the farmer, fox, chicken and grain across the river!'

class Operator:
	def __init__(self, name, precond, state_transf):
		self.name = name
		self.precond = precond
		self.state_transf = state_transf

	def is_applicable(self, s):
		return self.precond(s)

	def apply(self, s):
		return self.state_transf(s)
# </COMMON_CODE>

# <INITIAL_STATE>
CREATE_INITIAL_STATE = lambda: State(d = {'people': [LEFT, LEFT, LEFT, LEFT], 'boat': LEFT})
# </INITIAL_STATE>

# <OPERATORS>
take_along_options = [None, 1, 2, 3]

OPERATORS = [Operator(
	'Cross the river with ' + str(PARTNER_DIC[op]),
	lambda s, op1 = op: s.can_move(op1),
	lambda s, op1 = op: s.move(op1))
	for op in take_along_options]
# </OPERATORS>

# <GOAL_TEST>
GOAL_TEST = lambda s: goal_test(s)
# </GOAL_TEST>

# <GOAL_MESSAGE_FUNCTION>
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
# </GOAL_MESSAGE_FUNCTION>

